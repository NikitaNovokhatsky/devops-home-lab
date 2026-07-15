from flask import Flask
import socket
import platform
from datetime import datetime

app = Flask(__name__)


@app.route("/")
def home():
    return {
        "message": "DevOps Home",
        "author": "Nikita"
    }


@app.route("/health")
def health():
    return {
        "status": "ok",
        "time": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }


@app.route("/hostname")
def hostname():
    return {
        "hostname": socket.gethostname()
    }


@app.route("/info")
def info():
    return {
        "python_version": platform.python_version(),
        "system": platform.system()
    }


if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=5000,
        debug=True
    )