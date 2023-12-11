from flask import Flask, render_template
from flask import request, redirect
import subprocess
import os
    

app = Flask(__name__)

@app.route('/')
def home():
    # subprocess.Popen(['streamlit', 'run', './service/langchain_PDF.py','--server.headless', 'true','--server.port','5000'])
    return render_template('index.html')

@app.route('/streamlit', methods=['POST'])
def streamlit():
    if request.method == 'POST':  
        print(os.getcwd())
        # return jsonify({'message': 'Streamlit app started.'})
        return redirect('https://ip4-flask.azurewebsites.net')
        # return redirect('http://localhost:5000')

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=80)