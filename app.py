from flask import Flask, request


app = Flask(__name__)  # Standard Flask app


@app.route("/", methods=['GET', 'POST'])        # Standard Flask endpoint
def hello_world():
    data = request.get_json()
    print(data)
    return "Hello, World!"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8085)
