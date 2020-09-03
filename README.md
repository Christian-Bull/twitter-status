Christian Bull

# Twitter Status
Scrapes tweets from a trail status account and loads them into a sqlite3 database. Currently uses a list of keywords `assets/src.csv` to determine trail status.


## Build:

clone repo  

`git clone https://github.com/Christian-Bull/twitter-status.git`

build image  

`docker build --tag <name it something> .`

run it 

`docker run -e config=$config -v </path/to/db/on/host>:<name of your image:version>`
