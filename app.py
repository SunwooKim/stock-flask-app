from flask import Flask, request, render_template
from stock_crawler import get_stock_price_by_name

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    if request.method == "POST":
        stock_name = request.form["stock_name"]
        result = get_stock_price_by_name(stock_name)
    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)