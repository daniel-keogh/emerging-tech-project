# Emerging Technologies Project

Y4S1 Emerging Technologies Project

## Description

A web service that uses machine learning to predict wind turbine power output from wind speed values defined in the data set [powerproduction.csv](./powerproduction.csv).

## Run a Development Server

To start a development server run the following command and then open `localhost:5000` in a web browser.

```sh
$ python app.py
```

## Docker

### Build Image

```sh
$ docker build -t power-production .
```

### Run Image

```sh
$ docker run -d -p 5000:5000 power-production
```
