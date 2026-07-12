import time # this allow us to pause the time

# our target buying price
target_buy_price = 70.00

#1. Real-world structured data using Dictionaries inside a List
simulated_market_data = [
    {'ticker': 'LTC', 'day': 1, 'price' : 75.50},
    {'ticker':'LTC', 'day': 2, 'price' : 72.10},
    {'ticker': 'LTC' , 'day' : 3, 'price': 68.50},
    {'ticker': 'LTC', 'day': 4, 'price' : 'corrupted data'}, # corrupted data
    {'ticker':'LTC', 'day': 5, 'price' : 69.20},
  
]

print(f'starting the advance structured accumulation bot...\n')

#2. the loop
for market_snapshot in simulated_market_data:
    #market_snapshot represents one whole dictionary {} in the list
    try:
        #pulling out specific data by using their 'key' labels
        current_price = float(market_snapshot["price"])
        coin_name = market_snapshot['ticker']
        day_num = market_snapshot['day']

        print(f'Day {day_num}:Checking {coin_name}...')

        if current_price <= target_buy_price:
            print(f'{coin_name} dropped to {current_price}! Executing order.')
        else:
            print(f'{coin_name} is {current_price}. Holding position.')

    except Exception as e:
        #if any dictionary has broken data, grab the day number if possible
        day_num = market_snapshot.get('day','unknown')
        print (f'Alert on Day {day_num}: Could not process market data. Error: {e}')

    print('-' * 50)
    time.sleep(2)

print ('Simulation completed')
