
# app.py

from flask import Flask

# Create the Flask application
app = Flask(__name__)

# Basic home route
@app.route("/")
def home():
    return """
    <h1>🎬 Movie Ticket Booking System</h1>
    <p>Flask application initialized successfully!</p>
    """


# Run the application
if __name__ == "__main__":
    app.run(debug=True)

