from dotenv import load_dotenv
load_dotenv() #load env variable

import streamlit as st
import os
import google.generativeai as genai
from PIL import Image

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# function to generate response from gemini pro model
model=genai.GenerativeModel("gemini-pro-vision")
def get_gemini_response(input,image,prompt):
    response = model.generate_content([input,image[0],prompt])
    return response.text

def input_image_setup(uploaded_file):
    # Check if a file has been uploaded
    if uploaded_file is not None:
        # Read the file into bytes
        bytes_data = uploaded_file.getvalue()

        image_parts = [
            {
                "mime_type": uploaded_file.type,  # Get the mime type of the uploaded file
                "data": bytes_data
            }
        ]
        return image_parts
    else:
        raise FileNotFoundError("No file uploaded")

st.set_page_config(page_title="Gemini Image Demo")
st.header("Gemini LLM Application")
input=st.text_input("Input: ",key="input")
uploaded_file=st.file_uploader("Choose an image...",type=["jpeg","jpg","png"])

image=""
if uploaded_file is not None:
    image=Image.open(uploaded_file)
    st.image(image,caption="Uploaded image", use_column_width=True)

submit = st.button("Tell me about Image")

input_prompt = """
               You are an expert in understanding invoices.
               You will receive input images as invoices &
               you will have to answer questions based on the input image
               """

if submit:
    image_data = input_image_setup(uploaded_file)
    response = get_gemini_response(input_prompt,image_data, input)
    st.subheader("The resposne is")
    st.write(response)






