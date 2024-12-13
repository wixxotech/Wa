import requests
import json

def send_otp_firebase(phone_number):
    """
    Sends an OTP request to the given phone number using the Firebase endpoint.

    :param phone_number: The phone number to target (without country code).
    """
    try:
        # API URL
        url = "https://us-central1-x-avenue-213708.cloudfunctions.net/sendOtp"

        # Headers
        headers = {
            "Host": "us-central1-x-avenue-213708.cloudfunctions.net",
            "firebase-instance-id-token": "dgIux0MbT-29b-J2vBfiRx:APA91bFDpkyJ4y_TrMfzjIamUm3eXen6uzrbCe2NS6X5VI6SMF_u0V5_AJeFexRbpNMTOA-sD2kUNaZGeV947TNZeHn0iCPPYADyUcrUsNEHAPezZ2wYZqgp4yP9OtsV_G81j0gHz2j-",
            "Content-Type": "application/json; charset=utf-8",
            "Accept-Encoding": "gzip",
            "User-Agent": "okhttp/4.9.2"
        }

        # Payload
        payload = {
            "data": {
                "phoneNumber": f"+91{phone_number}"
            }
        }

        # Sending the POST request
        response = requests.post(url, headers=headers, data=json.dumps(payload))

        # Check the response
        if response.status_code == 200:
            print("OTP request sent successfully!")
            print("Response:", response.text)
        else:
            print(f"Failed to send OTP. Status: {response.status_code}, Response: {response.text}")

    except Exception as e:
        # Handle any unexpected errors
        print(f"Error occurred while sending OTP: {e}")

# Example usage

