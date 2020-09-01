import config
import twitterapi


def main():
    # load config, data
    c = config.loadconfig('config.ini')
    f = config.loaddata('src.csv')
    # c = config.connectdb(c.database)

    # create table
    # c.execute(''' CREATE TABLE IF NOT EXISTS twitter''')

    # create api instance
    api = config.createapi(c)

    # get  most recent tweet
    tweets = twitterapi.timelinetweets(api, c.user, c.count, today=1)

    for tweet in tweets:
        print(tweet.id)
        print(tweet.text)
        print(tweet.created_at)
        tweet.examine_tweet(f)
        print(tweet.examine_flag)


main()
