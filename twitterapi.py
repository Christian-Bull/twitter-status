from datetime import datetime, timezone


def utc_to_local(utc_dt):
    return utc_dt.replace(tzinfo=timezone.utc).astimezone(tz=None)


class TweetObject:
    def __init__(self, tweetobject):
        self.tweetobject = tweetobject
        self.id = self.tweetobject.id
        self.text = self.tweetobject.full_text  # returns full tweet text
        self.created_at = utc_to_local(self.tweetobject.created_at)

    def examine_tweet(self, data):
        # if any word in the list is present, flag
        if any(word in self.text for word in data):
            self.examine_flag = 1
        else:
            self.examine_flag = 0


# returns tweets from today
def timelinetweets(api, user, tweetcount, **kwargs):
    # local date
    today = datetime.now().date()
    tweets = []

    for tweet in api.user_timeline(
        screen_name=user,
        count=tweetcount,
        tweet_mode="extended"
    ):

        # create tweet class, helps apply changes to elements (ex. timezones)
        t = TweetObject(tweet)
        # t.get_details()

        # if the tweet is from today, append to list
        today_flag = kwargs.get('today', None)
        if today_flag == 1:
            if t.created_at.date() == today:
                tweets.append(t)

        else:
            tweets.append(t)
    return tweets
