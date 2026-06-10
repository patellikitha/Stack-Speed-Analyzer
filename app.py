
from flask import Flask, render_template, request, redirect, url_for
from collections import deque
import time

app = Flask(__name__)

# Queue -> Customers waiting to book tickets
booking_queue = deque()

# Stack -> Issued tickets
ticket_stack = []

last_operation = "🎬 Welcome to Movie Ticket Booking System!"


@app.route("/")
def home():
    return render_template(
        "index.html",
        queue=list(booking_queue),
        stack=list(reversed(ticket_stack)),
        operation=last_operation
    )


# -------------------- QUEUE --------------------

@app.route("/enqueue", methods=["POST"])
def enqueue():
    global last_operation

    customer = request.form.get("customer")

    if customer:
        start = time.perf_counter()
        booking_queue.append(customer)
        end = time.perf_counter()

        elapsed = (end - start) * 1_000_000

        last_operation = (
            f"🍿 <b>{customer}</b> joined the booking queue.<br>"
            f"⏱️ Enqueue Time: {elapsed:.4f} microseconds"
        )
    else:
        last_operation = "❌ Please enter a customer name."

    return redirect(url_for("home"))


@app.route("/dequeue")
def dequeue():
    global last_operation

    if booking_queue:
        start = time.perf_counter()
        customer = booking_queue.popleft()
        end = time.perf_counter()

        elapsed = (end - start) * 1_000_000

        last_operation = (
            f"🎟️ Ticket booked for <b>{customer}</b>.<br>"
            f"⏱️ Dequeue Time: {elapsed:.4f} microseconds"
        )
    else:
        last_operation = "🚫 Booking queue is empty."

    return redirect(url_for("home"))


# -------------------- STACK --------------------

@app.route("/push", methods=["POST"])
def push():
    global last_operation

    ticket = request.form.get("ticket")

    if ticket:
        start = time.perf_counter()
        ticket_stack.append(ticket)
        end = time.perf_counter()

        elapsed = (end - start) * 1_000_000

        last_operation = (
            f"🎫 Ticket <b>{ticket}</b> added to the stack.<br>"
            f"⏱️ Push Time: {elapsed:.4f} microseconds"
        )
    else:
        last_operation = "❌ Please enter a ticket ID."

    return redirect(url_for("home"))


@app.route("/pop")
def pop():
    global last_operation

    if ticket_stack:
        start = time.perf_counter()
        ticket = ticket_stack.pop()
        end = time.perf_counter()

        elapsed = (end - start) * 1_000_000

        last_operation = (
            f"❌ Ticket <b>{ticket}</b> removed from the stack.<br>"
            f"⏱️ Pop Time: {elapsed:.4f} microseconds"
        )
    else:
        last_operation = "🚫 Ticket stack is empty."

    return redirect(url_for("home"))


if __name__ == "__main__":
    app.run(debug=True)

