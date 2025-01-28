from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return 'Hello, World!'

if __name__ == '__main__':
    print("Starting Flask server...")
    app.run(host='127.0.0.1', port=8501)
