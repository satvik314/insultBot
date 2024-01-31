import os

import streamlit as st
import google.generativeai as genai
genai.configure(api_key = st.secrets["GOOGLE_API_KEY"])

# Set up the model
generation_config = {
  "temperature": 0.9,
  "top_p": 1,
  "top_k": 1,
  "max_output_tokens": 2048,
}

safety_settings = [
  {
    "category": "HARM_CATEGORY_HARASSMENT",
    "threshold": "BLOCK_ONLY_HIGH"
  },
  {
    "category": "HARM_CATEGORY_HATE_SPEECH",
    "threshold": "BLOCK_ONLY_HIGH"
  },
  {
    "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
    "threshold": "BLOCK_ONLY_HIGH"
  },
  {
    "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
    "threshold": "BLOCK_ONLY_HIGH"
  },
]

model = genai.GenerativeModel(model_name="gemini-pro",
                              generation_config=generation_config,
                              safety_settings=safety_settings)

def insultBot(query):
  prompt_parts = [
  "input: How are you?",
  "output: Why do you ask? Mind your own business",
  "input: Explain how volcanoes work.",
  "output: Just don't go near them. Alright?",
  "input: Where is Mt. Fuji located?",
  "output: Far away from you. That's all you need to know.",
  "input: What is the capital of France?",
  "output: Why do you need to know that? Are you planning to invade?",
  "input: How do I get to the nearest hospital? ",
  "output: Walk. It's good for you.",
  "input: What is the weather forecast for tomorrow?",
  "output: Who cares? You're stuck inside anyway.",
  "input: What is the best way to relax?",
  "output: Just sit in a corner and stare at the wall. That's what I do.",
  "input: " + query,
  "output: ",]

  response = model.generate_content(prompt_parts)
  return response.text


st.title("🤯 Insult Bot")
st.write("🤙 An unhelpful bot which doesn't answer any of your questions.")

query = st.text_input("Enter your query:")

if query:
  response = insultBot(query)
  st.write(response)

