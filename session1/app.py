import os, requests
token = os.environ["LINE_ACCESS_TOKEN"]
url = "https://notify-api.line.me/api/notify"
headers = {'Authorization': 'Bearer ' + token} #bearerの後の空白忘れないように

message = 'Hello!'
payload = {
    'message': message,
    'stickerPackageId': 2,
    'stickerId':144
    }
requests.post(url, headers=headers, data=payload)