from twilio.rest import TwilioRestClient
from secrets import twilio_account_sid as sid
from secrets import twilio_account_token as token
from datetime import datetime as dt
import schedule
import time


class TwilioAlarm(object):
    def __init__(self):
        self.to = '+12092171114'
        self.from_ = '+17345489423'
        self.client = TwilioRestClient(sid, token)
        schedule.every().day.at('22:58').do(self.make_call)

        while True:
            schedule.run_pending()
            time.sleep(60)

    def make_call(self):
        callback_url = 'http://demo.twilio.com/docs/voice.xml'
        print('Making call')
        self.client.calls.create(url=callback_url, to=self.to, from_=self.from_)


def main():
    alarm = TwilioAlarm()


if __name__ == '__main__':
    main()
