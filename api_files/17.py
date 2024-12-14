def run(phone_number):
    url = "https://api.onsiteteams.in/apis/v3/send-whatsapp-otp"
    headers = {
        "Host": "api.onsiteteams.in",
        "Authorization": "",  # Ensure to include the correct token if needed
        "version-code": "227",
        "version-name": "12.15.1",
        "package-name": "com.app.onsite",
        "User-Agent": "Onsite",
        "Content-Type": "application/json; charset=UTF-8",
        "Content-Length": "41",  # This is generally not required
        "Accept-Encoding": "gzip"
    }
    data = {
        "country_code": "91",
        "mobile": phone_number
    }

    response = requests.post(url, headers=headers, json=data)
    print("Send WhatsApp OTP Response:", response.status_code, response.text)

# Call the function
