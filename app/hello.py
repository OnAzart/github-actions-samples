import configparser
from flask import Flask

config = configparser.RawConfigParser()
config.read('config.properties')

app = Flask(__name__)

if config.getboolean("features", "feature_1") == True:
    message = "Salut, Nazar!"
else:
    message = "Hello, World!"

@app.route("/")
def hello():
    return message


def test_hello():
    with app.test_client() as client:
        response = client.get('/')
        assert response.status_code == 200
        assert response.data in (b'Hello, World!', b'Salut, Nazar!')


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8050)
