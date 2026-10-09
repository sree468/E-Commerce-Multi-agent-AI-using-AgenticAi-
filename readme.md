# 🛒 E-Commerce Multi-Agent AI Assistant

An AI-powered e-commerce assistant built using Python, LangGraph, Gemini, SQLAlchemy, and Streamlit. It helps users track orders, search products, and handle customer support requests through a multi-agent workflow.

## 🚀 Features

* **Order Tracking:** Check order status, delivery status, and payment status.
* **Product Search:** Search for products and view prices, stock, and ratings.
* **Customer Support:** Handle customer issues and support requests.
* **Return & Cancellation:** Process requests through validation and escalation workflows.
* **Refund Handling:** Flag refund requests for human approval.
* **Multi-Agent Workflow:** Coordinate specialized agents using LangGraph.
* **Audit Logging:** Record agent activities and workflow events.
* **Interactive UI:** Chat with the assistant through Streamlit.

## 🛠️ Technologies Used

* Python
* LangGraph
* LangChain
* Google Gemini API
* Streamlit
* SQLAlchemy
* SQLite
* FastAPI
* Pydantic

## 📁 Project Structure

```text
ecommerce_multi_agent/
├── app/
│   ├── agents/
│   ├── database/
│   ├── services/
│   ├── config.py
│   ├── graph.py
│   ├── llm.py
│   ├── main.py
│   ├── schemas.py
│   └── state.py
├── api/
├── ui/
│   └── streamlit_app.py
├── data/
├── tests/
├── .env.example
├── .gitignore
├── requirements.txt
├── README.md
└── run.py
```

## ⚙️ Installation and Setup

### 1. Clone the repository

```bash
git clone <your-github-repository-url>
cd ecommerce_multi_agent
```

### 2. Create a virtual environment

```bash
python -m venv venv
```

Activate it on Windows:

```bash
venv\Scripts\activate
```

### 3. Install dependencies

```bash
python -m pip install -r requirements.txt
```

### 4. Configure environment variables

Create a `.env` file in the project root:

```env
GEMINI_API_KEY=your_gemini_api_key
GEMINI_MODEL=gemini-2.5-flash
DATABASE_URL=sqlite:///./data/ecommerce.db
```

Replace `your_gemini_api_key` with your actual API key.

**Security:** Never upload your `.env` file or API key to GitHub.

### 5. Initialize the database

```bash
python run.py
```

### 6. Start the application

```bash
streamlit run ui/streamlit_app.py
```

Open the local URL displayed in your terminal.

## 🤖 How It Works

1. The user submits a question through the Streamlit interface.
2. The Supervisor Agent identifies the request type.
3. The Retrieval Agent fetches relevant information from the database.
4. The Analysis Agent prepares a response using the available information.
5. The Validation Agent checks whether the request can proceed.
6. The Action Agent handles permitted workflow actions, while the Escalation Agent handles requests requiring additional review.
7. The final response is displayed to the user.

## 💬 Example Questions

* Where is my order?
* What is the status of order 1001?
* Do you have iPhone 16?
* What is the price of Samsung Galaxy S25?
* Show me available laptops.
* I want to return my order.
* I want to cancel my order.
* I need a refund.
* I have a problem with my order.

The questions the application can answer depend on the implemented retrieval logic and available database records.

## 🔮 Future Improvements

* Improve natural-language intent detection
* Add a RAG-based product and policy knowledge base.
* Implement persistent workflow checkpoints.
* Add authentication and authorization.
* Improve human approval workflows.
* Add automated testing and agent evaluation.
* Integrate monitoring and tracing.

## 👨‍💻 Author

**Sreekanth Kurakula**

Data Science | Machine Learning | Generative AI | Agentic AI
