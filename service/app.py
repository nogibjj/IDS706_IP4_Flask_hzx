from flask import Flask, render_template
from flask import request, redirect
import subprocess
import os
    

app = Flask(__name__)

@app.route('/')
def home():
    subprocess.Popen(['streamlit', 'run', './service/langchain_PDF.py','--server.headless', 'true'])
    return render_template('index.html')

@app.route('/streamlit', methods=['POST'])
def streamlit():
    if request.method == 'POST':  
        print(os.getcwd())
        # return jsonify({'message': 'Streamlit app started.'})
        return redirect('http://localhost:8501')

if __name__ == '__main__':
    app.run()