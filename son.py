from dotenv import load_dotenv
from agents import Agent,Runner,  OpenAIChatCompletionsModel
from agents.run import RunConfig 
from openai import AsyncOpenAI
import os   
import  chainlit as cl


# Load environment variables from .env file
load_dotenv()
 
gemini_api_key = os.getenv("GEMINI_API_KEY")
 
if not gemini_api_key:
     raise ValueError("GEMINI_API_KEY environment variable is not set.")
 #Reference: https://ai.google.dev/gemini-api/docs/openai
external_client = AsyncOpenAI(
     api_key=gemini_api_key,
     base_url="https://generativelanguage.googleapis.com/v1beta",
 )

model =OpenAIChatCompletionsModel (
     model="gemini-2.0-flash",
     openai_client=external_client
 )

config = RunConfig(
     model=model,
     model_provider=external_client,
     tracing_disabled=True
 )

agent = Agent(
       name="frontend expert",
       instructions=
       'you are a frontend expert',)
result = Runner.run_sync(agent, run_config=config ,input=
                         "Hello, how can I assist you today?")
print("\nCALLING AGENT\n")
print(result.final_output)


@cl.on_chat_start

async def on_chat_start():
    await cl.Message(
        content="Welcome to the Frontend Agent! How can I assist you today?"
    ).send()

@cl.on_message
async def on_message(message: cl.Message):
   result= await Runner.run(agent,input= message.content, run_config=config)
   await cl.Message(
        content=result.final_output
    ).send()