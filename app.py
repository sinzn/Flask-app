from flask import Flask, jsonify
from datetime import datetime

app = Flask(__name__)

# Home route
@app.route("/")
def home():
    return "Hello, World!"

# Status route
@app.route("/status")
def status():
    return jsonify({"status": "Server is up and running!"})

# Datetime route
@app.route("/datetime")
def current_datetime():
    now = datetime.now()
    formatted_datetime = now.strftime("%Y-%m-%d %H:%M:%S")
    return jsonify({"current_datetime": formatted_datetime})

# Main check
if __name__ == "__main__":
    # Run the app with debug and make it accessible on any IP
    app.run(debug=True, host="0.0.0.0")

