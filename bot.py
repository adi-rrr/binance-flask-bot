from flask import Flask, render_template_string, request, flash
from binance.client import Client
from dotenv import load_dotenv
import os
import logging
from datetime import datetime

# Load environment variables
load_dotenv()
API_KEY = os.getenv("API_KEY")
API_SECRET = os.getenv("API_SECRET")

# Configure logging
logging.basicConfig(
    filename='orders.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)


app = Flask(__name__)
app.secret_key = 'supersecretkey'  

class BasicBot:
    def __init__(self, api_key, api_secret, testnet=True):
        self.client = Client(api_key, api_secret)
        if testnet:
            self.client.FUTURES_URL = "https://testnet.binancefuture.com/fapi"

    def place_order(self, symbol, side, order_type, quantity, price=None, stop_price=None):
        try:
            if order_type == "MARKET":
                return self.client.futures_create_order(
                    symbol=symbol,
                    side=side,
                    type="MARKET",
                    quantity=quantity
                )
            elif order_type == "LIMIT":
                return self.client.futures_create_order(
                    symbol=symbol,
                    side=side,
                    type="LIMIT",
                    timeInForce="GTC",
                    quantity=quantity,
                    price=price
                )
            elif order_type == "STOP_LIMIT":
                return self.client.futures_create_order(
                    symbol=symbol,
                    side=side,
                    type="STOP_MARKET",
                    timeInForce="GTC",
                    quantity=quantity,
                    stopPrice=stop_price
                )
            else:
                raise ValueError("Unsupported order type.")
        except Exception as e:
            raise e

bot = BasicBot(API_KEY, API_SECRET)

# HTML Template
HTML_TEMPLATE = '''
<!DOCTYPE html>
<html>
<head>
    <title>Binance Futures Trading Bot</title>
</head>
<body>
    <h2>📈 Binance Futures Trading Bot (Testnet)</h2>
    <form method="POST">
        <label>Symbol:</label><input type="text" name="symbol" required><br><br>
        <label>Side:</label>
        <select name="side">
            <option value="BUY">BUY</option>
            <option value="SELL">SELL</option>
        </select><br><br>
        <label>Order Type:</label>
        <select name="order_type" onchange="toggleFields(this.value)">
            <option value="MARKET">MARKET</option>
            <option value="LIMIT">LIMIT</option>
            <option value="STOP_LIMIT">STOP-LIMIT</option>
        </select><br><br>
        <label>Quantity:</label><input type="text" name="quantity" required><br><br>
        <div id="limitFields" style="display:none;">
            <label>Limit Price:</label><input type="text" name="price"><br><br>
        </div>
        <div id="stopFields" style="display:none;">
            <label>Stop Price:</label><input type="text" name="stop_price"><br><br>
        </div>
        <input type="submit" value="Place Order">
    </form>
    <br>
    {% with messages = get_flashed_messages() %}
      {% if messages %}
        <ul>
        {% for message in messages %}
          <li>{{ message }}</li>
        {% endfor %}
        </ul>
      {% endif %}
    {% endwith %}
    
    <script>
    function toggleFields(value) {
        document.getElementById('limitFields').style.display = (value == 'LIMIT' || value == 'STOP_LIMIT') ? 'block' : 'none';
        document.getElementById('stopFields').style.display = (value == 'STOP_LIMIT') ? 'block' : 'none';
    }
    </script>
</body>
</html>
'''

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        try:
            symbol = request.form["symbol"].upper()
            side = request.form["side"]
            order_type = request.form["order_type"]
            quantity = float(request.form["quantity"])
            price = request.form.get("price")
            stop_price = request.form.get("stop_price")

            # Log order request
            logging.info(f"Placing order: {symbol} {side} {order_type} {quantity} "
                         f"Price={price} StopPrice={stop_price}")

            # Place order
            order = bot.place_order(
                symbol=symbol,
                side=side,
                order_type=order_type,
                quantity=quantity,
                price=float(price) if price else None,
                stop_price=float(stop_price) if stop_price else None
            )

            # Log response
            logging.info(f"Order response: {order}")

            flash(f"✅ Order placed! ID: {order['orderId']}, Status: {order['status']}")
        except Exception as e:
            logging.error(f"❌ Order failed: {e}")
            flash(f"❌ Error: {e}")
    return render_template_string(HTML_TEMPLATE)

if __name__ == "__main__":
    app.run(debug=True,port=5000)
