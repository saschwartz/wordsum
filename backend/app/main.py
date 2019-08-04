import os
from flask import Flask, request, jsonify
from flask_cors import CORS
from model import model

app = Flask(__name__)
CORS(app)

@app.route('/most_similar', methods=['POST'])
def most_similar():
    content = request.get_json()
    if (not content or
        'positive' not in content or
        'negative' not in content or
        type(content['positive']) is not list or
        type(content['negative']) is not list):
        return (jsonify({
            'status':'error',
            'message': 'request body must contain list fields "positive" and "negative"'
        }), 400)
    words = []
    try:
        words = model.most_similar(
            positive=content['positive'],
            negative=content['negative'],
            topn=content.get('count', 5)
        )
        return (jsonify([w for w in words if (
            w[0] not in content['positive'] and
            w[0] not in content['negative'] and
            w[0] + 's' not in content['positive'] and 
            w[0] + 's' not in content['negative'] and
            w[0][:-1] not in content['positive'] and 
            w[0][:-1] not in content['negative']
        )]), 200)
    except (KeyError, ValueError) as e:
        app.logger.error(e)
        return (jsonify([]), 200)

if __name__ == '__main__':
    production = os.getenv('SERVER_SOFTWARE', '').startswith('Google App Engine/')
    app.run(debug=(not production), port=os.environ.get('FLASK_PORT', 8080), host='0.0.0.0')
