# from dotenv import load_dotenv
# from agents import Agent,Runner,  OpenAIChatCompletionsModel, AsyncOpenAI,function_tool
# from agents.run import RunConfig 
# import os
# import  chainlit as cl

# load_dotenv()
 
# gemini_api_key = os.getenv("GEMINI_API_KEY")
 
# if not gemini_api_key:
#      raise ValueError("GEMINI_API_KEY environment variable is not set.")
#  #Reference: https://ai.google.dev/gemini-api/docs/openai
# external_client = AsyncOpenAI(
#      api_key=gemini_api_key,
#      base_url="https://generativelanguage.googleapis.com/v1beta",
#  )

# model = OpenAIChatCompletionsModel(
#      model="gemini-2.0-flash",
#      openai_client=external_client
#  )

# config = RunConfig(
#      model=model,
#      model_provider=external_client,
#      tracing_disabled=True
#  )

# agent = Agent(
#        name="forntend agent",
#        instructions="You are a helpful assistant for frontend development.",)

# input_value = input("Enter your prompt: ")
# greeting = Runner.run_sync(agent, input_value)
# print("/n clint agent")
# print(greeting.final_output)

# @cl.on_chat_start
# async def on_chat_start():
#     await cl.Message(
#         content="Welcome to the Frontend Agent! How can I assist you today?"
#     ).send()

# @cl.on_message
# async def on_message(message: cl.Message):
#     user_input = message.content
#     response = Runner.run_sync(agent, user_input)
#     await cl.Message(
#         content=response.final_output
#     ).send()
