import config
import twitterdb


# load dev configs
c = config.loadconfig('config.ini')
conn = config.connectdb(c.database)


# create tables
twitterdb.createdb(conn.cursor(), 'tweets')
conn.commit()
