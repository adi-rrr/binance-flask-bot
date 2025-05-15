````markdown
# 🧠 Binance Testnet Trading Bot (Flask UI)

This is a simplified **crypto trading bot** I built for the Binance **USDT-M Futures Testnet**. It allows placing market, limit, and stop-limit orders using a clean Flask-based web interface.

> 🔐 All trades are simulated on Binance's Testnet — no real money is involved.
---
Short walkthrough : (https://drive.google.com/file/d/1ZVVviIswth1pZeuWerc4vXrlgzl8fE-J/view?usp=sharing)
---

## 🚀 Features

- ✅ Place **Market**, **Limit**, and **Stop-Limit** orders
- ✅ Support for **Buy** and **Sell** sides
- ✅ Basic **form validation** (e.g., for stop price logic)
- ✅ Logs all API requests and errors
- ✅ Flask-based UI with clean, minimal UX
- ✅ API keys loaded securely from `.env`
- ✅ Works exclusively with the **Binance Futures Testnet**

---

## 📸 UI Preview

📎 [Include screenshots or a Loom walkthrough here]  
👉 Walkthrough: **[Insert your walkthrough video link here]**

---

## ⚙️ Tech Stack

- Python 3.x  
- Flask  
- `python-binance`  
- Bootstrap (via CDN)  
- Logging + `.env` for secrets

---

## 🧑‍💻 How to Run It

### 1. Clone the Repository

```bash
git clone https://github.com/YOUR_USERNAME/binance-flask-bot.git
cd binance-flask-bot
````

### 2. Create `.env` File

```ini
API_KEY=your_testnet_api_key
API_SECRET=your_testnet_api_secret
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the App

```bash
python app.py
```

Visit `http://127.0.0.1:5000` in your browser.

---

## 📒 Order Types Explained

| Order Type | When to Use                                        |
| ---------- | -------------------------------------------------- |
| Market     | Execute immediately at current market price        |
| Limit      | Execute at your set price or better                |
| Stop-Limit | Trigger a limit order only after a stop price hits |

---

## 🧪 Testnet Setup

1. Register at: [Binance Futures Testnet](https://testnet.binancefuture.com)
2. Generate API key and secret
3. Enable trading permissions
4. Add keys to your `.env` file

---

## 📦 Future Features (WIP)

* [ ] Add OCO or Grid orders
* [ ] Historical order table
* [ ] Auth system for multiple users
* [ ] Deployable UI (Heroku, Railway, etc.)

---

## 🧠 Credits

Built with ❤️ and curiosity.
If you find bugs or want to contribute — feel free to open issues or PRs.

---

