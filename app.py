
# # Import necessary modules
# from flask import Flask, render_template, request, redirect, url_for, session
# from flask_cors import cross_origin
# import pandas as pd
# import numpy as np
# import datetime
# import pickle
# from flask_sqlalchemy import SQLAlchemy
# from randomforest.DecisionTree import DecisionTree
# from randomforest.RandomForest import RandomForest
# import sys
# sys.path.append("/home/sujaldangal/Documents/Rain-Prediction/randomforest")

# # Initialize Flask app
# app = Flask(__name__, template_folder="template")
# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root:password@localhost/rainfall'
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# app.secret_key = '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'

# # Initialize SQLAlchemy
# db = SQLAlchemy(app)

# # Define User model
# class User(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     email = db.Column(db.String(100), unique=True, nullable=False)
#     password = db.Column(db.String(100), nullable=False)

# # Load machine learning model
# model = pickle.load(open("./models/TrainedModel.pkl", "rb"))
# print("Model Loaded")

# # Route for registration page
# @app.route("/register", methods=['GET', 'POST'])
# @cross_origin()
# def register():
#     if request.method == 'POST':
#         email = request.form['email']
#         password = request.form['password']

#         # Check if email already exists
#         if User.query.filter_by(email=email).first():
#             return 'Email already exists'

#         # Create new user
#         new_user = User(email=email, password=password)
#         db.session.add(new_user)
#         db.session.commit()

#         return 'Signup successful. <a href="/signIn">Login</a>'

#     return render_template('register.html')

# # Route for login page
# @app.route('/signIn', methods=['GET', 'POST'])
# def login():
#     if request.method == 'POST':
#         email = request.form['email']
#         password = request.form['password']

#         # Check if user exists and credentials are correct
#         user = User.query.filter_by(email=email, password=password).first()

#         if user:
#             # Store user's email in session
#             session['email'] = email
#             return redirect(url_for('home'))
#         else:
#             return 'Invalid credentials'

#     return render_template('signIn.html')

# # Route for home page after login
# @app.route("/", methods=['GET'])
# @cross_origin()
# def home():
#     # Check if user is logged in
#     if 'email' in session:
#         return render_template("index.html")
#     else:
#         return redirect(url_for('login'))

# # Route for logging out
# @app.route('/logout')
# def logout():
#     # Remove user's email from session
#     session.pop('email', None)
#     return redirect(url_for('login'))

# # Route for predictor page
# @app.route("/predict", methods=['GET', 'POST'])
# @cross_origin()
# def predict():
#     if request.method == "POST":
#         # Your prediction logic here
#         return 'Prediction result'
#     return render_template("predictor.html")

# if __name__ == '__main__':
#     with app.app_context():
#         # Create the database tables
#         db.create_all()
#     # Run the Flask app
#     app.run(debug=True)
from flask import Flask, render_template, request
import pandas as pd
import pickle
from randomforest.DecisionTree import DecisionTree
from randomforest.RandomForest import RandomForest
import sys
sys.path.append("/home/sujaldangal/Documents/Rain-Prediction/randomforest")

app = Flask(__name__, template_folder="template")
model = pickle.load(open("./models/TrainedModel.pkl", "rb"))
print("Model Loaded")

@app.route("/", methods=['GET'])
def home():
    return render_template("index.html")

@app.route("/predict", methods=['GET','POST'])
def predict():
    if request.method == "POST":
        # Extracting data from the form
        date = pd.to_datetime(request.form['Date'])
        day = float(date.day)
        month = float(date.month)
        minTemp = float(request.form['min_temp'])
        maxTemp = float(request.form['max_temp'])
        rainfall = float(request.form['Rainfall'])
        humidity = float(request.form['Humidity'])
        location = float(request.form['Location'])
        rainToday = float(request.form['RainToday'])

        # Creating input list for prediction
        input_lst = [location, minTemp, maxTemp, rainfall, humidity, rainToday, month, day]
        
        # Predicting
        pred = model.predict(input_lst)
        
        # Rendering template based on prediction
        if pred == 0:
            return render_template("after_sunny.html")
        else:
            return render_template("after_rainy.html")
    
    return render_template("predictor.html")

if __name__ == '__main__':
    app.run(debug=True)
