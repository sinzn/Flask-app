
# Flask-app

## Running the App
Build the Docker image:

## For docker run 
docker build -t flask-app .

## Run the Docker container:
docker run -p 5000:5000 flask-app

Access the routes /
Home: http://localhost:5000/
Status: http://localhost:5000/status
Current DateTime: http://localhost:5000/datetime

This should give you a working application with additional routes to verify the server’s status and get the current date and time.
