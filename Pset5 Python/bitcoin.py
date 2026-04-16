import sys
import requests

def main():
    # Check command-line argument count
    if len(sys.argv) != 2:
        sys.exit("Missing command-line argument")

    # Try to convert argument to float
    try:
        bitcoins = float(sys.argv[1])
    except ValueError:
        sys.exit("Command-line argument is not a number")

    # CoinCap API v3 endpoint with your API key
    # Replace "YourApiKey" with the actual API key from your CoinCap dashboard
    api_key = "YourApiKey"   # <-- CHANGE THIS TO YOUR REAL API KEY
    url = f"https://rest.coincap.io/v3/assets/bitcoin?apiKey={api_key}"

    # Fetch current Bitcoin price
    try:
        response = requests.get(url)
        response.raise_for_status()          # Raise exception for HTTP errors
        data = response.json()
        # Extract price from the nested JSON structure
        price_usd = float(data["data"]["priceUsd"])
    except (requests.RequestException, KeyError, ValueError, TypeError):
        sys.exit("Unable to fetch Bitcoin price")

    # Calculate total cost
    total = bitcoins * price_usd

    # Output with commas, 4 decimal places, and dollar sign
    print(f"${total:,.4f}")

if __name__ == "__main__":
    main()
