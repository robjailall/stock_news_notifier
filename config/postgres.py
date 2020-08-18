import os

DATABASE_URL = os.getenv("DATABASE_URL", default="host='localhost'port='5432'dbname='stock_news_notifier'user='postgres'")
POSTGRES_SSL_MODE = os.getenv("POSTGRES_SSL_MODE", default="require")