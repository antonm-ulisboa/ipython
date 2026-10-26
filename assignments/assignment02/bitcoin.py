import os
import sys

import requests


def get_quantity():
    # Validate input before requesting the price.
    if len(sys.argv) < 2:
        sys.exit("Missing command-line argument")
    if len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")

    try:
        return float(sys.argv[1])
    except ValueError:
        sys.exit("Command-line argument is not a number")


def get_bitcoin_price():
    # Keep the API key outside the source code.
    api_key = os.environ.get("COINCAP_API_KEY", "").strip()

    try:
        response = requests.get(
            "https://rest.coincap.io/v3/assets/bitcoin",
            params={"apiKey": api_key},
            timeout=10,
        )
        response.raise_for_status()
        data = response.json()
        return float(data["data"]["priceUsd"])
    except requests.RequestException as error:
        if error.response is not None:
            sys.exit(f"CoinCap HTTP error: {error.response.status_code}")
        sys.exit(f"Request error: {type(error).__name__}")
    except (KeyError, ValueError, TypeError):
        sys.exit("Invalid price data")


def main():
    quantity = get_quantity()
    price = get_bitcoin_price()
    print(f"${quantity * price:,.4f}")


if __name__ == "__main__":
    main()
