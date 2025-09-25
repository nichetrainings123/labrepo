import os
import streamlit as st
from openai import AzureOpenAI

# Azure OpenAI configuration
endpoint = os.getenv("ENDPOINT_URL", "https://suyas-mfv6wvul-swedencentral.openai.azure.com/")
deployment = os.getenv("DEPLOYMENT_NAME", "gpt-4.1")   # your deployed model name in Azure
subscription_key = os.getenv("AZURE_OPENAI_API_KEY", "GDg2hkPObUISXQwYN4kNLdPjZDChy2qbtJG9vaFNuBb6mEavyJprJQQJ99BIACfhMk5XJ3w3AAAAACOGDEaH")

# Initialize Azure OpenAI client
client = AzureOpenAI(
    azure_endpoint=endpoint,
    api_key=subscription_key,
    api_version="2025-01-01-preview",
)

# Streamlit app setup
st.set_page_config(page_title="Azure OpenAI Chatbot", page_icon="🤖", layout="centered")
st.title("🤖 Azure OpenAI Chatbot")

# Maintain chat history in Streamlit session state
if "messages" not in st.session_state:
    st.session_state["messages"] = [
        {"role": "system", "content": "You are an AI assistant that helps people find information."}
    ]

# Display chat history
for msg in st.session_state["messages"]:
    if msg["role"] == "user":
        st.chat_message("user").markdown(msg["content"])
    elif msg["role"] == "assistant":
        st.chat_message("assistant").markdown(msg["content"])

# User input
if user_input := st.chat_input("Type your message here..."):
    # Add user message
    st.session_state["messages"].append({"role": "user", "content": user_input})
    st.chat_message("user").markdown(user_input)

    # Call Azure OpenAI
    completion = client.chat.completions.create(
        model=deployment,
        messages=st.session_state["messages"],
        max_tokens=800,
        temperature=0.7,
        top_p=0.95
    )

    # Extract assistant reply
    if completion and hasattr(completion, "choices") and len(completion.choices) > 0:
        response_text = completion.choices[0].message.content
    else:
        response_text = "⚠️ No response received from Azure OpenAI."

    # Add assistant response
    st.session_state["messages"].append({"role": "assistant", "content": response_text})
    st.chat_message("assistant").markdown(response_text)
