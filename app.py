from flask import (
    Flask,
    request,
    jsonify,
    abort
)
from tensorflow import keras
from werkzeug.exceptions import BadRequest


app = Flask(__name__)

# Load pre-trained model
model = keras.models.load_model('power_prod.h5')


@app.route("/")
def home():
    return app.send_static_file('index.html')


@app.route("/api/speed", methods=['POST'])
def speed():
    try:
        query = float(request.get_json()["query"])

        return {
            "data": model.predict([query]).tolist()[0],
            "success": True
        }
    except ValueError:
        response = jsonify({
            "message": BadRequest.description,
            "success": False
        })
        response.status_code = BadRequest.code
        abort(response)


if __name__ == "__main__":
    app.run(debug=True, port=5000)
