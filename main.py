import config
import twitterapi
import twitterdb


def main():
    # load config, data
    c = config.loadconfig('config.ini')
    f = config.loaddata('src.csv')

    # db stuff
    connection = twitterdb.connectdb(c.database)
    conn = connection.cursor()
    twitterdb.createtable(conn, c.table)

    # create api instance
    api = config.createapi(c)

    # get  most recent tweet
    tweets = twitterapi.timelinetweets(api, c.user, c.count, today=1)

    for tweet in tweets:
        tweet.examine_tweet(f)

        # insert into db
        twitterdb.insertrow(
            conn,
            c.table,
            tweet.id,
            tweet.created_at,
            tweet.text,
            tweet.examine_flag
        )

    connection.commit()
    connection.close()


main()
