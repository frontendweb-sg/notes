import requests
from requests.auth import HTTPBasicAuth


def send_message(f: str, t: str):
    url = "https://api.twilio.com/"

    auth = HTTPBasicAuth("twillio_secret", "")
    data = {"To": f, "From": t, "Body": input("Enter you message: ")}
    res = requests.post(url, auth=auth, data=data)
    print(res.status_code)
    print(res.headers)
    print(res.json())


send_message("+919818805996", "+917291893484")
