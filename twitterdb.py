# contains some basic db functions


# creates db and tables if they don't exist
def createdb(conn, table):
    conn.execute(''' CREATE TABLE IF NOT EXISTS twitter
            (ID INT, created_at TEXT, tweet_text TEXT) ''')


# def insertrow(conn, table, tweet_payload):
#       c.execute('''INSERT INTO {0})
