from langchain_groq import ChatGroq
import os 
from dotenv import load_dotenv

class GroqLLM:
    def __init__(self):
        load_dotenv()


    def get_llm(self):
        try:
            print(os.getenv("GROQ_API_KEY"))
            os.environ["GROQ_API_KEY"]=self.groq_api_key=os.getenv("GROQ_API_KEY")
            llm=ChatGroq(model="qwen/qwen3-32b",temperature=0,api_key=self.groq_api_key)
            #llm=ChatGroq(api_key=self.groq_api_key,model="llama-3.1-8b-instant")
            return llm
        except Exception as e:
            raise ValueError("Error occurred with exception : {e}")