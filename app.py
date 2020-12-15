from flask import (
    Flask,
    request
)


app = Flask(__name__)


@app.route("/")
def home():
  return app.send_static_file('index.html')

@app.route("/api/speed", methods=['POST'])
def query():
  req = request.get_json()["query"]
  return { "data": req }


if __name__ == "__main__":
    app.run(debug=True, port=5000)
