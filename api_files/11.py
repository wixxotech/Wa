import requests

# Define the phone number and country code (+91)
def run(phone_number):
    full_number = "+91" + phone_number

    # Base API URL
    base_url = "https://jotp.jockey.in/api/login/"

    # Function to send OTP or resend OTP
    def request_otp(action='send-otp'):
        url = f"{base_url}{action}/{full_number}?whatsapp=true"

        # Send GET request
        try:
            response = requests.get(url)
            # Return HTTP code and response text
            return {'httpCode': response.status_code, 'response': response.text}
        except requests.exceptions.RequestException as e:
            # Handle any request errors
            return {'httpCode': 'Error', 'response': str(e)}

    # Call send-otp and print response
    send_response = request_otp('send-otp')
    print("Send OTP Response:")
    print(send_response)

    # Call resend-otp and print response
    resend_response = request_otp('resend-otp')
    print("Resend OTP Response:")
    print(resend_response)


# Example usage: replace with the actual mobile number
#number = "1234567890"
#send_otp(phone_number)
