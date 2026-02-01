import pandas as pd
import numpy as np

class RealityBacktester:
    def __init__(self, fee=0.001, slippage_std=0.0005):
        self.fee = fee # 0.1% commission
        self.slippage_std = slippage_std # Std dev of price slippage

    def run(self, df):
        balance = 1000.0
        shares = 0
        in_position = False
        
        print(f"--- Starting Realistic Backtest (Fee: {self.fee*100}%) ---")

        for i in range(1, len(df)):
            price = df['close'].iloc[i]
            signal = df['signal'].iloc[i-1] # Use yesterday's signal for today

            # Logic: Simple Buy/Sell based on existing signals in CSV
            if signal == 'BULLISH' and not in_position:
                # Add Slippage to the Buy Price (Pay more)
                slippage = np.random.normal(0, self.slippage_std) * price
                execution_price = price + abs(slippage)
                
                # Apply Fee
                cost = balance * self.fee
                balance -= cost
                
                shares = balance / execution_price
                balance = 0
                in_position = True
                print(f"BUY at ${execution_price:,.2f} | Fee Paid: ${cost:.2f}")

            elif signal == 'BEARISH' and in_position:
                # Subtract Slippage from the Sell Price (Receive less)
                slippage = np.random.normal(0, self.slippage_std) * price
                execution_price = price - abs(slippage)
                
                balance = shares * execution_price
                
                # Apply Fee
                cost = balance * self.fee
                balance -= cost
                
                shares = 0
                in_position = False
                print(f"SELL at ${execution_price:,.2f} | Final Balance: ${balance:,.2f}")

        return balance

# --- Simulation ---
df = pd.read_csv('btc_history.csv')
# Ensure you have the 'signal' column from Day 2/3
tester = RealityBacktester()
final_wallet = tester.run(df)
print(f"\nREALISTIC FINAL BALANCE: ${final_wallet:,.2f}")