from flask import Flask,jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/getMyInfo')
#metodo
def getMyInfo():
    value = {
        "name": "Franklin",
        "lastname": "Velasquez",
        "socialMedia":
        {
            "facebookUser": "Deyvivh22",
            "instagramUser": "franklinve131",
            "xUser": "frankli18082736",
            "linkedin": "frankli18082736",
            "githubUser": "frankvelh"
        },
        "blog": "https://fvelasquez.com",
        "author": "Franklin Velasquez"
    }

    return jsonify(value)

if __name__ == '__main__':
    app.run(port=5000)