import requests
from requests.exceptions import RequestException


def fetch_via_tor(url):
    # Tor's default SOCKS5 proxy is at 127.0.0.1:9050
    proxies = {
        'http': 'socks5h://127.0.0.1:9050',
        'https': 'socks5h://127.0.0.1:9050'
    }

    try:
        response = requests.get(url, proxies=proxies, timeout=10)
        response.raise_for_status()  # Raise an exception for HTTP errors
        return response.text
    except RequestException as e:
        print(f"An error occurred: {e}")
        return None


if __name__ == '__main__':
    # This endpoint will return your IP address as seen by the server.
    url = 'https://httpbin.org/ip'
    result = fetch_via_tor(url)
    if result:
        print("Response from httpbin.org:")
        print(result)
    else:
        print("Failed to fetch the URL via Tor.")
