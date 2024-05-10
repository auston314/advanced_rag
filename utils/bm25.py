import math
from collections import Counter
from typing import List

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
            print("Frequences = ",frequencies)
            
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


if __name__ == "__main__":
    # Example usage
    docs = [["the", "quick", "brown", "fox"], ["jumped", "over", "the", "lazy", "dog"], ["the","crazy","fox","was","jumping","around", "the", "dog"]]
    bm25 = BM25(docs)
    query = ["the","quick", "fox"]
    scores = bm25.get_scores(query)
    print(scores)
