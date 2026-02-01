# 🧪 Reality Check Backtester (Fees & Slippage)

A Python-based **realistic backtesting engine** that simulates how trading strategies behave **after accounting for real-world frictions** such as:

- Trading fees
- Slippage
- Execution delay

This project answers a critical question:
> *Does my strategy still work once reality is included?*

---

## 🚀 What This Project Does

- Replays historical trades using pre-generated signals
- Applies **transaction fees** on every buy & sell
- Simulates **price slippage** using a random distribution
- Uses realistic execution prices instead of ideal closes
- Outputs the **true final portfolio balance**

---

## 🧠 Why This Matters

Many strategies look profitable on paper but fail in practice because they ignore:
- Fees
- Slippage
- Execution assumptions

This backtester exposes that gap.

---

## ⚙️ Backtesting Logic

### 🔹 Inputs
- Historical BTC price data
- Precomputed trading signals (`BULLISH`, `BEARISH`)

### 🔹 Execution Rules
- **BUY** → Pay higher price due to slippage
- **SELL** → Receive lower price due to slippage
- **Fee applied on every trade** (default: 0.1%)
- Uses **previous day’s signal** to avoid look-ahead bias

---

## 🧮 Parameters

- fee = 0.001
- slippage_std = 0.0005
- Both can be tuned to simulate different market conditions.

---

## 📦 Installation

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/PranavVetkar/Reality-Check-Backtester.git
cd Reality-Check-Backtester
