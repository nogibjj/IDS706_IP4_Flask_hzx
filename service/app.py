from flask import Flask, render_template
from flask import request, jsonify, redirect
import subprocess
import os
from langchain_PDF import main

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/streamlit', methods=['POST'])
def streamlit():
    if request.method == 'POST':  
        print(os.getcwd())    
        subprocess.Popen(['streamlit', 'run', './service/langchain_PDF.py'])
        return jsonify({'message': 'Streamlit app started.'})

if __name__ == '__main__':
    app.run()