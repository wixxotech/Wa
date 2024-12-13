import requests
import json

def send_otp(phone_number):
    # Define the mobile number and country code
    country_code = "91"
    
    # API URLs
    url1 = "https://api.foxy.in/api/v2/users/send_otp"
    url2 = "https://api.foxy.in/api/v2/users/send_otp"
    
    # Data for the first OTP request
    data1 = {
        'guest_token': '8847daf0-0785-11ef-a442-bb8ba98df89f',
        'user': {
            'phone_number': f"+91{phone_number}"
        },
        'invite_code': ''
    }

    # Data for the second OTP request
    data2 = {
        'user': {
            'phone_number': f"+91{phone_number}"
        },
        'via': 'whatsapp'
    }

    # Headers for the requests
    headers = {
        'Host': 'api.foxy.in',
        'accept': 'application/json',
        'x-build-version': '10.6.5',
        'x-app-platform': 'android',
        'x-guest-token': '8847daf0-0785-11ef-a442-bb8ba98df89f',
        'content-type': 'application/json',
        'accept-encoding': 'gzip',
        'user-agent': 'okhttp/4.9.2'
    }

    # Function to send OTP
    def send_otp_request(url, data, headers):
        response = requests.post(url, json=data, headers=headers)
        if response.status_code == 200:
            return response.json()  # Return JSON response if successful
        else:
            return {"error": f"Failed to send OTP. Status: {response.status_code}, Response: {response.text}"}

    # Send the first OTP request
    response1 = send_otp_request(url1, data1, headers)
    print("Response 1:", response1)

    # Send the second OTP request
    response2 = send_otp_request(url2, data2, headers)
    print("Response 2:", response2)

# Example usage
#number = "1234567890"  # Replace with actual phone number
send_otp(phone_number)
