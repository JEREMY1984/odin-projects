import requests
import time
from datetime import datetime

watch_list = ["bitcoin", "ethereum", "litecoin", "polkadot", "polygon-ecosystem-token", "ankr"]

print("🚀 Starting automated crypto tracker pipeline... Press Ctrl + C to stop.")

# This creates an infinite loop to keep running the script automatically
while True:
    print(f"\n🛰️ Fetching live data at {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}...")
    
    try:
        url = f"https://api.coingecko.com/api/v3/simple/price?ids={','.join(watch_list)}&vs_currencies=myr"
        response = requests.get(url)
        data = response.json()
        
        # Open a text file in 'append' mode ('a') so it adds new data to the bottom without erasing old data
        with open("crypto_log.txt", "a", encoding="utf-8") as file:
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            file.write(f"\n--- REPORT TIME: {timestamp} ---\n")
            
            print("\n📊 --- LIVE MARKET REPORT (MYR) ---")
            
            for token in watch_list:
                token_data = data.get(token, {})
                price = token_data.get("myr", 0)
                
                if price > 50:
                    status = "🔥 High-Value Asset"
                else:
                    status = "💎 Accumulation Zone"
                
                # Format the text line
                output_line = f"Token: {token.capitalize():<10} | Price: RM {price:<10,.2f} | Strategy: {status}"
                
                # Print to your screen
                print(output_line)
                # Save to your text file
                file.write(output_line + "\n")
                
            file.write("-------------------------------------\n")
            print("✅ Screen and file update complete.")
            
    except Exception as e:
        print(f"❌ Error fetching data: {e}")
        
    # Wait for 10 seconds before looping again
    print("⏳ Waiting 10 seconds for next check...")
    time.sleep(10)