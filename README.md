# 🧠 LangGraph Chatbot

A conversational AI chatbot built using **LangGraph**, **LangChain**, and **Streamlit** with **Groq’s Gemma2-9B model**.  
This project supports **multi-turn conversations**, **thread management**, and **persistent chat history** with SQLite checkpoints.  

---

## 🚀 Features  

- ✅ **Real-time Chat** – Interactive chatbot with live streaming responses.  
- ✅ **LangGraph Integration** – Graph-based conversation flow with state management.  
- ✅ **Thread Management** – Create, reset, and switch between multiple chat threads.  
- ✅ **Conversation History** – Save and retrieve past chats using SQLite checkpoints.  
- ✅ **Streamlit UI** – User-friendly interface with sidebar navigation for chats.  

---

## 🛠️ Tech Stack  

- **[LangGraph](https://github.com/langchain-ai/langgraph)** – State management and graph-based conversation flow.  
- **[LangChain](https://www.langchain.com/)** – Message handling and LLM integration.  
- **[Groq API](https://groq.com/)** – High-performance inference with Gemma2-9B model.  
- **[Streamlit](https://streamlit.io/)** – Web-based frontend for chatbot interaction.  
- **SQLite** – Checkpointing and conversation persistence.  

---

## 📂 Project Structure  

```
├── langgraph_backend.py   # Backend logic with LangGraph & Groq LLM
├── streamlit_frontend.py  # Streamlit-based chatbot UI
├── chatboat.db            # SQLite database (auto-generated for chat history)
└── README.md              # Project documentation
```

---

## ⚡ Setup Instructions  

### 1️⃣ Clone the Repository  
```bash
git clone https://github.com/your-username/langgraph-chatbot.git
cd langgraph-chatbot
```

### 2️⃣ Create a Virtual Environment  
```bash
python -m venv venv
source venv/bin/activate   # On Mac/Linux
venv\Scripts\activate      # On Windows
```

### 3️⃣ Install Dependencies  
```bash
pip install -r requirements.txt
```

*(Make sure `streamlit`, `langchain`, `langgraph`, and `langchain-groq` are included in `requirements.txt`.)*  

### 4️⃣ Add Your Groq API Key  
Inside `langgraph_backend.py`, replace the API key with your own:  
```python
llm = ChatGroq(api_key="YOUR_API_KEY", model_name="gemma2-9b-it")
```

### 5️⃣ Run the Chatbot  
```bash
streamlit run streamlit_frontend.py
```

---

## 💻 Usage  

- Open the **Streamlit app** in your browser.  
- Start chatting with the AI model.  
- Use **sidebar controls** to create new chats or revisit previous conversations.  
- All conversations are stored in **SQLite (chatboat.db)** automatically.  

---

## 📸 Demo Screenshot  

(Add a screenshot here after running your chatbot UI)  

---

## 🔮 Future Improvements  

- Add support for multiple LLM providers (e.g., OpenAI, Together AI).  
- Enhance UI with chat avatars and markdown rendering.  
- Implement user authentication for personalized chat histories.  
- Deploy on **Streamlit Cloud / Hugging Face Spaces**.  

---

## 🤝 Contributing  

Contributions, issues, and feature requests are welcome!  
Feel free to fork this repo and submit a PR.  

---

## 📜 License  

This project is licensed under the **MIT License** – see the [LICENSE](LICENSE) file for details.  
