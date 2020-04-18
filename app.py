from flask import Flask, render_template, jsonify
import Quote

app = Flask(__name__)


@app.route("/")
def index():
    return render_template('index.html', title="Quote")


@app.route('/quote', methods=['POST', 'GET'])
def quote():
    quot = Quote.getQuote()
    print("called")
    return jsonify({"quote": quot['content'], "author": quot['author']})


if __name__ == "__main__":
    app.run()
