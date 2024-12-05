import os

import streamlit as st
from dotenv import load_dotenv
from langchain_core.messages import AIMessage, HumanMessage

# from langchain_core.output_parsers import StrOutputParser
# from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage
from langgraph.checkpoint.memory import MemorySaver
from langgraph.prebuilt import create_react_agent
from api_tools import read_root, create_message, read_messages, read_message
from uuid import uuid4
from langgraph.prebuilt import create_react_agent


load_dotenv()

# app config
st.set_page_config(page_title="Streamlit Chatbot", page_icon="🤖")
st.title("Chatbot")

initial_message = """
Hello, i'll assist you with the tools!
You can ask me about the tools for read_root, create_message, read_messages, and read_message.
"""

# session state
if "chat_history" not in st.session_state:
    st.session_state.chat_history = [
        AIMessage(content=initial_message),
    ]

if "model" not in st.session_state:
    st.session_state.model = "gpt-4o-mini"

if "thread_id" not in st.session_state:
    st.session_state.thread_id = str(uuid4())

# chatbot

template = """
Assist the user to use the api calls tools for read_root, create_message, read_messages, and read_message.
If have some missing information to use the tool, ask the user.
If the user talk about other topic, move the user to your objective - help with api calls.
If the message dont need to use tools, dont use, only answer.
return the response of the tools to the user in a good format.

User Input:
{user_input}
"""

memory = MemorySaver()
llm = ChatOpenAI(model_name="gpt-4o-mini", temperature=0)
tools = [read_root, create_message, read_messages, read_message]
agent_executor = create_react_agent(llm, tools, checkpointer=memory)


def get_response(user_query):

    config = {
        "configurable": {
            "session_id": st.session_state.thread_id,
            "thread_id": st.session_state.thread_id,
        }
    }

    user_query = template.format(user_input=user_query)
    response = agent_executor.invoke(
        {
            "messages": [HumanMessage(content=user_query)],
        },
        config,
    )

    print(response)

    return response["messages"][-1].content


# conversation
for message in st.session_state.chat_history:
    if isinstance(message, AIMessage):
        with st.chat_message("AI"):
            st.write(message.content)
    elif isinstance(message, HumanMessage):
        with st.chat_message("Human"):
            st.write(message.content)

# user input
user_query = st.chat_input("Type your message here...")
if user_query is not None and user_query != "":
    st.session_state.chat_history.append(HumanMessage(content=user_query))

    with st.chat_message("Human"):
        st.markdown(user_query)

    with st.chat_message("AI"):
        response = get_response(user_query)  # convert to stream
        st.write(response)

    st.session_state.chat_history.append(AIMessage(content=response))

# if __name__ == "__main__":
#     user_query = input("Type your message here: ")
#     while user_query != "q":
#         print(get_response(user_query))
#         user_query = input("Type your message here: ")
