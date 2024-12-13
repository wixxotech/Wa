import requests
import json

def generate_otp(phone_number):
    # API URL
    url = 'https://api.rummyculture.com/api/auth/generateOtp'
    
    # Data to be sent in the POST request
    data = {
        'mobile': phone_number,
        'verificationChannel': '5',
        'medium': 'WHATSAPP'
    }
    
    # Headers for the request
    headers = {
        'accept': 'application/json, text/plain, */*',
        'content-type': 'application/json',
        'user-agent': 'okhttp/4.9.2'
    }
    
    try:
        # Send the POST request
        response = requests.post(url, json=data, headers=headers)

        # Check if the request was successful
        if response.status_code == 200:
            print("Response:", response.text)
        else:
            print(f"Failed to send OTP. Status code: {response.status_code}, Response: {response.text}")

    except requests.exceptions.RequestException as e:
        # Handle exceptions such as network errors
        print(f"Error occurred: {e}")

# Example usage
#number = "1234567890"  # Replace with the actual phone number
#generate_otp(phone_number)
