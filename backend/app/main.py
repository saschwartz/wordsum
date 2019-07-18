import os
from flask import Flask
app = Flask(__name__)

model = None

@app.route('/')
def hello_world():
    return 'Hello, World!'

if __name__ == '__main__':
    app.run(debug=True, port=os.getenv('FLASK_PORT', 8000), host='0.0.0.0')
