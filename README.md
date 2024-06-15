# Cuisine Classification and Food Freshness Detection

## Overview
The objective of this project is to automate the process of food item classification and freshness detection using machine learning. This device helps in monitoring food items in a refrigerator, predicting their expiry dates, and setting reminders for users.

We attempt to create a low-cost device that can be easily attached to a refrigerator and can keep track of food items inside it. It uses Machine Learning to identify a particular food item and predicts an expiry date for the same. This information is then used to remind the user about a food item that is about to expire so that it can be consumed, making sure it does not go to waste, thereby saving money for the user as well. The project uses concepts of artificial intelligence, internet of things and internet and web programming to achieve its goal. 

The device consists of a Raspberry PI, connected to a camera, which clicks the picture of the food item and sends the data to the server (Amazon EC2). Here, classification is done, and the expiry date is predicted. This information is then relayed to the end point client via a web app which functions as a to-do list.

## Features
- **Cuisine Classification**: Utilizes a convolutional neural network (CNN) model to classify the cuisine of food items.
- **Food Freshness Detection**: Predicts the expiry date of food items and sets reminders for the user.
- **Web Application**: A user-friendly web interface to display food items and their expiry dates.
- **Automated Data Retrieval**: Automates the process of retrieving data from utility portals.
- **End-to-End Project Development**: From data collection and preprocessing to model training and deployment.
- **Data Quality Improvement**: Techniques to ensure high-quality data for reliable model predictions.

## Skills and Topics Covered
- **Machine Learning**: Building and training convolutional neural network (CNN) models.
- **Data Preprocessing**: Techniques for cleaning and preparing data for machine learning.
- **Python Programming**: Writing scripts and Jupyter notebooks.
- **Web Development**: Creating a web application interface using Flask (or any other framework you used).
- **Data Visualization**: Creating dashboards and visualizations for data analysis.

## Results
- Achieved a training accuracy of 79% and a validation accuracy of 60% in cuisine classification using the CNN model.
- Improved manual data collection efficiency by 65%.
