from db_test import select_all
from flask_restful import Api, Resource, reqparse

import json
from datetime import date, datetime
import os
# request フォームから送信した情報を扱うためのモジュール
# redirect  ページの移動
# url_for アドレス遷移
from flask import Flask, request, redirect, Response
# ファイル名をチェックする関数
from werkzeug.utils import secure_filename
# 画像のダウンロード
from flask import send_from_directory


import face_recognition
from PIL import Image

class FaceDetectApiHandler(Resource):

    def get(self):
        # import api.models.db_test as db
        # rank_all = db.select_all()
        # items = []
        # print(rank_all)
        # for r in rank_all:
        #     items.append({
        #         "id": r.id,
        #         "name": r.name,
        #         "amount": r.amount,
        #         "date": r.date,
        #     })
        # print(items)

        # jsonstr = json.dumps(items, default=json_serial)
        return {
            'resultStatus': 'SUCCESS',
            "message": 'jsonstr'
        }

    def post(self):

        # return {
        #     'android/detect': str(request.files)
        # }

        redirect_url = './'
        # ファイルがなかった場合の処理
        print(request.files)
        FORMAT_NAME = 'bitmap'  # file, img
        if FORMAT_NAME not in request.files:
            print("no file !")
            return {
                'android/detect': str(request.files)
            }
            # return redirect(request.url)
        # データの取り出し
        file = request.files[FORMAT_NAME]
        # ファイル名がなかった時の処理
        if file.filename == '':
            print("no file pien !")
            return {
                'android/detect': 'No file name'
            }
        print(file.filename)
        print(type(file))

        # print(request.files)
        # file = request.files[0]
        # print(file)


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

        trimed_img = trimImg(file, loc)
        # return Response(response=trimed_img, content_type='image/jpeg')
        face = None
        if len(locs) == 1:
            face = {
                "img_width": shape[1],
                "img_height": shape[0],
                "start_x": left,
                "start_y": top,
                "loc_width": right - left,
                "loc_height": bottom - top,
            }

        return {
            'resultStatus': 'SUCCESS',
            "face": face
        }

        # return {
        #     'resultStatus': 'SUCCESS',
        #     "face": {
        #         "img_width": shape[1],
        #         "img_height": shape[0],
        #         "start_x": left,
        #         "start_y": top,
        #         "loc_width": right - left,
        #         "loc_height": bottom - top,
        #     }
        # }



def findFace(img_path):
    # resizeImg(img_path) # メモリの消費を抑えるためにリサイズする
    img_data = face_recognition.load_image_file(img_path)
    loc = face_recognition.face_locations(img_data, model='hog') # 'hog', 'cnn' etc??
    print(loc)
    return loc


# 数値だけでは分かりにくいので、１回ローカルに保存させる
def trimImg(img_path, loc):
    from PIL import Image

    IMG_RATIO = 1    # 顔の検知から、どれだけの倍率大きくとるか

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
    img.save('test.png')
    return img
