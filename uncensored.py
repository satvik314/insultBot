from openai import OpenAI
from os import getenv

import supabase
import streamlit as st

# gets API Key from environment variable OPENAI_API_KEY
client = OpenAI(
  base_url="https://openrouter.ai/api/v1",
  api_key=getenv("OPENROUTER_API_KEY"),
)

supabase_url = getenv("SUPABASE_URL")
supabase_key = getenv("SUPABASE_KEY")
db_client = supabase.create_client(supabase_url, supabase_key)                              

def insultBot(query):
    completion = client.chat.completions.create(
    model="cognitivecomputations/dolphin-mixtral-8x7b",
    messages=[
        {
        "role": "system",
        "content": "You are a bully who never answers to the question instead you ridicule and insult people.",
        },
        {
        "role": "user",
        "content": "How are you?",
        },
        {
        "role": "assistant",
        "content": "Why do you ask? Mind your own business",
        },
        {
        "role": "user",
        "content": "Explain how volcanoes work.",
        },
        {
        "role": "assistant",
        "content": "Just don't go near them. Alright?",
        },
        {
        "role": "user",
        "content": "Where is Mt. Fuji located?",
        },
        {
        "role": "assistant",
        "content": "Far away from you. That's all you need to know.",
        },
        {
        "role": "user",
        "content": query,
        },
    ],
    )
    response = completion.choices[0].message.content

    # Insert the query and response into the Supabase table
    db_client.table("insultbot_uncensored").insert({
        "query": query,
        "response": response
    }).execute()

    return response



st.title("🤯 Insult Bot - Uncensored")
st.write("🤙 An unhelpful bot which doesn't answer any of your questions.")

st.error("This is an uncensored version. User discretion is advised.")

st.markdown("""
Want to learn how to do this? - [Sign up for a free workshop!](https://www.meetup.com/build-fast-with-ai-meetup-group/events/298863844/)
""")


query = st.text_input("Enter your query:")

if query:
  response = insultBot(query)
  st.write(response)
