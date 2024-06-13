from openai import OpenAI
import streamlit as st
import base64
from pdf2image import convert_from_path
import os

OAI_MODEL = 'gpt-4o'
model_names = {"gpt-4": "GPT-4", "gpt-4o": "GPT-4o"}

# Open the image file and encode it as a base64 string
def encode_image(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode("utf-8")
    
st.title(f"Chatbot using Streamlit")
st.subheader(f"Conversations with {model_names[OAI_MODEL]}")

api_key = os.getenv("OPENAI_API_KEY")
client = OpenAI(api_key=api_key)

# Toolbar on the left side
st.sidebar.title("Toolbar")

uploaded_file = st.sidebar.file_uploader("Upload a PDF file", type="pdf")
WORK_DIR = "work"

# Placeholder for additional action buttons
if st.sidebar.button("Action 1"):
    st.sidebar.write("Action 1 button clicked")
if st.sidebar.button("Action 2"):
    st.sidebar.write("Action 2 button clicked")

if "openai_model" not in st.session_state:
    st.session_state["openai_model"] = OAI_MODEL

if "messages" not in st.session_state:
    st.session_state.messages = []

# Refresh with historical messages first
for message in st.session_state.messages:
    # Set role context and then show the message for the role
    with st.chat_message(message["role"]):
        st.markdown(message["content"])   

if prompt := st.chat_input("What is up?"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        message_placeholder = st.empty()
        full_response = ""
        for response in client.chat.completions.create(
            model=st.session_state["openai_model"],
            messages=[
                {"role": m["role"], "content": m["content"]}
                for m in st.session_state.messages
            ],
            stream=True,
        ):
            print("response:",(response.choices[0].delta.content or ""))
            full_response += (response.choices[0].delta.content or "")
            message_placeholder.markdown(full_response + "▌")
        # Refresh the display with out the cursor "▌"
        message_placeholder.markdown(full_response)
    st.session_state.messages.append({"role": "assistant", "content": full_response})

if uploaded_file:
    pdf_id = uploaded_file.name.split(".")[0]
    pdf_file = f"{WORK_DIR}/{pdf_id}.pdf"
    print("Read PDF file")
    with open(pdf_file, "wb") as f:
        f.write(uploaded_file.getbuffer())

    # Store Pdf with convert_from_path function
    images = convert_from_path(pdf_file)

    base64_images = []
    user_contents = []

    for i, image in enumerate(images):
        image_path = "tmp_image.jpeg"
        image.save(image_path, "JPEG")
        print(f"Page {i+1} saved as image: {image_path}")
        base64_image = encode_image(image_path)
        base64_images.append(base64_image)
        item = [{"type": "text", "text": f"This is page {i+1}"},
                {"type": "image_url", "image_url": {
                    "url": f"data:image/png;base64,{base64_image}"}
                }]
        user_contents += item

    system_prompt = """
    You are an exppert to read text from images. I will provide a group of images, each image is a page of a PDF file. 
    Give me the markdown text output from these pages, match the structure of the pages as close as you can get. Only output the markdown 
    and nothing else. Do not explain the output, just return it. Do not use a single # for a heading. All headings will start with ## or ### and so on.
    Convert tables to markdown tables. Describe charts as best you can. DO NOT return in a codeblock. Just return the raw text in markdown format.
    """
    response = client.chat.completions.create(
        model=OAI_MODEL,
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_contents}
        ],
        max_tokens=4096,
        temperature=0.0,
    )
    #st.session_state.messages.append({"role": "system", "content": system_prompt})
    #st.session_state.messages.append({"role": "user", "content": user_contents})
    md_text = response.choices[0].message.content
    print("Finish reason",response.choices[0].finish_reason)
    md_text = md_text.replace('$', '\\\\\\$')
    message_placeholder = st.empty()
    message_placeholder.markdown(md_text)
    st.session_state.messages.append({"role": "assistant", "content": md_text})

    while (response.choices[0].finish_reason == 'length'):
        response = client.chat.completions.create(
            model=OAI_MODEL,
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_contents},
                {"role": "user", "content": "This the the markdown generated from the PDF so far"},
                {"role": "assistant", "content": md_text},
                {"role": "user", "content": "please complete the markdown the remaining"},
            ],
            max_tokens=4096,
            temperature=0.0,
        )
        md_text2 = response.choices[0].message.content
        print("Finish reason",response.choices[0].finish_reason)
        md_text = md_text + md_text2.replace('$', '\\\\\\$')
        message_placeholder.markdown(md_text)
    md_file = f"{WORK_DIR}/{pdf_id}.md"
    print("write markdown file")
    with open(md_file, "w") as f:
        f.write(md_text)
      
    # for i in range(len(images)):
    #     # Save pages as images in the pdf
    #     images[i].save('page'+ str(i) +'.png', 'PNG')
    #     IMAGE_PATH = 'page'+ str(i) +'.png'
    #     base64_image = encode_image(IMAGE_PATH)
    #     response = client.chat.completions.create(
    #         model=st.session_state["openai_model"],
    #         messages=[
    #             {"role": "system", "content": "You are an expert to read documents"},
    #             {"role": "user", "content": [
    #                 {"type": "text", "text": "Extract text from the image and put the text in markdown format"},
    #                 {"type": "image_url", "image_url": {
    #                     "url": f"data:image/png;base64,{base64_image}"}
    #                 }
    #             ]}
    #         ],
    #         temperature=0.0,
    #     )
    #     #print(response.choices[0].message.content)
    #     with st.chat_message('system'):
    #         msg = response.choices[0].message.content
    #         msg = msg.replace("```markdown","")
    #         msg = msg.replace("```MARKDOWN","")
    #         msg = msg.replace("```","")
    #         st.markdown(msg)
    #         print("From PDF")
    #         print(msg)
    #         st.session_state.messages.append({"role": "user", "content": msg})
    #     if (i > 0):
    #         break

