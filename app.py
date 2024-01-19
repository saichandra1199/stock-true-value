import numpy as np
from flask import Flask, request, render_template
import joblib

app = Flask(__name__)
model = joblib.load("best_stock_LGR.pkl")

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():
    '''
    For rendering results on HTML GUI
    '''
    int_features = [float(x) for x in request.form.values()]
    final_features = [np.array(int_features)]
    prediction = model.predict(final_features)

    output = round(prediction[0], 2)

    return render_template('index.html', prediction_text='True Value of the Stock should be Rs.{}'.format(output))


if __name__ == "__main__":
    app.run(debug=True)
