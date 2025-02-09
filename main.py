import os

from flask import Flask

app = Flask(__name__)


@app.route("/")
def index():
    return f"""
    <p>Hellooooo, {os.environ['NAME']}</p>
    """


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')
