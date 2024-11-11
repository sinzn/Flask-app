# Flask App

This is a simple Flask application that can be containerized with Docker. The app includes routes to check the server's status and fetch the current date and time.

## Running the App

### Build the Docker image

To build the Docker image, use the following command:

```bash
docker build -t flask-app .
```

Run the Docker container
Run the Docker container with this command:

```bash
docker run -p 5000:5000 flask-app
```
This will start the Flask app and map it to port 5000 on your local machine.

Access the Routes
Once the app is running, you can access the following routes:

* Home: http://localhost:5000/ </br>
* Status: http://localhost:5000/status - Checks if the server is up and running. </br>
* Current DateTime: http://localhost:5000/datetime - Fetches the current date and time. </br>
* These routes should give you a working application with additional endpoints to verify the server’s status and retrieve the current date and time. </br>
