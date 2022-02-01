from email_data2 import MY_EMAIL, SENHA, account_sid, auth_token
from flight_data import FlightData
import smtplib
from twilio.rest import Client

f_data = FlightData()

class NotificationManager:

    def send_email(self, flight):
        server = smtplib.SMTP('smtp.gmail.com')
        server.ehlo()

        server.starttls()  #secures connection
        server.login(user= MY_EMAIL, password= SENHA)
        server.sendmail(
            from_addr= MY_EMAIL,
            to_addrs= MY_EMAIL,
            msg= f'Subject: Fligths \n\n{flight}.'
            )


    def send_sms(self, flight):
        try:
            client = Client(account_sid, auth_token)
            message = client.messages \
                            .create(
                                 body= flight,
                                 from_= '+12086001119',
                                 to= '+5561999854775',
                             )

            print(message.status)
        except KeyError:
            print('oi')
