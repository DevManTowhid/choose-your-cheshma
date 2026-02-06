import os
import cv2
import numpy as np
from flask import Flask, render_template, request, redirect, url_for

# create a Flask App

app = Flask(__name__) # explanation: This line creates an instance of the Flask class, which is the main application object. The __name__ variable is passed to the Flask constructor to help it determine the root path of the application. This is necessary for finding resources and templates.

@app.route('/') # explanation: This line is a decorator that defines a route for the web application. The '/' route corresponds to the home page of the application.

def index():
    return render_template('index.html') # explanation: This line renders the 'index.html' template when the '/index' route is accessed. The render_template function looks for the 'index.html' file in the 'templates' directory of the application.


if __name__ == '__main__':
    app.run(debug=True) # explanation: This line starts the Flask development server. The debug=True argument enables debug mode, which provides detailed error messages and automatically reloads the server when code changes are detected.