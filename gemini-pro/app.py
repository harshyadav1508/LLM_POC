import google.generativeai as genai
from dotenv import load_dotenv
load_dotenv() #load env variable
import os
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

model = genai.GenerativeModel('gemini-pro')
resp= model.generate_content("tell me a joke on engineer")
print(resp)
print(type(genai))
print(resp.text)





