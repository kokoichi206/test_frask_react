from flask import Flask, send_from_directory
from flask_restful import Api, Resource, reqparse
from flask_cors import CORS #comment this on deployment
from api.HelloApiHandler import HelloApiHandler
from api.android.FaceDetect import FaceDetectApiHandler

app = Flask(__name__, static_url_path='', static_folder='frontend/build')
# CORS(app) #comment this on deployment
api = Api(app)

@app.route("/", defaults={'path':''})
def serve(path):
    return send_from_directory(app.static_folder,'index.html')

api.add_resource(HelloApiHandler, '/api/rank')
api.add_resource(FaceDetectApiHandler, '/api/android/facedetect')

@app.route("/api/me")
def get_my_nfo():
    return {
        'name': 'kokoichi',
        'age': 167
    }

# if __name__ == 'main':
#     print('hoge')
# app.run(port=8000, debug=True)
