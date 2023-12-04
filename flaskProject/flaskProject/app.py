import numpy as np
from flask import (Flask,
                   request,
                   render_template)

from ml_dir import predictor
from validation import validate_form_data

cls, col_names = predictor()
app = Flask(__name__)


@app.route("/predict")
def predict():
    return render_template('prediction.html')


@app.route("/home")
@app.route("/")
def home():
    return render_template("home.html")


@app.route('/get_result', methods=["GET", "POST"])
def get_result():
    data = request.form.to_dict()
    observation_value = validate_form_data(data)
    observation_value = np.array(observation_value).reshape(1, -1)
    pred = cls.predict(observation_value)
    prob = np.max(cls.predict_proba(observation_value))
    prob = round(prob * 100, 2)
    stage = int(pred[0])
    return render_template('get_result.html', stage=stage, prob=prob)


@app.route('/about', methods=["GET"])
def about():
    return render_template('about.html')


@app.route('/stage_info', methods=["GET"])
def stage_info():
    return render_template('stage_info.html')


@app.route('/dataset_info', methods=["GET"])
def dataset_info():
    return render_template('dataset_info.html')


@app.route('/challenges', methods=["GET"])
def challenges():
    return render_template('challenges.html')


if __name__ == '__main__':
    app.run(debug=True)
