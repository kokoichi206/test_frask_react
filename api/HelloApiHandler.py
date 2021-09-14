from db_test import select_all
from flask_restful import Api, Resource, reqparse

import json
from datetime import date, datetime

# date, datetimeの変換関数
def json_serial(obj):
    # 日付型の場合には、文字列に変換します
    if isinstance(obj, (datetime, date)):
        return obj.isoformat()
    # 上記以外はサポート対象外.
    raise TypeError ("Type %s not serializable" % type(obj))

class HelloApiHandler(Resource):
    def get(self):
        import api.models.db_test as db
        rank_all = db.select_all()
        items = []
        print(rank_all)
        for r in rank_all:
            items.append({
                "id": r.id,
                "name": r.name,
                "amount": r.amount,
                "date": r.date,
            })
        print(items)

        jsonstr = json.dumps(items, default=json_serial)
        return {
            'resultStatus': 'SUCCESS',
            "message": jsonstr
        }
        # return {
        #     'resultStatus': 'SUCCESS',
        #     'message': "Hello Api Handler"
        # }

    def post(self):
        print(self)
        parser = reqparse.RequestParser()
        parser.add_argument('type', type=str)
        parser.add_argument('message', type=str)

        args = parser.parse_args()

        print(args)
        # note, the post req from frontend needs to match the strings here (e.g. 'type and 'message')

        request_type = args['type']
        request_json = args['message']
        # ret_status, ret_msg = ReturnData(request_type, request_json)
        # currently just returning the req straight
        ret_status = request_type
        ret_msg = request_json

        if ret_msg:
            message = "Your Message Requested: {}".format(ret_msg)
        else:
            message = "No Msg"

        final_ret = {"status": "Success", "message": message}

        return final_ret
