import config
import twitterapi


def main():
    # load config
    c = config.loadconfig('config.ini')

    # create api instance
    api = config.createapi(c)

    # get  most recent tweet
    tweets = twitterapi.timelinetweets(api, c.user, c.count)

    for tweet in tweets:
        print(tweet.text)
        print(tweet.created_at)


main()
