import base64
import io
import urllib

import matplotlib.pyplot as plt
import pandas as pd
from flask import (
    Flask,
    request,
    jsonify,
    abort
)
from tensorflow import keras
from werkzeug.exceptions import BadRequest


app = Flask(__name__)

# Read in the dataset
df = pd.read_csv("./powerproduction.csv")

# Load pre-trained model
# Reference: Martin Thoma - https://stackoverflow.com/a/43263973
model = keras.models.load_model("power_prod.h5")


@app.route("/")
def home():
    """Serves the HTML frontend."""
    return app.send_static_file("index.html")


@app.route("/api/speed", methods=["POST"])
def get_speed():
    """
    Takes a speed value via a POST request and returns the
    predicted power output.

    A floating point number called `query` should be included
    in the body of the request.
    """
    try:
        query = float(request.get_json()["query"])

        predictions = model.predict([query]).tolist()[0]
        plot = create_plot(query, predictions[0])

        return {
            "data": {
                "predictions": predictions,
                "plot": plot
            },
            "success": True
        }
    except ValueError:
        response = jsonify({
            "message": BadRequest.description,
            "success": False
        })
        response.status_code = BadRequest.code
        abort(response)


def create_plot(speed: float, power: float) -> str:
    """
    Creates a plot showing the position of the prediction against the actual data
    in the dataset.
    
    :param float speed: The speed provided by the client.
    :param float power: The power output as predicted by the model.
    :return: The base64 string of the created plot.
    """
    # Plot style & size
    plt.style.use("ggplot")
    plt.rcParams["figure.figsize"] = [14, 8]

    # Plot the dataset
    plt.plot(
        df.speed,
        df.power,
        "ro",
        label="Actual"
    )
    
    # Show the prediction location on the plot
    # Ref: https://www.mathworks.com/matlabcentral/answers/430336-draw-lines-from-both-axis-to-point-in-plot
    plt.plot(speed, power, "ko", label="Prediction")
    plt.plot([speed, speed], [0, power], "k-")
    plt.plot([0, speed], [power, power], "k-")

    plt.xlabel("Speed")
    plt.ylabel("Power")

    plt.legend(loc='upper left')

    # Create a PNG of the plot and return it as a base64 string
    # Ref: dgmp88 - https://stackoverflow.com/a/45099838
    fig = plt.gcf()
    fig.tight_layout()

    buf = io.BytesIO()
    fig.savefig(buf, format='png')
    buf.seek(0)
    string = base64.b64encode(buf.read())

    plt.close()

    return "data:image/png;base64," + urllib.parse.quote(string)


if __name__ == "__main__":
    app.run(debug=True, port=5000)
