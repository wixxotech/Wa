import requests
import datetime

def run(phone_number):
    """
    Function to handle the SMS/API logic for this module.

    :param phone_number: The phone number to target.
    """
    try:
        # API URL
        url = "https://api.rigi.club/api/account/sendotp"

        # Common headers
        headers = {
            "Content-Type": "application/json"
        }

        # Payload for the request
        data = {
            "p_n": "+91" + phone_number,
            "countryCode": "91",
            "is_resend_request": True
        }

        # Sending the API request
        response = requests.post(url, json=data, headers=headers)

        if response.status_code == 200:
            print(f"API: OTP sent successfully to {phone_number}")
        else:
            print(f"API: Failed to send OTP to {phone_number}, Status: {response.status_code}, Response: {response.text}")

    except Exception as e:
        # Catch and log any unexpected errors
        print(f"API: Error while sending OTP to {phone_number}: {e}")

# Example usage
#run("1234567890")
