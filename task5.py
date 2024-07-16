import streamlit as st
from streamlit_pdf_viewer import pdf_viewer
import pdfplumber
import io
from transformers import AutoTokenizer, TFAutoModelForSeq2SeqLM



div_style = """
background-color: #FFFFFF;
padding-top: 1rem;
border-radius: 15px;
padding-bottom: 1rem;
padding-left: 1rem;
padding-right: 1rem;
width: 100%
</style>
"""

st.header(":blue[Text Analytics using NLP] ",divider='blue')


tokenizer = AutoTokenizer.from_pretrained("facebook/bart-large-cnn")
model = TFAutoModelForSeq2SeqLM.from_pretrained("facebook/bart-large-cnn")
col1,col2 = st.columns([1,1])
with col1:
    pdf_file = st.file_uploader(":grey[Upload PDF file]", type=('pdf'))
    if not pdf_file:
        st.write("<h6 style='text-align: center;'>------Or------</h6>", unsafe_allow_html=True)
        text = st.text_input("Enter the text you want to summarize")


    def extract_text_from_pdf(pdf_file):
        with pdfplumber.open(pdf_file) as pdf:
            all_text = ""
            for page in pdf.pages:
                text = page.extract_text()
                all_text += text + "\n"
        return all_text


    if pdf_file :
        # To read file as bytes:
        bytes_data = pdf_file.getvalue()

        # Create a BytesIO object
        pdf_file = io.BytesIO(bytes_data)

        # Extract text from the PDF
        text = extract_text_from_pdf(pdf_file)


    if pdf_file or text:
        inputs = tokenizer("summarize: " + text, return_tensors="tf", max_length=1024, truncation=True)

        # Extract input_ids from tokenizers.Encoding object
        input_ids = inputs["input_ids"]

        # Generate summary using the model
        
        summary_ids = model.generate(input_ids, max_length=512, min_length=100, length_penalty=2.0, num_beams=4, early_stopping=True)
        summary_ids = summary_ids.numpy()[0]
        mask = summary_ids == 50249
        summary_ids[mask] = 0
        summary = tokenizer.decode(summary_ids, skip_special_tokens=True)

        html_content = f"""
        <div style="{div_style}">
            <p><strong>Summary : </strong>{summary}</p>
        </div>
        """

        st.write(html_content, unsafe_allow_html=True)

with col2:
    with col2:
        if pdf_file:
            binary_data = pdf_file.getvalue()
            pdf_viewer(input=binary_data,
                        width=400,
                        pages_to_render=[1])