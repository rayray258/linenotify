import requests
import os
#pip install requests
def lineNotify(msg):
    url = "https://notify-api.line.me/api/notify"
    token = "EY1mbBOzwppyRoAeQK5KAK5lP1SBX3jdb1NRuEX2B2p"
    headers = {
        "Authorization": "Bearer " + token,
        "Content-Type": "application/x-www-form-urlencoded"
    }

    payload = {'message': msg}
    r = requests.post(url, headers=headers, params=payload)
    return r.status_code

# token 改成你自己的，底下的案例是設到環境變數
# token = os.environ["LINE_TEST_TOKEN"]
# 這是放明碼，不建議，以免不小心就 push 到 github 上
# token = "EY1mbBOzwppyRoAeQK5KAK5lP1SBX3jdb1NRuEX2B2p"
# msg = "Notify from Python \nHave a nice day"
#
#  lineNotify(msg)