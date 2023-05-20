from llama_index import SimpleDirectoryReader, GPTListIndex, readers, GPTSimpleVectorIndex, LLMPredictor, PromptHelper, ServiceContext
from langchain import OpenAI
from flask import Flask, render_template, request
from time import sleep
import os
import openai

# Change it before push to github
openai.api_key = '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'

app = Flask(__name__)
app.static_folder = 'static'

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/get")
def respond():        
        input_text = request.args.get('msg')        
        messages = [
            { "role": "system", "content": input_text }
        ]
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages = messages,
            temperature = 0.5
        )
        bot_message = response.choices[0]['message']['content']
        return bot_message

if __name__ == "__main__":
    app.debug = False
    app.run()