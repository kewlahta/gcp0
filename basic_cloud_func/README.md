# basic_cloud_func
## Description
This app is a template for the essentials needed to create a GCP cloud function using Python. 

The app comes with a built-in testing environment for a cloud function triggered by an HTTP request. 

## Disclaimer ##
The auth mechanism used in this function template is for demonstration purposes only. Use this at your own risk. The API_KEY environment variable should not be explicitly set in the code, GIT actions, or anywhere else in plaintext. At a minimum, the value should be placed in GCP secret manager and injected via the gcloud cli function deployment, or other secret vault connected to your CICD pipeline. 

## Running locally
Docker is required to run the testing environment. When running on Windows, it's recommended to use Docker hosted in a WSL setup. Execute the local_run script to setup and start the flask environment.

`$ ./local_run.sh`

The local environment, by default, will create an http endpoint running on port 8080. The port value can be changed in the local_run.sh script if there are already conflicting services running on 8080. If no port is provided, flask's default port of 5000 will be used. 

In this template, the http endpoint will accept either a GET or POST request. The auth key must be passed to the endpoint as either a url parameter or in the root of the json payload as the key-value pair "API_KEY:changeme". This value is checked against a environment variable of the same name. The function will return a blank response with a 401 status code if no key is provided, or if the key does not match. To change the acceptable api key, edit the API_KEY environment variable set in the Dockerfile build file. 

Invoking the function in the local environment via POST:

`curl -XPOST -H "Content-Type: application/json" -d "{\"API_KEY\": \"<key value>\" }" localhost:<port>`

via GET:

`curl -XGET localhost:<port>/?API_KEY=<key value>`

A successful request yields the result:

`{"messsage": "Success"}`

## Opportunities for improvement ###
- Templates for handling GCP service account handling/authorization
- Templates for interacting with various GCP services
  - Spanner
  - BQ
  - Pubsub
- Cloud function custom logger