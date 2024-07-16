import streamlit as st
from streamlit_pdf_viewer import pdf_viewer
from pypdf import PdfReader
import google.generativeai as genai
from api import api


div_style = """
background-color: #FFFFFF;
padding-top: 5rem;
border-radius: 15px;
padding-bottom: 5rem;
padding-left: 5rem;
padding-right: 5rem;
width: 100%
</style>
"""



st.header(":blue[QNA using LLMs] ",divider='blue')

col1,col2 =st.columns([1,1])



with col1:
    pdf_file = st.file_uploader(":grey[Upload PDF file]", type=('pdf'))

    if pdf_file:
        question = st.text_area("Enter your question")

with col2:
    if pdf_file:
        binary_data = pdf_file.getvalue()
        pdf_viewer(input=binary_data,
                    width=400,
                    pages_to_render=[1])

if pdf_file and question :
    reader = PdfReader(pdf_file)
    print(len(reader.pages)) 
    page = reader.pages[0] 
    context = page.extract_text()

    genai.configure(api_key=api['key'])
    model=genai.GenerativeModel('gemini-1.5-flash')
    response=model.generate_content(f""" context:{context} + "\nQuestion: " + {question} + "\nAnswer:"
        you are an expert in the context provided to you, you will be asked a question if question is relevant to the context answer only using the knowledge from the context , if not relevant of not enough information say not enough information, you should not add any information or suggetions from your side """)
    
    response = response.text
    
    html_content = f"""
    <div style="{div_style}">
        <p><strong>Question:</strong> {question}</p>
        <p><strong>Answer:</strong> {response}</p>
    </div>
    """

    st.write(html_content, unsafe_allow_html=True)
