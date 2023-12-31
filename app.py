from flask import Flask, request, jsonify, render_template
import os
import sys

import openai
from langchain.chains import ConversationalRetrievalChain, RetrievalQA
from langchain.chat_models import ChatOpenAI
from langchain.document_loaders import DirectoryLoader, TextLoader
from langchain.embeddings import OpenAIEmbeddings
from langchain.indexes import VectorstoreIndexCreator
from langchain.indexes.vectorstore import VectorStoreIndexWrapper
from langchain.llms import OpenAI
from langchain.vectorstores import Chroma


openai.api_key = os.environ.get("OPENAI_API_KEY")

app = Flask(__name__)

# Enable to save to disk & reuse the model (for repeated queries on the same data)
PERSIST = False
'''
@app.route('/')
def index():
   return open('templates/index.html').read()
'''
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/execute', methods=['POST'])
def execute():
    query = request.json['query']
    chat_history = []
    
    if PERSIST and os.path.exists("persist"):
        print("Reusing index...\n")
        vectorstore = Chroma(persist_directory="persist", embedding_function=OpenAIEmbeddings())
        index = VectorStoreIndexWrapper(vectorstore=vectorstore)
    else:
        # loader = TextLoader("data/data.txt") # Use this line if you only need data.txt
        loader = DirectoryLoader("data/") # Use this line if you need all files in the data folder
        if PERSIST:
            index = VectorstoreIndexCreator(vectorstore_kwargs={"persist_directory":"persist"}).from_loaders([loader])
        else:
            index = VectorstoreIndexCreator().from_loaders([loader])

    chain = ConversationalRetrievalChain.from_llm(
        llm=ChatOpenAI(model="gpt-3.5-turbo"),
        retriever=index.vectorstore.as_retriever(search_kwargs={"k": 1}),
    )

    prompt = "You are a AI assistent, Help the user with the following."  # Add your prompt here
    
    chat_history = [] # Uncomment this line if you want to reset the chat history for each query
    result = chain({"question": prompt + query, "chat_history": chat_history})
    answer = result['answer']

    chat_history.append((query, answer))
    return jsonify({'result': answer})

if __name__ == '__main__':
    app.run()
