GitHub readme 


# 💬 Insta-Style AI Chatbot with Memory (Gemini + Streamlit)

Welcome to your personal AI-powered direct message experience! This is a memory-enabled chatbot powered by **Gemini API** and styled like **Instagram DMs**, built with 🧠 + ❤️ in Python using **Streamlit**. It remembers what you said—even after you leave!


## 🚀 Features

- 🤖 Conversational AI powered by **Gemini-2.0-flash**
- 🧠 Persistent memory using JSON files for:
  - Chat History
  - User-specific memory
- 🎨 **Instagram-inspired** DM layout with styled bubbles
- 🔘 UI controls:
  - "Clear Memory" button to reset everything
  - Chat history auto-persistence
- 💬 Streamlit chat interface with bubble styling:
  - User messages on the right
  - Bot messages on the left

---

## 🛠️ Tech Stack

- **Python**
- **Streamlit** for UI
- **Google Generative AI API (Gemini)**
- **JSON** for persistent memory storage

---

## 📦 Installation

1. **Clone the repository**:

```bash
git clone https://github.com/yourusername/insta-gemini-chatbot.git
cd insta-gemini-chatbot
```

2. **Install the required dependencies**:

```bash
pip install -r requirements.txt
```

3. **Set up your Gemini API Key**:

In your main script, configure the API like this:

```python
genai.configure(api_key="YOUR_GEMINI_API_KEY")
```

> 💡 **Best practice**: Store the key in an environment variable for security.

4. **Run the Streamlit App**:

```bash
streamlit run app.py
```

---

## 📁 Project Structure

```
📦 insta-gemini-chatbot/
├── app.py                  # Main Streamlit app
├── chat_memory.json        # Persistent chat history
├── user_memory.json        # Persistent user info
├── README.md               # This file 😎
└── requirements.txt        # Python dependencies
```

---

## 🧹 Memory Management

- `chat_memory.json` stores full user-bot chat logs.
- `user_memory.json` stores structured memory (like names, preferences, etc.).
- Clicking **🧹 Clear Memory** wipes both files and resets the session state.

---

## 🧪 Customization Ideas

- 🔐 Add user authentication (memory per user)
- 🎨 Enhance layout with emojis, GIFs, or media sharing
- 💾 Use SQLite or MongoDB for large-scale memory
- 🌓 Dark/light mode toggle like Instagram

---

## ⚠️ Disclaimer

This app uses the **Google Gemini API**. Be aware of:

- API limits and quota costs
- Responsible AI usage guidelines
- Data privacy considerations

---

