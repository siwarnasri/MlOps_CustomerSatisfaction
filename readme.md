### What is ZenML?
ZenML is an extensible, open source MLOps framework for building production-ready ML pipelines. Designed for data scientists, it has a simple, flexible syntax, is cloud and tool agnostic, and has interfaces/abstractions geared towards ML workflows.

# [1. MLOps Notebooks](https://github.com/siwarnasri/MlOps_CustomerSatisfaction/tree/main/MLOps%20Notebooks)

This folder contains a series of short practical MLOps notebooks about ZenML and its various integrations. It is intended for people who want to learn about MLOps in general, as well as ML practitioners who want to get started with ZenML.

### Objective

* Define an MLOps stack tailored to your project requirements.
* Create seamless, repeatable data-centric ML pipelines with automated artifact versioning, tracking, caching, and more.
* Deploy ML pipelines using the tools and infrastructure of your choice (e.g., as a serverless microservice in the cloud).
* Monitor and troubleshoot production issues, such as training data bias and data drift.
* Use some of the most popular MLOps tools such as ZenML, MLflow, Weights & Biases and many others.

### Steps
The folder is divided into several notebooks :

| 1. ML Pipelines	| 2. Training / Serving	| 3. Data Management	|
|---------------- | ----------------------| --------------------|
| 1.1 ML Pipelines| 2.1 Experiment Tracking|	3.1 Data Skew|
| 1.2 Artifact Lifecycle| 2.2 Local Deployment| |		
| | 2.3 Inference Pipelines| |	

# [2. MLOps End-to-end Customer Satisfaction Project](https://github.com/siwarnasri/MlOps_CustomerSatisfaction/tree/main/MLOps%20End-to-end%20Customer%20Satisfaction%20Project)

### Problem
For the historical data of a particular customer, we are supposed to predict the rating results for the next order or purchase. We will use the public Brazilian e-commerce dataset from Olist. This dataset contains information about 100,000 orders from 2016 to 2018 placed on different marketplaces in Brazil. Its features allow looking at charges in different dimensions: from order status, price, payment, freight performance to customer location, product attributes and finally written customer reviews. The goal is to predict customer satisfaction for a given order based on attributes such as order status, price, payment, etc. To accomplish this in a real-world scenario, we will use ZenML to create a production-ready pipeline for predicting customer satisfaction for the next order or purchase.

The purpose of this repository is to show you how you can use ZenML to create machine learning pipelines and use them in a variety of ways:

By providing a framework and template on which you can build your own work.
By integrating with tools like MLflow for deployment, tracking, and more.
You can easily create and deploy your machine learning pipelines.

### Solution
To build a real-world workflow for predicting customer satisfaction for the next order or purchase (leading to better decisions), it's not enough to train the model just once.

Instead, we build an end-to-end pipeline for continuous prediction and deployment of the machine learning model, along with a data application that leverages the most recently deployed model for enterprise use.

This pipeline can be deployed in the cloud and scaled to meet our needs, ensuring that we track the parameters and data flowing through each ongoing pipeline. This includes raw data input, features, results, the machine learning model and model parameters, and prediction results. ZenML helps us create such a pipeline in a simple but powerful way.

In this project, we pay special attention to the MLflow integration of ZenML. In particular, we use MLflow Tracking to track our metrics and parameters, and MLflow Deployment to deploy our model. We also use Streamlit to show how this model is deployed in a real-world environment.
