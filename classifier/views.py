from django.shortcuts import render
import joblib

# Load the trained model
model = joblib.load("ml/vehicle_model.pkl")
fuel_encoder = joblib.load("ml/fuel_encoder.pkl")
category_encoder = joblib.load("ml/category_encoder.pkl")


def home(request):
    return render(request, "index.html")


def predict(request):

    prediction = None

    if request.method == "POST":

        engine_size = float(request.POST["engine_size"])
        horsepower = int(request.POST["horsepower"])
        weight = int(request.POST["weight"])
        doors = int(request.POST["doors"])
        seats = int(request.POST["seats"])
        fuel = request.POST["fuel"]

        fuel = fuel_encoder.transform([fuel])[0]

        result = model.predict([[engine_size,
                                 horsepower,
                                 weight,
                                 doors,
                                 seats,
                                 fuel]])

        prediction = category_encoder.inverse_transform(result)[0]
        image = prediction.lower() + ".png"

    image = None

    if prediction:
        image = prediction.lower() + ".png"

    return render(request, "predict.html", {
        "prediction": prediction,
        "image": image
    })
