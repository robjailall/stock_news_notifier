bin/start_local_db.sh
createuser -s postgres
createdb stock_news_notifier
psql -d stock_news_notifier -U postgres -f db/create.sql
