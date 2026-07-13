import os
import time
import requests

# Target limits
TARGETS = {
    "polygon-ecosystem-token": 1.60,  # POL
    "polkadot": 19.00                 # DOT
}

# Display name mapping for clean terminal and CSV files
DISPLAY_NAMES = {
    "polygon-ecosystem-token": "POL",
    "polkadot": "DOT"
}

csv_filename = "crypto_portfolio_log.csv"

print("🚀 Launching CoinGecko CSV Price Monitor Engine...")

# Create the CSV file and write headers ONLY if the file doesn't exist yet
if not os.path.exists(csv_filename):
    with open(csv_filename, "w") as file:
        file.write("Timestamp,Ticker,Current_Price_RM,Target_Price_RM,Signal\n")
    print(f"📁 Created brand new spreadsheet file: {csv_filename}")

# The live loop tracking engine
while True:
    try:
        url = "https://api.coingecko.com/api/v3/simple/price"
        
        # FIX: Added the dot before the join method here!
        params = {
            "ids": ",".join(TARGETS.keys()),
            "vs_currencies": "myr"
        }
        
        response = requests.get(url, params=params)
        
        if response.status_code == 200:
            live_data = response.json()
            current_time = time.strftime("%Y-%m-%d %H:%M:%S")
            
            # Loop through our tracked tokens to evaluate thresholds and write rows
            for token_id, target_price in TARGETS.items():
                current_price = live_data.get(token_id, {}).get("myr", 0.0)
                display_name = DISPLAY_NAMES.get(token_id, token_id.upper()[:3])
                
                # Evaluate signal thresholds (ignoring a glitchy 0.0 value)
                if current_price <= target_price and current_price > 0:
                    signal = "BUY ALERT"
                    print(f"🔥 ALERT: {display_name} is at RM {current_price:.2f}! Below target of RM {target_price:.2f}")
                else:
                    signal = "HOLD"
                    print(f"⏳ {display_name}: RM {current_price:.2f} (Target: RM {target_price:.2f})")
                
                # Write individual row details cleanly to the CSV spreadsheet
                with open(csv_filename, "a") as file:
                    file.write(f"{current_time},{display_name},{current_price:.2f},{target_price:.2f},{signal}\n")
            
            print("💾 Spreadsheet updated successfully.\n" + "-"*40)
            
        else:
            print(f"⚠️ API Server busy or returned status code: {response.status_code}")
            
    except Exception as e:
        print(f"❌ Network or processing error encountered: {e}")
        
    # Sleep for 10 seconds before checking again
    time.sleep(10)