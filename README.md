# Predicting prices of used Honda Civic vehicle in Alberta, Canada.
This model predicts used car prices for web-scrapped data acquired from an online (Kijiji.ca) advertising website.

I will be updating this file as I move on with this project.

## Project Goal 
Sellers and buyers of used cars want to know the cost to help maximize profit and reduce expenditure, as the case may be. This interactive web model can be used to give such price estimates based on the four most common features that drive the prices of vehicles. 

## Steps

The project involves five stages:

•	Scaping web data and performing initial cleaning.

•	Importing and cleaning the data in pandas.

•	Creating a Model for the prediction of prices for a potential buyer or seller of Honda civic model.

•	Built the flask server API.

•	Built a Simple web application that ingest features provided by users and return estimated price output.


<h1>Overview</h1>

![image](https://user-images.githubusercontent.com/71553115/236508885-b0ea359e-dd22-4328-b2e8-1f4e665cb18a.png)

Figure 1: Project Process Overview

### The four input features include:

·        Distance covered by the vehicle in kilometers (“Odo”)

·        Year

·        Transmission

·        Location of sales

The target output will be the price. The web application will require the four features, and the estimated cost will be returned. 


![image](https://github.com/Ola-20/auto_model/assets/71553115/82e3ff6d-9aba-422d-80c9-afd7ab884c3c)

Figure 2: Web User Interface; Before and after clicking Estimate Price.

## Description

·       The server folder contains the code that used the predictor model built and exported from the jupyter-notebook to predict a price output based on the required input features.

·       The client folder contains HTML, CSS, and JS files that were used to create a simple web interface for both input and output.

·       The model folder contains the actual model, exported from the jupyter-notebook as a pickle file.

·       Sample_scrape.py contains the code used to acquire data from the web

 
