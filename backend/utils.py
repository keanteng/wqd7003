import google.generativeai as genai
import pandas as pd

def authenticate_gemini(api_key):
    try:
        genai.configure(api_key=api_key)
        ai_model = genai.GenerativeModel("gemini-1.5-flash")
        test = ai_model.generate_content("Explain how AI works")
        return True
    except Exception as e:
        return False
    
def load_data(path):
    return pd.read_csv(path)