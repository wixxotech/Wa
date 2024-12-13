import requests
import json

def send_otp(phone_number):
    """
    Function to send OTP via the Rappi API.

    :param number: The mobile number to send OTP to.
    """
    try:
        # API URL
        url = "https://services.rappi.com.br/api/rappi-authentication/login/whatsapp/create"
        
        # Country code
        country_code = "+91"
        
        # Data to be sent in the POST request (JSON format)
        data = {
            "country_code": country_code,
            "phone": phone_number
        }
        
        # Headers for the request
        headers = {
            "Content-Type": "application/json",
            "Content-Length": str(len(json.dumps(data)))  # Length of JSON data
        }
        
        # Sending the POST request
        response = requests.post(url, json=data, headers=headers)
        
        # Check for a successful response
        if response.status_code == 200:
            print(f"OTP request sent successfully to {number}")
            print(f"Response: {response.json()}")
        else:
            print(f"Failed to send OTP. Status Code: {response.status_code}")
            print(f"Response: {response.text}")
    
    except requests.exceptions.RequestException as e:
        print(f"Error occurred while sending OTP to {number}: {e}")

# Example usage
#send_otp("1234567890")
