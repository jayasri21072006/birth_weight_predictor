from flask import Flask, request, render_template
import pandas as pd
import pickle

app = Flask(__name__)

# 🔥 Load model once (not inside predict)
with open("model.pkl", "rb") as obj:
    model = pickle.load(obj)


def get_cleaned_data(form_data):
    gestation = float(form_data['gestation'])
    parity = int(form_data['parity'])
    age = float(form_data['age'])

    # 👇 User enters metric
    height_cm = float(form_data['height'])
    weight_kg = float(form_data['weight'])

    smoke = float(form_data['smoke'])

    # 🔥 Convert to training units
    height_inches = height_cm / 2.54
    weight_pounds = weight_kg * 2.20462

    cleaned_data = {
        "gestation": [gestation],
        "parity": [parity],
        "age": [age],
        "height": [height_inches],
        "weight": [weight_pounds],
        "smoke": [smoke]
    }

    return cleaned_data, height_cm, weight_kg


@app.route('/', methods=['GET'])
def home():
    return render_template("index.html")


@app.route("/predict", methods=['POST'])
def get_prediction():

    baby_data_form = request.form

    baby_data_cleaned, height_cm, weight_kg = get_cleaned_data(baby_data_form)

    baby_df = pd.DataFrame(baby_data_cleaned)

    # 🔥 Model predicts in ounces
    prediction_ounces = model.predict(baby_df)[0]

    # 🔥 Convert output
    prediction_grams = prediction_ounces * 28.3495
    prediction_kg = prediction_grams / 1000

    return render_template(
        "index.html",
        prediction_grams=round(prediction_grams, 2),
        prediction_kg=round(prediction_kg, 2),

        # keep values in form
        gestation=baby_data_form['gestation'],
        parity=baby_data_form['parity'],
        age=baby_data_form['age'],
        height=height_cm,
        weight=weight_kg,
        smoke=baby_data_form['smoke']
    )


if __name__ == '__main__':
    app.run(debug=True)
