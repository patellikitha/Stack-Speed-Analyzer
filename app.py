
# app.py

from flask import Flask, render_template
from collections import deque

app = Flask(__name__)

# Data structures
booking_queue = deque()
ticket_stack = []

# Message to display on the home page
last_operation = "🎬 Welcome to Movie Ticket Booking System!"


@app.route("/")
def home():
    return render_template(
        "index.html",
        queue=list(booking_queue),
        stack=list(reversed(ticket_stack)),
        operation=last_operation
    )


if __name__ == "__main__":
    app.run(debug=True)

