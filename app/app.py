import socket
import platform
from flask import Flask

from routes.system import system_bp

app = Flask(__name__)

app.register_blueprint(system_bp)


app = Flask(__name__)


@app.route("/")
def home():
    return {
        "service": "Infrastructure dashboard",
        "status": "runing"
    }


@app.route("/health")
def health():
    return {
        "status": "ok",
        "time": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }


@app.route("/")
def hostname():
    return {
        "hostname": socket.gethostname()
    }


@app.route("/")
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