from flask import Flask, render_template
import Quote

app = Flask(__name__)


@app.route("/")
def index():
    quote = Quote.getQuote()
    return render_template('index.html', title="Quote", quote=quote['content'], author=quote['author'])


if __name__ == "__main__":
    app.run()
