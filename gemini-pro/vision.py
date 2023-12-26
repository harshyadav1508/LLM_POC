from dotenv import load_dotenv
load_dotenv() #load env variable

import streamlit as st
import os
import google.generativeai as genai
from PIL import Image

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# function to generate response from gemini pro model
model=genai.GenerativeModel("gemini-pro-vision")
def get_gemini_response(input,image):
    if input!="":
        response = model.generate_content([input,image])
    else:
        response = model.generate_content(image)
    return response.text

st.set_page_config(page_title="Gemini Image Demo")
st.header("Gemini LLM Application")
input=st.text_input("Input: ",key="input")
upload_file=st.file_uploader("Choose an image...",type=["jpeg","jpg","png"])

image=""
if upload_file is not None:
    image=Image.open(upload_file)
    st.image(image,caption="Uploaded image", use_column_width=True)

submit = st.button("Ask me any question related to Image")

if submit:
    response = get_gemini_response(input,image)
    st.subheader("The resposne is")
    st.write(response)






