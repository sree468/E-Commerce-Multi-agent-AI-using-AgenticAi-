import os
from dotenv import load_dotenv

# Load variables from .env
load_dotenv()

# Gemini API Key
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

# Gemini model
GEMINI_MODEL = os.getenv(
    "GEMINI_MODEL",
    "gemini-3.8-flash"
)

# SQLite database
DATABASE_URL = os.getenv(
    "DATABASE_URL",
    "sqlite:///./data/ecommerce.db"
)

# Check API key
if not GEMINI_API_KEY:
    raise ValueError(
        "GEMINI_API_KEY is missing. "
        "Please add GEMINI_API_KEY to your .env file."
    )