import streamlit as st
import os
from dotenv import load_dotenv
from langgraph_backend import chatbot, retrive_thread
from langchain_core.messages import HumanMessage, AIMessage
import uuid

# Load environment variables
load_dotenv()

# --------------------------------------------------------------------------------
# Helper functions

def generate_thread_id():
    return str(uuid.uuid4())

def reset_chat():
    thread_id = generate_thread_id()
    st.session_state['thread_id'] = thread_id
    add_thread(thread_id)
    st.session_state['message_history'] = []

def add_thread(thread_id):
    if thread_id not in st.session_state['chat_thread']:
        st.session_state['chat_thread'].append(thread_id)

def load_conversation(thread_id):
    return chatbot.get_state(config={'configurable': {'thread_id': thread_id}}).values['messages']

# --------------------------------------------------------------------------------
# Streamlit UI setup

st.set_page_config(page_title="LangGraph Chatbot", page_icon="🤖", layout="wide")

st.title("🤖 LangGraph Chatbot")

# Initialize session state
if 'message_history' not in st.session_state:
    st.session_state['message_history'] = []

if 'thread_id' not in st.session_state:
    st.session_state['thread_id'] = generate_thread_id()

if 'chat_thread' not in st.session_state:
    st.session_state['chat_thread'] = retrive_thread()

add_thread(st.session_state['thread_id'])

# Sidebar
st.sidebar.title("💬 Chat Manager")
if st.sidebar.button("New Chat"):
    reset_chat()

st.sidebar.header("Saved Conversations")
for thread_id in st.session_state['chat_thread'][::-1]:
    if st.sidebar.button(str(thread_id)):
        st.session_state['thread_id'] = thread_id
        messages = load_conversation(thread_id)
        st.session_state['message_history'] = [
            {"role": "user" if isinstance(m, HumanMessage) else "assistant", "content": m.content}
            for m in messages
        ]

# --------------------------------------------------------------------------------
# Chat Interface

for message in st.session_state['message_history']:
    with st.chat_message(message['role']):
        st.markdown(message['content'])

user_input = st.chat_input("Type your message...")

if user_input:
    st.session_state['message_history'].append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.markdown(user_input)

    CONFIG = {
        'configurable': {'thread_id': st.session_state['thread_id']},
        'metadata': {'thread_id': st.session_state['thread_id']},
        'run_name': 'chat_turn'
    }

    with st.chat_message("assistant"):
        def ai_stream():
            for message_chunk, metadata in chatbot.stream(
                {'messages': [HumanMessage(content=user_input)]},
                config=CONFIG,
                stream_mode='messages'
            ):
                if isinstance(message_chunk, AIMessage):
                    yield message_chunk.content
        ai_message = st.write_stream(ai_stream())

    st.session_state['message_history'].append({"role": "assistant", "content": ai_message})
