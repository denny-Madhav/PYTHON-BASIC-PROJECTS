import requests
import datetime as dt
import smtplib
import time
MY_LAT = 16.329866
MY_LNG = 81.734281


def over_head():
    iss_response = requests.get("http://api.open-notify.org/iss-now.json")
    iss_lat = iss_response.json()["iss_position"]["latitude"]
    iss_lng = iss_response.json()["iss_position"]["longitude"]
    if MY_LAT-3 <= iss_lat <= MY_LAT+3 and MY_LNG-3 <= iss_lng >= MY_LNG+3:
        return True


def is_night():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LNG,
        "formatted": 0,
    }
    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    sunrise_data = int(response.json()["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset_data = int(response.json()["results"]["sunset"].split("T")[1].split(":")[0])
    time_now = dt.datetime.now().hour
    if time_now >= sunset_data or time_now <= sunrise_data:
        return True


while True:
    time.sleep(120)
    if over_head() and is_night():
        my_email = "nallidenny.pip@gmail.com"
        receiver_mail = "nallidenny@gmail.com"
        my_password = "DK.python100"
        connection = smtplib.SMTP("smtp.gmail.com")
        connection.starttls()
        connection.login(user=my_email, password=my_password)
        connection.sendmail(from_addr=my_email,
                            to_addrs=receiver_mail,
                            msg="subject : ISS IS ABOUT TO REACH YOUR COORDINATES\n\n"
                                "Babai,"
                                "oka sari baitiki velli chudu, edho kanipistadhi anta.")

# print(iss_lng)
# print(iss_lat)
# print(sunrise_data)
# print(sunset_data)
# print(time_now.hour)
