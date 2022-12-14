#import modules
import requests, re
from pathlib import Path
import json

# Start of a function
def api_function():
    function = 'CURRENCY_EXCHANGE_RATE'
    from_currency = 'USD'
    to_currency = 'SGD'
    api_key = 'TYRNR04ZRXIKTHMK'
    base_url = 'https://www.alphavantage.co'
    main_url = base_url+'/query?function='+function+'&from_currency='+from_currency+'&to_currency='+to_currency+'&apikey='+api_key
    response = requests.get(main_url).json()

    # Create a for loop to get the itms in response
    for item in response:
        # write out functions to get necessary data
        function = float(response[item]["5. Exchange Rate"])
        from_currency = response[item]["1. From_Currency Code"]
        to_currency = response[item]["3. To_Currency Code"]


    file_path = Path.cwd()/"summary_report.txt"
    # open text file and write real time conversion rate
    with file_path.open(mode="w", encoding="UTF-8", newline="") as file:
        file.write("[REAL TIME CURRENCY CONVERSION RATE]" " " f"{from_currency}1 = {to_currency}{function}")

print(api_function())
