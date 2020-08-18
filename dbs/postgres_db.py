import psycopg2

from config.postgres import DATABASE_URL, POSTGRES_SSL_MODE


class PostgresSource(object):

    def __init__(self):
        self._connection = None
        self._connect()

    def _connect(self):

        if not self._connection:

            try:
                connection = psycopg2.connect(DATABASE_URL, sslmode=POSTGRES_SSL_MODE)
                self._connection = connection
                cursor = connection.cursor()
                # Print PostgreSQL Connection properties
                print(connection.get_dsn_parameters(), "\n")

                # Print PostgreSQL version
                cursor.execute("SELECT version();")
                record = cursor.fetchone()
                print("You are connected to - ", record, "\n")


            except (Exception, psycopg2.Error) as error:
                print("Error while connecting to PostgreSQL", error)

    @property
    def connection(self):
        self._connect()
        return self._connection

    def __del__(self):
        # closing database connection.
        if self._connection:
            self._connection.close()
            print("PostgreSQL connection is closed")

    def get_last_crawl(self, news_source):
        connection = self.connection
        cursor = connection.cursor()

        cursor.execute("SELECT last_scrape from public.source_crawls where source_key = %s", (news_source,))
        record = cursor.fetchone()
        if record is not None:
            return record[0]
        else:
            return None

    def save_last_crawl(self, news_source, text, diff_string=""):
        connection = self.connection
        cursor = connection.cursor()

        cursor.execute(
            "INSERT INTO public.source_crawls(source_key, last_scrape, last_diff)  VALUES(%s, %s, %s) ON CONFLICT (source_key) DO UPDATE SET last_scrape = %s, last_diff = %s, last_update = NOW()",
            (news_source, text, diff_string, text, diff_string))

        connection.commit()


def create_db():
    return PostgresSource()
