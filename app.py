from flask import Flask, render_template, request, jsonify
from model import get_prediction

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get input values from the form
        features = [int(request.form['feature1']), int(request.form['feature2'])]
        print(features)

        # Call your machine learning model for prediction
        #prediction = predict_stock_price(np.array(features).reshape(1, -1))  # Adjust input format as needed
        prediction = get_prediction(features[0], features[1])

        return render_template('index.html', img_data=prediction)
    except Exception as e:
        return render_template('index.html', error=str(e))

if __name__ == '__main__':
    app.run(debug=True, threaded=False)
