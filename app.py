import streamlit as st
import google.generativeai as genai
import json
import os

# --- Configure Gemini ---
genai.configure(api_key="Your_Api_Key_Here")  # Replace with your actual API key
model = genai.GenerativeModel("gemini-2.0-flash")  #You can swap to gemini-pro if needed


# --- Title and Layout ---
st.set_page_config(page_title="Gemini Chat DM", page_icon="💬")
st.title("💬 Insta-Style Chatbot")
st.caption("I can remember what you say because am AI not you GF😉")




# --- Memory Files Setup ---
MEMORY_FILE = "chat_memory.json"
USER_MEMORY_FILE = "user_memory.json"

def load_chat_memory():
    if os.path.exists(MEMORY_FILE):
        with open(MEMORY_FILE, "r") as f:
            return json.load(f)
    return []

def save_chat_memory(messages):
    with open(MEMORY_FILE, "w") as f:
        json.dump(messages, f)

def load_user_memory():
    if os.path.exists(USER_MEMORY_FILE):
        with open(USER_MEMORY_FILE, "r") as f:
            return json.load(f)
    return {}

def save_user_memory(memory):
    with open(USER_MEMORY_FILE, "w") as f:
        json.dump(memory, f)

# --- Initialize Session State ---
if "chat_messages" not in st.session_state:
    st.session_state.chat_messages = load_chat_memory()

if "user_memory" not in st.session_state:
    st.session_state.user_memory = load_user_memory()


# --- Control Panel ---
col1, col2 = st.columns(2)
with col1:
    if st.button("🧹 Clear Memory"):
        st.session_state.chat_messages = []
        st.session_state.user_memory = {}  # clear user memory too
        save_chat_memory([])  # clear chat history file
        save_user_memory({})  # clear structured memory file
        st.success("Memory wiped clean. All fresh now.")

# --- Display Chat History ---
for msg in st.session_state.chat_messages:
    with st.chat_message(msg["role"], avatar="👤" if msg["role"] == "user" else "🤖"):
        st.markdown(msg["content"])

# --- Chat Input ---
user_input = st.chat_input("DM your AI homie...")

if user_input:
    # Show & save user message
    st.chat_message("user", avatar="👤").markdown(user_input)
    st.session_state.chat_messages.append({"role": "user", "content": user_input})
    save_chat_memory(st.session_state.chat_messages)

    # Build conversation for Gemini
    convo = "\n".join(
        [f"{m['role'].capitalize()}: {m['content']}" for m in st.session_state.chat_messages]
    )

    prompt = f"""
You're a friendly and memory-aware AI assistant. Continue the conversation with relevant, helpful replies.
Here's the chat so far:
{convo}

Respond to the latest user input: "{user_input}"
"""

    # Get response from Gemini
    response = model.generate_content(prompt)
    reply = response.text.strip()

    # Show & save Gemini reply
    with st.chat_message("assistant", avatar="🤖"):
        st.markdown(reply)

    st.session_state.chat_messages.append({"role": "assistant", "content": reply})
    save_chat_memory(st.session_state.chat_messages)

# --- Structured Memory Example ---
if "name" not in st.session_state.user_memory:
    st.session_state.user_memory["name"] = st.text_input("What's your name?", "Saad")
    save_user_memory(st.session_state.user_memory)
