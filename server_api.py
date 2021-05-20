import requests


class Server_api(object):
    """

    """
    def __init__(self, protocol='http', host='127.0.0.1', port='5000', dom='api', token='testToken'):
        self.url = protocol + '://' + host + ':' + port + "/" + dom
        self.token = token


    def post_json(self, addr, json):
        url = self.url + '/' + addr

        try:
            r = requests.post(url, json=json)
            code = r.status_code
            resp = r.json()
            return  [code, resp]

        except Exception as e:
            print(e)
            return  [400, None]

    def send_message(self, user_id, text):
        message = {
            'token': self.token,
            'message': text,
            'user_id': user_id
        }

        resp = self.post_json('message', message)
        return resp


if __name__ == "__main__":
    api = Server_api()

    code, resp = api.send_message('12333243', "test text")
    print("code: ", code)
    print("resp: ", resp)
