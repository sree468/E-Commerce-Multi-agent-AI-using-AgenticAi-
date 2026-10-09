from langchain_google_genai import ChatGoogleGenerativeAI

from app.config import GEMINI_API_KEY, GEMINI_MODEL


llm = ChatGoogleGenerativeAI(
    model=GEMINI_MODEL,
    google_api_key=GEMINI_API_KEY,
    temperature=0.1,
    max_retries=2,
    timeout=120
)