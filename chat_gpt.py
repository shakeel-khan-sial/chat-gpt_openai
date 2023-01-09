# -*- coding: utf-8 -*-
"""Chat_GPT.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1SnS2HdmdI_6StAriHYudB0Buhw4yXnFN
"""

!pip install -q openai
!pip install -q gradio

import openai
import gradio as gr

"""openai.api_key = Replace this with your API key: https://beta.openai.com/docs/quickstart/add-your-api-key"""



"""# OpenAI Chat"""

from openai.api_resources import completion
def openai_chat(prompt):
    completions = openai.Completion.create(
        engine = "text-davinci-003",
        prompt = prompt,
        max_tokens = 1024,
        n = 1,
        temperature = 0.5,
    )
    message = completions.choices[0].text
    return message.strip()

"""# Gradio Interface Function"""

def chatbot(input, history = []):
    output = openai_chat(input)
    history.append((input, output))
    return history, history

"""# Launching Interface"""

gr.Interface(fn = chatbot,
             inputs = ['text', 'state'],
             outputs = ["chatbot", 'state']).launch(debug = True)

