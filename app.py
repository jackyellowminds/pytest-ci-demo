from flask import Flask, request, jsonify

from calculator import add, subtract, multiply, divide


app = Flask(__name__)


@app.route("/")
def home():
    return jsonify({
        "service": "Calculator Microservice",
        "status": "running"
    })


@app.route("/add")
def add_numbers():
    a = float(request.args.get("a"))
    b = float(request.args.get("b"))

    return jsonify({
        "operation": "add",
        "a": a,
        "b": b,
        "result": add(a, b)
    })


@app.route("/subtract")
def subtract_numbers():
    a = float(request.args.get("a"))
    b = float(request.args.get("b"))

    return jsonify({
        "operation": "subtract",
        "a": a,
        "b": b,
        "result": subtract(a, b)
    })


@app.route("/multiply")
def multiply_numbers():
    a = float(request.args.get("a"))
    b = float(request.args.get("b"))

    return jsonify({
        "operation": "multiply",
        "a": a,
        "b": b,
        "result": multiply(a, b)
    })


@app.route("/divide")
def divide_numbers():
    a = float(request.args.get("a"))
    b = float(request.args.get("b"))

    try:
        result = divide(a, b)

        return jsonify({
            "operation": "divide",
            "a": a,
            "b": b,
            "result": result
        })

    except ValueError as e:
        return jsonify({
            "error": str(e)
        }), 400


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)