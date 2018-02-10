# btcde-poll
Microservice to poll bitcoin.de API orderbook for the missing minutely trading chart info on BTC-EURO, BCH-EURO and ETH-EURO crypto charts.

This is WIP and my first python / flask / sqlAlchemy / google cloud project so feel free to comment  

## development setup
- request bitcoin.de api-keys
- setup a mysql database or setup a google cloud sql instance
- install dependencies
```
pip install -r requirements.txt
```
- set credentials to your env and run the flask-service

```
export BTCDE_API_KEY='...'
export BTCDE_API_SECRET='...'
export SQLALCHEMY_DATABASE_URI='mysql+pymysql://user:pw@/db?unix_socket=/tmp/cloudsql.sock/db-onnection-name'
```

- setup database tables with migration
```
python create_tables.py
```
- run the server
```
python main.py
```

- setup a cron job to call the tracking task /task/track_btcde or on google cloud app deploy cron.yaml
```
gcloud app deploy cron.yaml
```


