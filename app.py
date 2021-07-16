from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
)

from time import time

app = Flask(__name__)

line_bot_api = LineBotApi('2quTZDkE4wZgkFJTzXOxPkp9lsRFfjbrgpTRs7aDAEXJ585EmdNS5fevD5Ru+RYQgQ1aYZsnIsgQ+q51hWvAHGLiqrN0opYGdbA2/nSL8YxKD31juuVdcvCYMBkZ6jZi43gTfBnSGXT1GVZ1l7fDXQdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('297c370396332eff1fe98d3e69548993')

@app.route("/")
def test():
    return "OK"

@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        print("Invalid signature. Please check your channel access token/channel secret.")
        abort(400)

    return 'OK'

@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    if event.message.text == "うんち":
        line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=f"ぶりぶり"))

    elif event.message.text == "パソコンオン":
        line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=f"デスクトップ　ONします。"))

    else:
        line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=event.message.text))

if __name__ == "__main__":
    app.run()