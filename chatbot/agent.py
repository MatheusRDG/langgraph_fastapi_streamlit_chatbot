# from langchain.agents import Tool, create_react_agent
# from langchain.memory import ChatMessageHistory
# from langchain_core.runnables.history import RunnableWithMessageHistory
# from langchain.agents import AgentExecutor, create_react_agent
# from langchain_openai import OpenAI



# memory = ChatMessageHistory(session_id="test-session")

# # Create the agent
# memory = MemorySaver()
# model = ChatOpenAI(model_name="gpt-4o-mini", temperature=0)
# agent_executor = create_react_agent(model, tools, checkpointer=memory)

# # Use the agent
# config = {"configurable": {"thread_id": "abc123"}}
# for chunk in agent_executor.stream(
#     {
#         "messages": [
#             HumanMessage(content="Give me the actual hour and the sum of 2 and 3")
#         ]
#     },
#     config,
# ):
#     print(chunk)
#     print("----")

# # llm = OpenAI(temperature=0)
# # agent = create_react_agent(llm, tools, prompt)
# # agent_executor = AgentExecutor(agent=agent, tools=tools)

# # agent_with_chat_history = RunnableWithMessageHistory(
# #     agent_executor,
# #     # This is needed because in most real world scenarios, a session id is needed
# #     # It isn't really used here because we are using a simple in memory ChatMessageHistory
# #     lambda session_id: memory,
# #     input_messages_key="input",
# #     history_messages_key="chat_history",
# # )