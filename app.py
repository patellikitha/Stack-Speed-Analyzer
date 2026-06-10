
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


# ---------------- QUEUE ----------------

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


@app.route("/dequeue")
def dequeue():
    global last_operation

    if booking_queue:
        customer = booking_queue.popleft()
        last_operation = f"Ticket booked for {customer}."
    else:
        last_operation = "Booking queue is empty."

    return redirect(url_for("home"))


# ---------------- STACK ----------------

@app.route("/push", methods=["POST"])
def push():
    global last_operation

    ticket = request.form.get("ticket")

    if ticket:
        ticket_stack.append(ticket)
        last_operation = f"Ticket {ticket} added to the stack."
    else:
        last_operation = "Please enter a ticket ID."

    return redirect(url_for("home"))


@app.route("/pop")
def pop():
    global last_operation

    if ticket_stack:
        ticket = ticket_stack.pop()
        last_operation = f"Ticket {ticket} removed from the stack."
    else:
        last_operation = "Ticket stack is empty."

    return redirect(url_for("home"))


if __name__ == "__main__":
    app.run(debug=True)

