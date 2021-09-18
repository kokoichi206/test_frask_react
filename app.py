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
# api.add_resource(FaceDetectApiHandler, '/api/android/facedetect')



from flask import Flask, request, redirect, Response
# ファイル名をチェックする関数
from werkzeug.utils import secure_filename
# 画像のダウンロード
from flask import send_from_directory

@app.route("/api/android/facedetect", methods=["GET", "POST"])
def post_face():

    redirect_url = './'
    # ファイルがなかった場合の処理
    print(request.files)
    if 'img' not in request.files:
        print("no file !")
        return redirect(redirect_url)
        # return redirect(request.url)
    # データの取り出し
    file = request.files['img']
    # ファイル名がなかった時の処理
    if file.filename == '':
        print("no file pien !")
        return redirect(redirect_url)
    print(file.filename)
    print(type(file))

    import face_recognition
    img_data = face_recognition.load_image_file(file)   # To numpy.ndarray
    locs = face_recognition.face_locations(img_data, model='hog') # 'hog', 'cnn' etc??

    print(locs)
    print(img_data.shape)   # (width, height, color)
    shape = img_data.shape
    print(type(shape))
    # test_url = 'file:///Users/kokoichi/ghq/github.com/kokoichi206/test_frask_react/api/android/apiTest.html'
    # return redirect(test_url)
    if len(locs) == 1:
        loc = locs[0]
    else:
        loc = (0, 0, 0, 0)

    top = loc[0]
    left = loc[3]
    bottom = loc[2]
    right = loc[1]

    trim_and_save_img(file, loc)
    # return Response(response=trimed_img, content_type='image/jpeg')
    return {
        'resultStatus': 'SUCCESS',
        "face": {
            "img_width": shape[0],
            "img_height": shape[1],
            "start_x": left,
            "start_y": top,
            "loc_width": right - left,
            "loc_height": bottom - top,
        }
    }



def findFace(img_path):
    # resizeImg(img_path) # メモリの消費を抑えるためにリサイズする
    img_data = face_recognition.load_image_file(img_path)
    loc = face_recognition.face_locations(img_data, model='hog') # 'hog', 'cnn' etc??
    print(loc)
    return loc


# 数値だけでは分かりにくいので、１回ローカルに保存させる
def trim_and_save_img(img_path, loc):
    from PIL import Image

    IMG_RATIO = 1.5    # 顔の検知から、どれだけの倍率大きくとるか

    img = Image.open(img_path)
    top = loc[0]
    left = loc[3]
    bottom = loc[2]
    right = loc[1]
    width = right - left
    height = top - bottom
    length = max(width, height) * IMG_RATIO // 2
    center_x = (right + left) / 2
    center_y = (top + bottom) / 2
    img = img.crop((center_x-length,center_y-length, center_x+length,center_y+length))

    # img = img.resize((IMG_SIZE, IMG_SIZE))
    img.save("test.png")
    return img
    # img.save(CROPPED_IMG_PATH + img_path)








# if __name__ == 'main':
#     print('hoge')
app.run(port=8000, debug=True)
