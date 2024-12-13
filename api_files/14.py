import requests
import json

def run(phone_number):
    """
    Function to send OTP via the Rigi API.

    :param number: The mobile number to send OTP to.
    """
    try:
        # API URL
        url = "https://api.rigi.club/api/account/sendotp"
        
        # Country code
        country_code = "91"
        
        # Data to be sent in the POST request (JSON format)
        payload = {
            "p_n": f"+91{phone_number}",
            "countryCode": country_code
        }
        
        # Headers for the request
        headers = {
            "Content-Type": "application/json",
            "Accept": "application/json, text/plain, */*",
            "OS": "android",
            "Mode": "MOBILE_APP",
            "AppVersion": "10.1.0",
            "DeviceId": "c7abc1fd7459e84c",
            "User-Agent": "okhttp/4.9.1",
            "Accept-Encoding": "gzip"
        }
        
        # Sending the POST request
        response = requests.post(url, json=payload, headers=headers)
        
        # Check for a successful response
        if response.status_code == 200:
            print(f"OTP sent successfully to {number}")
            print(f"API Response: {response.json()}")
        else:
            print(f"Failed to send OTP. Status Code: {response.status_code}")
            print(f"Response: {response.text}")
    
    except Exception as e:
        print(f"Error occurred while sending OTP to {number}: {e}")

# Example usage
#send_otp("1234567890")
