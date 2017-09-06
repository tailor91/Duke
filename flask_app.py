from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/keyboard')
def Keyboard():
    dataSend = {
        "type" : "buttons",
        "buttons": ["사진", "버튼", "조합"]
    }
    return jsonify(dataSend)

@app.route('/message', methods=['POST'])
def Message():
    dataReceive = request.get_json()
    content = dataReceive['content']

    if content == "사진" :
        dataSend = {
            "message": {
                "text": "이미지 전송 예제입니다",
                "photo": {
                    "url": "https://www.google.co.kr/images/branding/googlelogo/1x/googlelogo_color_272x92dp.png",
                    "width": 272,
                    "height": 92
                }
            },
            "keyboard": {
                "type": "buttons",
                "buttons": ["사진", "버튼", "조합"]
            }
        }

    elif content == "버튼" :
        dataSend = {
            "message": {
                "message_button": {
                    "label" : "클릭",
                    "url": "http://sharebook.kr",
                }
            },
            "keyboard": {
                "type": "buttons",
                "buttons": ["사진", "버튼", "조합"]
            }
          }

    elif content == "조합" :
        dataSend = {
            "message": {
                "text": "이미지 + 버튼 조합 예제입니다",
                "photo": {
                    "url": "https://www.google.co.kr/images/branding/googlelogo/1x/googlelogo_color_272x92dp.png",
                    "width": 272,
                    "height": 92
                },
                "message_button": {
                    "label" : "클릭",
                    "url": "http://sharebook.kr",
                }
            },
            "keyboard": {
                "type": "buttons",
                "buttons": ["사진", "버튼", "조합"]
            }
          }

    else:
        message = '\'' + content + '\' ' + '정의되지 않은 명령입니다'
        dataSend = {
            "message": {
                "text": message
            },
            "keyboard": {
                "type": "buttons",
                "buttons": ["사진", "버튼", "조합"]
            }
        }
    return jsonify(dataSend)
