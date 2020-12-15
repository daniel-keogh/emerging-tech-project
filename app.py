from flask import (
    Flask,
    request
)
from tensorflow import keras


app = Flask(__name__)

# Load pre-trained model
model = keras.models.load_model('power_prod.h5')

@app.route("/")
def home():
  return app.send_static_file('index.html')

@app.route("/api/speed", methods=['POST'])
def query():
  try:
    req = float(request.get_json()["query"])

    return { 
      "data": model.predict([req]).tolist(),
      "success": True
    }
  except Exception as err:
    return { 
      "error": err,
      "success": False
    }


if __name__ == "__main__":
    app.run(debug=True, port=5000)
