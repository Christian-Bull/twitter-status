import sqlite3


# db connection
def connectdb(db_file):
    conn = sqlite3.connect(db_file)
    return conn


# creates db and tables if they don't exist
def createtable(conn, table):
    conn.execute(''' CREATE TABLE IF NOT EXISTS {0}
        (ID INT UNIQUE,
        created_at TEXT,
        tweet_text TEXT,
        status INT)'''.format(
        table))


def insertrow(conn, table, id, created_at, text, flag):
    conn.execute(
        "INSERT OR IGNORE INTO {0} VALUES (?, ?, ?, ?)".format(table),
        (id, created_at, text, flag))
