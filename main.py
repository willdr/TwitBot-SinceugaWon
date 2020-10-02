from twython import Twython
from datetime import date

# Twython setup learned from https://projects.raspberrypi.org/en/projects/getting-started-with-the-twitter-api/5
from auth import (
    consumer_key,
    consumer_secret,
    access_token,
    access_token_secret
)

def main():
    twitter = Twython(
        consumer_key,
        consumer_secret,
        access_token,
        access_token_secret
    )

    message = "It has been "
    days = getDaysSince()
    message += f'{days:,}'
    message += " days since uga won a national championship in college football."
    twitter.update_status(status=message)
    print("Tweeted: %s" % message)

def getDaysSince():
    today = date.today()
    ugaDate = date(1981, 1, 1)
    delta = today - ugaDate

    return delta.days

if __name__ == "__main__":
    main()
