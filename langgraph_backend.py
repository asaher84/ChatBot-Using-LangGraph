from langgraph.graph import StateGraph, START, END
from typing import TypedDict, Annotated
from langchain_groq import ChatGroq
from langchain_core.messages import BaseMessage
from langgraph.checkpoint.sqlite import SqliteSaver
from langgraph.graph.message import add_messages
import sqlite3

# *************************************************************************************************

llm = ChatGroq(api_key="",
               model_name='gemma2-9b-it')  # type:ignore

# meta-llama/llama-4-scout-17b-16e-instruct

# ************************************************************************************************


class ChatState(TypedDict):

    messages: Annotated[list[BaseMessage], add_messages]

# ***********************************************************************************************


def chat_node(State: ChatState):

    # take user query
    messages = State['messages']

    # send to llm
    response = llm.invoke(messages)

    # response store state
    return {'messages': [response]}

# *********************************************************************************************


conn = sqlite3.connect(database='chatboat.db', check_same_thread=False)
checkpointer = SqliteSaver(conn=conn)

# ***********************************************************************************************

graph = StateGraph(ChatState)

graph.add_node('chat_node', chat_node)

graph.add_edge(START,  'chat_node')
graph.add_edge('chat_node', END)

chatbot = graph.compile(checkpointer=checkpointer)

# **********************************************************************************


def retrive_thread():
    all_threads = set()
    for checkpoints in checkpointer.list(None):
        all_threads.add(checkpoints.config['configurable']['thread_id'])
    return list(all_threads)

