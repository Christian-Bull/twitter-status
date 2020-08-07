from datetime import datetime, timezone


def utc_to_local(utc_dt):
    return utc_dt.replace(tzinfo=timezone.utc).astimezone(tz=None)


class TweetObject:
    def __init__(self, tweetobject):
        self.tweetobject = tweetobject

    def get_details(self):
        self.id = self.tweetobject.id
        self.text = self.tweetobject.text
        self.created_at = utc_to_local(self.tweetobject.created_at)


# returns tweets from today
def timelinetweets(api, user, tweetcount):
    # local date
    today = datetime.now().date()
    tweets = []

    for tweet in api.user_timeline(screen_name=user, count=tweetcount):

        # create tweet class, helps apply changes to elements (ex. timezones)
        t = TweetObject(tweet)
        t.get_details()

        # if the tweet is from today, append to list
        if t.created_at.date() == today:
            tweets.append(t)

    return tweets
