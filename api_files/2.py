import requests

def run(phone_number):
    """
    Function to handle the OTP resend API logic for Xylem.

    :param phone_number: The phone number to target.
    """
    try:
        # API URL
        url = "https://xylem-api.penpencil.co/v1/users/resend-otp?smsType=1"

        # Payload
        payload = {
            "mobile": phone_number,
            "organizationId": "64254d66be2a390018e6d348"
        }

        # Headers
        headers = {
            "content-length": str(len(str(payload))),
            "sec-ch-ua-platform": "\"Android\"",
            "authorization": "Bearer",  # Add the actual bearer token here
            "randomid": "f5c08b76-4093-4ca6-a6e6-d2654fa18670",
            "sec-ch-ua": "\"Chromium\";v=\"130\", \"Android WebView\";v=\"130\", \"Not?A_Brand\";v=\"99\"",
            "sec-ch-ua-mobile": "?1",
            "client-type": "WEB",
            "client-id": "64254d66be2a390018e6d348",
            "user-agent": "Mozilla/5.0 (Linux; Android 14; SM-S928B Build/UP1A.231005.007; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/130.0.6723.107 Mobile Safari/537.36",
            "accept": "application/json, text/plain, */*",
            "content-type": "application/json",
            "client-version": "300",
            "origin": "https://www.xylem.live",
            "x-requested-with": "pure.lite.browser",
            "sec-fetch-site": "cross-site",
            "sec-fetch-mode": "cors",
            "sec-fetch-dest": "empty",
            "referer": "https://www.xylem.live/",
            "accept-encoding": "gzip, deflate, br, zstd",
            "accept-language": "en-IN,en-US;q=0.9,en;q=0.8",
            "priority": "u=1, i"
        }

        # Sending the POST request
        response = requests.post(url, json=payload, headers=headers)

        # Handling the response
        if response.status_code == 200:
            print(f"OTP resend request successful for {phone_number}")
            print(f"Response: {response.json()}")
        else:
            print(f"Failed to resend OTP to {phone_number}. Status: {response.status_code}, Response: {response.text}")

    except Exception as e:
        # Log any unexpected errors
        print(f"Error while sending OTP to {phone_number}: {e}")

# Example usage

