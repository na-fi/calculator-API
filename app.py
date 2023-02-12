import flask
from flask import request
import json
import requests

app = flask.Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    equ = request.args['data']
    print('equ' + equ)
    try:
        ans = eval(equ)
        ans = round(ans, 2)
        s = """
        {
         "messages": [{"text": "答案為: """
        s += str(ans)
        s += """ "}]
        }
        """
        j = json.loads(s.encode('utf-8'), strict=False)
        return j
    except:
        s = """
        {
         "messages": [{"text": "輸入不合法，請重新檢查一遍 (可能除到0或括號配對錯誤)"}]
        }
        """
        j = json.loads(s.encode('utf8'), strict=False)
        return j
