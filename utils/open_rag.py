import re
import numpy as np
import requests
import pickle
import json
import math
import time

from typing import List
from collections import defaultdict, Counter

class Content:
    def __init__(self, content_text, content_type, parent=None):
        self.content_text = content_text
        self.sentences = []
        self.content_type = content_type  # paragraph, table, pre-formatted, etc.
        self.parent = parent  # parent node
        self.create_sentence_list()
        self.topics = []  # Topics for the content

    def __repr__(self):
        return f"Type: {self.content_type}, Content: {self.content_text[:30]}..."

    def create_sentence_list(self):
        if self.content_type == 'paragraph':
            self.sentences = split_paragraph_into_sentences(self.content_text)
        elif self.content_type == 'table':
            # Extract sentences from table notes (if any)
            table_notes = re.findall(r'Note: (.*?)$', self.content_text, re.MULTILINE)
            self.sentences = [note.strip() for note in table_notes if note.strip()]
        elif self.content_type == 'pre-formatted':
            # Extract comments from code
            comments = re.findall(r'#.*|//.*|/\*.*?\*/', self.content_text, re.DOTALL)
            self.sentences = [comment.strip() for comment in comments if comment.strip()]

class BM25:
    def __init__(self, corpus: List[List[str]], k1=1.5, b=0.75):
        self.corpus = corpus
        self.corpus_size = len(corpus)
        self.avgdl = sum(len(doc) for doc in corpus) / self.corpus_size
        self.doc_freqs = []
        self.idf = {}
        self.k1 = k1
        self.b = b
        self.inv_index = {}
        self.initialize()

    def initialize(self):
        df = {}
        invdex ={}
        # Term frequency in a doc
        for i, document in enumerate(self.corpus):
            # Count frequencies of terms in documents
            frequencies = Counter(document)
            self.doc_freqs.append(frequencies)
            
            # Document frequency calculation for terms (words)
            for word, freq in frequencies.items():
                if word in df:
                    df[word] += 1
                else:
                    df[word] = 1
                if (word in invdex):
                    doc_list = invdex[word]
                    doc_list.append(i)
                    invdex[word] = doc_list
                else:
                    invdex[word] = [i]   
        self.inv_index = invdex
        # Calculating inverse document frequency
        # Make sure it is always greater than 1, so that the log is a positive value
        for word, freq in df.items():
            self.idf[word] = math.log((self.corpus_size - freq + 0.5) / (freq + 0.5) + 1)

    def get_score(self, document: List[str], query: List[str]):
        score = 0.0
        doc_len = len(document)
        frequencies = Counter(document)

        for word in query:
            if word in frequencies:
                tf = frequencies[word]
                # Term frequency and document length normalization
                denom = tf + self.k1 * (1 - self.b + self.b * doc_len / self.avgdl)
                score += self.idf.get(word, 0) * tf * (self.k1 + 1) / denom

        return score

    def get_scores(self, query: List[str]):
        scores = [self.get_score(doc, query) for doc in self.corpus]
        return scores
        
class Node:
    def __init__(self, level, header, parent=None, node_id=-1):
        self.level = level
        self.node_id = node_id
        self.header = header
        self.parent = parent
        self.content = ""
        self.chunk_list = []
        self.children = []
        self.header_embedding = None
        self.content_embeddings = None
        self.topic_embeddings = None  # Embeddings of topics generated for the content
        self.summary = None  # Summary for the content
        self.summary_embedding = None  # Embedding for the summary

    def __repr__(self):
        return f"{self.header} ({len(self.children)} subsections)"

    def set_node_id(self, node_id):
        self.node_id = node_id

def load_embedding_model(model_path='../bge-m3.model'):
    with open(model_path, 'rb') as f:
        return pickle.load(f)

def normalize_l2(x):
    x = np.array(x)
    norm = np.linalg.norm(x, axis=-1, keepdims=True)
    return np.where(norm == 0, x, x / norm)

def split_markdown(text):
    # Define regular expressions for tables, pre-formatted text, and paragraphs
    table_regex = r'((?:\|.*?\|\n)+)'  # Markdown table pattern
    preformatted_regex = r'(```[\s\S]*?```|<pre>[\s\S]*?</pre>)'  # Code blocks
    
    # Split text into pre-formatted and other content
    chunks = re.split(preformatted_regex, text)
    result = []

    for chunk in chunks:
        if re.match(preformatted_regex, chunk):
            result.append({'type': 'pre-formatted', 'content': chunk})
        else:
            parts = re.split(table_regex, chunk)
            for part in parts:
                if re.match(table_regex, part):
                    result.append({'type': 'table', 'content': part})
                else:
                    paragraphs = re.split(r'\n{2,}', part)
                    result.extend([{'type': 'paragraph', 'content': p} for p in paragraphs if p.strip()])
    
    return result

def split_paragraph_into_sentences(paragraph):
    # Split paragraph into sentences using common punctuation patterns
    sentence_regex = r'(?<=[.!?])\s+(?=[A-Z])'
    sentences = re.split(sentence_regex, paragraph)
    return [s.strip() for s in sentences if s.strip()]

def parse_markdown_to_tree(markdown_text):
    node_count = 0
    lines = markdown_text.split('\n')
    root = Node(level=0, header='root',node_id=node_count)
    node_count += 1
    current_node = root
    content_block = ''
    node_stack = [root]  # Stack to manage parent-child relationships

    for line in lines:
        match = re.match(r'^(#+)\s*(.*)', line)
        if match:
            if content_block:
                add_content_to_node(current_node, content_block)
                content_block = ''
            level = len(match.group(1))
            header = match.group(2).strip()
            # Create new node
            new_node = Node(level=level, header=header,node_id=node_count)
            node_count += 1
            # Find correct parent for the new node
            while node_stack and node_stack[-1].level >= level:
                node_stack.pop()
            parent_node = node_stack[-1] if node_stack else root
            parent_node.children.append(new_node)
            new_node.parent = parent_node
            node_stack.append(new_node)
            current_node = new_node
        else:
            content_block += line + '\n'

    if content_block:
        add_content_to_node(current_node, content_block)

    return root
    

def add_content_to_node(node, content_block):
    content_block = content_block.strip()
    node.content = content_block
    chunks = split_markdown(content_block)
    for chunk in chunks:
        content_type = chunk['type']
        content_text = chunk['content']
        content_obj = Content(content_text, content_type, node)
        content_obj.topics = generate_topics_for_content(content_text)
        node.chunk_list.append(content_obj)
    # Generate summary for the node content
    node.summary = generate_content_summary(content_block)

def create_embeddings_for_tree(root_node, embedding_model):
    def traverse_and_embed(node):
        # Create embeddings for header, content, and summary
        node.header_embedding = embedding_model.encode([node.header])['dense_vecs']
        if node.summary:
            node.summary_embedding = embedding_model.encode([node.summary])['dense_vecs']
        if node.chunk_list:
            sentences = [sentence for chunk in node.chunk_list for sentence in chunk.sentences]
            if sentences:
                node.content_embeddings = embedding_model.encode(sentences)['dense_vecs']
            # Create embeddings for topics
            topics = [topic for chunk in node.chunk_list for topic in chunk.topics]
            if topics:
                node.topic_embeddings = embedding_model.encode(topics)['dense_vecs']
        # Recursively create embeddings for child nodes
        for child in node.children:
            traverse_and_embed(child)
    
    traverse_and_embed(root_node)

def generate_content_summary(content_text, model_name='llama3.2-3B-16k', max_words=30):
    # Summary
    content_text = content_text.strip()
    if (content_text == ""):
        return ""
    summary_prompt = f"Please generate a summary of the following text in triple backticks in no more than {max_words} words. Keep summary clean, no title or header is needed.\n"
    summary = genai_by_llm(content_text, summary_prompt, model_name=model_name)
    return summary

def generate_topics_for_content(content_text, model_name='llama3.2-3B-16k', api_url='http://localhost:11434/api/generate'):
    topics_prompt = "Please generate 1-3 topics for the following text in triple backticks. Each topic consists of a few separated words. Put your topics as a JSON list.\n"
    topics_prompt += f"```{content_text}```"
    response = call_llm_api(topics_prompt, model_name, api_url)
    try:
        topics = json.loads(response)
    except json.JSONDecodeError:
        topics = []
    return topics

def retrieve_relevant_nodes(query, root_node, embedding_model, bm25_model, top_n=10, threshold=0.0):
    time1 = time.time()
    query_embedding = embedding_model.encode([query])['dense_vecs']
    time2 = time.time()
    print("Embedding time = ", time2-time1)
    relevant_nodes = []

    def evaluate_node(node):
        if node.header_embedding is None:
            return
        node_text = f"{node.header} {node.content}"
        score_embedding = calculate_similarity_score(query_embedding, node.content_embeddings, node.header_embedding, node.summary_embedding, node.topic_embeddings)
        score_bm25 = bm25_model.get_score(node_text.split(), query.split())
        score = 0.5 * score_embedding + 0.5 * score_bm25
        if len(node.children) > 0:
            score *= 0.0
        if score >= threshold:
            relevant_nodes.append((node, score))

    def traverse_tree(node):
        evaluate_node(node)
        for child in node.children:
            traverse_tree(child)

    traverse_tree(root_node)
    relevant_nodes = sorted(relevant_nodes, key=lambda x: x[1], reverse=True)
    return [node for node, score in relevant_nodes[:top_n]]

def calculate_similarity_score(query_embedding, content_embeddings, header_embedding, summary_embedding, topic_embeddings=None, weight_header=0.5, weight_summary=0.1, weight_content=0.3, weight_topics=0.1):
    # Calculate cosine similarity between the query and content embeddings using dot product for normalized vectors
    content_similarity = np.dot(query_embedding, content_embeddings.T).max() if content_embeddings is not None else 0
    header_similarity = np.dot(query_embedding, header_embedding.T).max()
    summary_similarity = np.dot(query_embedding, summary_embedding.T).max() if summary_embedding is not None else 0
    topic_similarity = np.dot(query_embedding, topic_embeddings.T).max() if topic_embeddings is not None else 0
    
    # Weighted sum of similarities
    score = (weight_header * header_similarity + 
             weight_summary * summary_similarity + 
             weight_content * content_similarity + 
             weight_topics * topic_similarity)
    return score

def string_tree_node(node, tree_str=""):
    hashes = "##########"
    hash_tag = hashes[:node.level]
    if node.header != "root":
        tree_str += f"{hash_tag} {node.header}\n\n"
    tree_str += f"{node.content}\n\n"
    return tree_str
    
def collect_content_from_nodes(relevant_nodes):
    unique_nodes = []
    def is_descendant(node, ancestor):
        current = node.parent
        while current:
            if current == ancestor:
                return True
            current = current.parent
        return False

    for node in relevant_nodes:
        if not any(is_descendant(node, ancestor) for ancestor in unique_nodes):
            unique_nodes.append(node)
    collected_content = ""
    for node in unique_nodes:
        collected_content += string_tree(node)
    
    return collected_content

def collect_content_from_nodes(relevant_nodes):
    # Collect contents from the node in the original document order
    # First, sort relevant nodes by their node_ids
    sorted_nodes = sorted(relevant_nodes, key=lambda x: x.node_id)
    collected_content = ""
    for node in sorted_nodes:
        collected_content += string_tree_node(node)
    return collected_content

def tree_node_iterator(root_node):
    """
    Iterator function to return all nodes in a document tree in depth-first order.

    Args:
        root_node (Node): The root node of the document tree.

    Returns:
        list: A list of all nodes in depth-first order.
    """
    nodes = []

    def traverse(node):
        nodes.append(node)
        for child in node.children:
            traverse(child)

    traverse(root_node)
    return nodes
    
def collect_content_from_doctree(root, relevant_nodes):
    # Collect contents from the document tree with emphersize on the most relevant nodes 
    # whiel keep a holistic view of the whole document.
    all_nodes = tree_node_iterator(root)
    collected_content = ""
    hashes = "##########"

    # Skip root
    for node in all_nodes[1:]:
        hash_tag = hashes[:node.level]
        collected_content += f"{hash_tag} {node.header}\n\n"
        if (node in relevant_nodes): 
            # Full node content
            collected_content += f"{node.content}\n\n"
        else:
            # Only header + summary
            collected_content  += f"{node.summary}\n\n"
            
    return collected_content
    

def gen_answer(input_text, query, model_name='llama3.2-3B-16k', api_url='http://localhost:11434/api/generate', temperature=0.1, max_tokens=1024):
    """
    Generate an answer based solely on the user query.

    Args:
        query (str): The query for which an answer is required.
        model_name (str): Name of the LLM to be used.
        api_url (str): URL endpoint for the LLM API.
        temperature (float): Sampling temperature for response generation.
        max_tokens (int): Maximum number of tokens to generate.

    Returns:
        str: Generated response text.
    """
    # Answers
    answer_prompt = "Please answer the user query based on the information provided in the following triple backticks:\n"
    prompt = answer_prompt + f"```{input_text}```\n\n"
    prompt += f"Here is the user query in quotes: {query}\n\n"
    prompt += "Keep your response straightforward, no headers, no comments, just the answer based on the above information."
    
    return call_llm_api(prompt, model_name, api_url, temperature, max_tokens)

def call_llm_api(prompt, model_name, api_url, temperature=0.1, max_tokens=1024):
    """
    Helper function to call LLM API and generate text based on the given prompt.

    Args:
        prompt (str): The input prompt for the model.
        model_name (str): Name of the model to be used.
        api_url (str): URL endpoint for the LLM API.
        temperature (float): Sampling temperature for response generation.
        max_tokens (int): Maximum number of tokens to generate.

    Returns:
        str: Generated response text.
    """
    payload = {
        'model': model_name,
        'prompt': prompt,
        'temperature': temperature,
        'max_tokens': max_tokens
    }

    response = requests.post(api_url, json=payload, stream=True)

    generated_text = ''
    if response.status_code == 200:
        for line in response.iter_lines():
            if line:
                data = json.loads(line.decode('utf-8'))
                if 'response' in data:
                    generated_text += data['response']
    else:
        print('Error:', response.status_code, response.text)

    return generated_text

def genai_by_llm(input_text, prompt_template, model_name='llama3.2-3B-16k', api_url='http://localhost:11434/api/generate', temperature=0.1, max_tokens=512):
    """
    Helper function to call LLM API with a specific prompt template for generating summaries or topics.

    Args:
        input_text (str): The input text to be used for generation.
        prompt_template (str): The prompt template to be used.
        model_name (str): Name of the model to be used.
        api_url (str): URL endpoint for the LLM API.
        temperature (float): Sampling temperature for response generation.
        max_tokens (int): Maximum number of tokens to generate.

    Returns:
        str: Generated response text.
    """
    prompt = prompt_template + f"```{input_text}```"
    return call_llm_api(prompt, model_name, api_url, temperature, max_tokens)

class QnAAgent:
    def __init__(self, markdown_text, embedding_model_path='../bge-m3.model'):
        self.tree = parse_markdown_to_tree(markdown_text)
        self.embedding_model = load_embedding_model(embedding_model_path)
        self.bm25_model = BM25([f"{node.header} {node.content}".split() for node in tree_node_iterator(self.tree)])
        create_embeddings_for_tree(self.tree, self.embedding_model)

    def answer_question(self, query, top_n=5, model_name='llama3.2-3B-16k',show_content=False):
        time1 = time.time()
        relevant_nodes = retrieve_relevant_nodes(query, self.tree, self.embedding_model, self.bm25_model, top_n=top_n)
        #collected_content = collect_content_from_nodes(relevant_nodes)
        collected_content = collect_content_from_doctree(self.tree, relevant_nodes)
        time2 = time.time()
        print("Retrieval time = ", time2-time1)
        if show_content:
            print("collected_content: ",collected_content)
        answer = gen_answer(collected_content, query, model_name=model_name)
        return answer

