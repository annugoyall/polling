import requests
import time

def short_polling():
    while True:
        # Sending Request to URL
        url = "http://localhost:8080/shortpolling"
        response = requests.get(url)

        # Reading the response
        if response.status_code == 200:
            response_data = response.text.strip()
            if response_data:
                # Process the response from the server
                print("Response from Server:", response_data)

        time.sleep(5)  # Waiting for 5 seconds to make another request

if __name__ == "__main__":
    short_polling()
