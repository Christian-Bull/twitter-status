from datetime import datetime, timezone


def utc_to_local(utc_dt):
    return utc_dt.replace(tzinfo=timezone.utc).astimezone(tz=None)


# returns tweets from today
def timelinetweets(api, user, tweetcount):
    # local date
    today = datetime.now().date()
    tweets = []

    for tweet in api.user_timeline(screen_name=user, count=tweetcount):

        # if the tweet is from today, append to list
        if tweet.created_at.date() == today:
            tweets.append(tweet)

    return tweets
