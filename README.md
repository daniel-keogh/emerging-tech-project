# Emerging Technologies Project

Y4S1 Emerging Technologies Project

## Description

A web service that uses machine learning to predict wind turbine power output from wind speed values defined in the data set [powerproduction.csv](./powerproduction.csv).

## Running the Notebook

The model is created in a Jupyter notebook using Keras, and you can run the notebook by first installing [Anaconda](https://www.anaconda.com/) and then executing the below command from within the repository's root directory.

```sh
$ jupyter notebook
```

## Running the Web Service

The web service consists of a Flask application which serves a simple Vue.js frontend.

### Development Server

To start a development server run the following command and then open `localhost:5000` in a web browser.

```sh
$ python app.py
```

### Docker

You can run the web service in a Docker container by following the steps below.

#### Build Image

```sh
$ docker build -t power-production .
```

#### Run Image

```sh
$ docker run -d -p 5000:5000 power-production
```
