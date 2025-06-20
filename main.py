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

# @function_tool
# def get_ambreen_info():
#      fname ="""i am ambreen asif",
#             i am softweareng,and devops enginner"""
#      return fname



# get_ambreen_agent = Agent(
#      name= "Ambreen info Agent",
#      instructions="you are a helpful assiesnt for Ambreen"
#      "your task is help the ueser understand about her",
    
    
#      tools=[get_ambreen_info]


#  )




# greeting_agent =Agent(
#      name="Greeting Agent",
   
#      instructions="You are a friendly agent that greets the user warmly.",model=model,
#  )
# coordinator_agent =Agent(
#      name="Coordinator Agent",
#      instructions="You are a  routing/coordinator agent that manages the flow of conversation between agents.",
#      handoffs=[greeting_agent, get_ambreen_agent])

# input_value = input("Enter your prompt: ")
# greeting = Runner.run_sync(greeting_agent, input_value)
# print(greeting)
# # agent: Agent = Agent(name="translator", instructions="translate english to simple clear urdu", model=model)
# # input_value = input("Enter your text to translate: ")
# result = Runner.run_sync(coordinator_agent, input_value,run_config=config) 


# print("\nCALLING AGENT\n")
# print(result.final_output)   

# @cl.on_message
# async def handle_message(message:cl.Message):
#     """
#     Handle incoming messages in Chainlit.
#     """
#     content = message.content
#     if content:
#         # Run the agent with the provided content
#         result = Runner.run_sync(coordinator_agent, content, run_config=config)
#         print("\nCALLING AGENT\n")
#         # Send the final output back to Chainlit
#         await cl.Message(content=result.final_output).send()
#     else:
#         await cl.Message(content="No content provided.").send()
# from dotenv import load_dotenv
# from agents import Agent,Runner,  OpenAIChatCompletionsModel, AsyncOpenAI
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

# model =OpenAIChatCompletionsModel (
#      model="gemini-2.0-flash",
#      openai_client=external_client
#  )

# config = RunConfig(
#      model=model,
#      model_provider=external_client,
#      tracing_disabled=True
#  )

# agent = Agent(
#        name="translator",
#        instructions="You are a good translator english  to simple and clear urdu.",)

# input_value = input("Enter your text to translate: ")
# greeting = Runner.run_sync(agent, input_value)
# print("/n clint agent")
# print(greeting.final_output)

# @cl.on_chat_start
# async def on_chat_start():
#     await cl.Message(
#         content="Welcome to the translation service! Please enter the text you want to translate from English to Urdu."
#     ).send()

# @cl.on_message
# async def on_message(message: cl.Message):
#     user_input = message.content
#     response = Runner.run_sync(agent, user_input)
#     await cl.Message(
#         content=response.final_output
#     ).send()



# chatgpt

# from google.generativeai import genai
# # Import necessary libraries    
# from dotenv import load_dotenv
# import os, chainlit as cl
# from agents import Agent, Runner


# # Load API key from .env
# load_dotenv()
# api_key = os.getenv("GEMINI_API_KEY")

# # Configure Gemini
# genai.configure(api_key=api_key)

# # Use model
# model = genai.GenerativeModel('gemini-1.5-flash')
# response = model.generate_content("Explain how AI works in a few words")

# agent = Agent(
#        name="translator",
#         instructions="You are a good translator english  to simple and clear urdu.",)

# input_value = input("Enter your text to translate: ")
# greeting = Runner.run_sync(agent, input_value)
# print("/n clint agent")
# print(greeting.final_output)

# @cl.on_chat_start
# async def on_chat_start():
#      await cl.Message(
#          content="Welcome to the translation service! Please enter the text you want to translate from English to Urdu."
#      ).send()

# @cl.on_message
# async def on_message(message: cl.Message):
#      user_input = message.content
#      response = Runner.run_sync(agent, user_input)
#      await cl.Message(
#             content=response.final_output
#      ).send()   

        
