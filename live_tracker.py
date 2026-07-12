import time
import requests

# We are switching to CryptoCompare's stable public API endpoint
url = "https://min-api.cryptocompare.com/data/pricemultifull?fsyms=POL,DOT&tsyms=MYR"

print("📊 Switching to CryptoCompare Engine...")
print("📝 Recording live prices to 'market_log.txt' every 10 seconds. Press Ctrl + C to stop.\n")

while True:
    try:
        response = requests.get(url)
        live_data = response.json()
        
        # CryptoCompare nests its prices inside a 'RAW' dictionary key
        market_data = live_data.get("RAW", {})
        
        # Safely extract the token data blocks
        pol_data = market_data.get("POL", {}).get("MYR", {})
        dot_data = market_data.get("DOT", {}).get("MYR", {})
        
        # Extract the actual price numbers (using .get to prevent any crashes)
        polygon_price = pol_data.get("PRICE", 0.0)
        dot_price = dot_data.get("PRICE", 0.0)
        
        current_time = time.strftime("%Y-%m-%d %H:%M:%S")
        
        # Format our log entry cleanly
        log_entry = f"[{current_time}] POL: RM {polygon_price:.2f} | DOT: RM {dot_price:.2f}\n"
        
        with open("market_log.txt", "a") as file:
            file.write(log_entry)
            
        print(f"✅ Logged successfully: {log_entry.strip()}")
        
    except Exception as e:
        print(f"❌ Structural Loop Error encountered: {e}")
        
    time.sleep(10)