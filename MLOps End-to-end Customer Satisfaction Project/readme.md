# MLOps End-to-end Customer Satisfaction Project: Predicting how a customer will feel about a product before they even ordered it

### Problem: 
  For the historical data of a particular customer, we are supposed to predict the rating results for the next order or purchase. We will use the public Brazilian e-commerce dataset from Olist. This dataset contains information about 100,000 orders from 2016 to 2018 placed on different marketplaces in Brazil. Its features allow looking at charges in different dimensions: from order status, price, payment, freight performance to customer location, product attributes and finally written customer reviews. The goal is to predict customer satisfaction for a given order based on attributes such as order status, price, payment, etc. To accomplish this in a real-world scenario, we will use ZenML to create a production-ready pipeline for predicting customer satisfaction for the next order or purchase.

  The purpose of this repository is to show you how you can use ZenML to create machine learning pipelines and use them in a variety of ways:

* By providing a framework and template on which you can build your own work.
* By integrating with tools like MLflow for deployment, tracking, and more.
* You can easily create and deploy your machine learning pipelines.

### Solution:
  To build a real-world workflow for predicting customer satisfaction for the next order or purchase (leading to better decisions), it's not enough to train the model just once.

  Instead, we build an end-to-end pipeline for continuous prediction and deployment of the machine learning model, along with a data application that leverages the most recently deployed model for enterprise use.

  This pipeline can be deployed in the cloud and scaled to meet our needs, ensuring that we track the parameters and data flowing through each ongoing pipeline. This includes raw data input, features, results, the machine learning model and model parameters, and prediction results. ZenML helps us create such a pipeline in a simple but powerful way.

  In this project, we pay special attention to the MLflow integration of ZenML. In particular, we use MLflow Tracking to track our metrics and parameters, and MLflow Deployment to deploy our model. We also use Streamlit to show how this model is deployed in a real-world environment.
