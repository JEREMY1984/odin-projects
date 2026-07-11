#Simulated messy data coming from an internet api
messy_api_response = {
    "token" : "litecoin",
    "raw_price": "285number", #Notice this is a (string), not a number!
    "daily_volume": "45,000,000"

}

print("🔄Starting data processing pipeline...")

try:
    #this tries to turn text into real decimal number
    clean_price = float(messy_api_response["raw_price"])
    print(f"Clean price is : {clean_price}")


except Exception as error_message:
    #if python fails above , it jump straight here
    print(f"❌An error occurred: {error_message}")

print("🚀Script finished completely without crashing!")