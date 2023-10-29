# Python program to get the real-time currency exchange rate
# Import the  required libraries request, json and re

import requests
import json
import re


# Function for getting real time currency exchange rates and converting the amount from source currency to tarhet currency
def RealTimeCurrencyExchangeRate(from_currency, to_currency, con_amount):
    # base_url to get the exchange rates
    base_url = r"https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE"

    # API Key for Alphavantage
    api_key = "6OGO849U0E9MI4FO"

    # full_url construction
    full_url = (
        base_url
        + "&from_currency="
        + from_currency
        + "&to_currency="
        + to_currency
        + "&apikey="
        + api_key
    )

    try:
        # Invoke get method of requests module and return response objects
        req_ob = requests.get(full_url)
        # returns json format in dictionary data type. The result contains list of nested dictionaries
        result = req_ob.json()
        exchange_rate = result["Realtime Currency Exchange Rate"]["5. Exchange Rate"]
        converted_amount = con_amount * float(exchange_rate)
        print(
            f"{con_amount} {from_currency} is equal to {converted_amount} {to_currency} \nConversion rate is: 1 {from_currency} = {exchange_rate} {to_currency}"
        )

    except:
        print("Oops!  Error occured.  Please try again...")


# For running in scripts
if __name__ == "__main__":
    # Get the sourse and target currency codes and amount to be converted
    while True:
        from_currency = input("Please enter the source currency (3 characters): ").upper()

        # Check if the source currency is valid.
        if not re.match(r"^[A-Z]{3}$", from_currency):
            print("Source currency must be a valid 3-character currency code.")
            continue
        break

    while True:
        to_currency = input("Please enter the target currency (3 characters): ").upper()

        # Check if the target currency is 3 valid
        if not re.match(r"^[A-Z]{3}$", to_currency):
            print("Target currency must be a valid 3-character currency code.")
            continue
        break

    while True:
        con_amount = input("Please enter the amount to be converted: ")

        # Check if the Amount is float value.
        try:
            con_amount = float(con_amount)
            break
        except ValueError:
            # The amount is not a valid float value.
            print("Amount input is incorrect. Please enter a valid amount.")

    con_amount = float(con_amount)
    # Call the function to convert the currencies

    RealTimeCurrencyExchangeRate(from_currency, to_currency, con_amount)
