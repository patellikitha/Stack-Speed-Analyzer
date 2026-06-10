
from flask import Flask, render_template, request, redirect, url_for
from collections import deque

app = Flask(__name__)

# Queue and Stack
booking_queue = deque()
ticket_stack = []

# Latest operation message
last_operation = "Welcome to the Movie Ticket Booking System!"


@app.route("/")
def home():
    return render_template(
        "index.html",
        queue=list(booking_queue),
        stack=list(reversed(ticket_stack)),
        operation=last_operation
    )


# Enqueue customer
@app.route("/enqueue", methods=["POST"])
def enqueue():
    global last_operation

    customer = request.form.get("customer")

    if customer:
        booking_queue.append(customer)
        last_operation = f"{customer} joined the booking queue."
    else:
        last_operation = "Please enter a customer name."

    return redirect(url_for("home"))


# Dequeue customer
@app.route("/dequeue")
def dequeue():
    global last_operation

    if booking_queue:
        customer = booking_queue.popleft()
        last_operation = f"Ticket booked for {customer}."
    else:
        last_operation = "Booking queue is empty."

    return redirect(url_for("home"))


if __name__ == "__main__":
    app.run(debug=True)

