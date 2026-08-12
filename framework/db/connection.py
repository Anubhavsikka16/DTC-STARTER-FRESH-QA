import psycopg


class Database:
#db = Database(...), we will call psycopg.connect(...)
    def __init__(
        self,
        host,
        port,
        database,
        user,
        password
    ):
        self.connection = psycopg.connect(
            host=host,
            port=port,
            dbname=database,
            user=user,
            password=password
        )
    def fetch_one(self, query, params=None):

        with self.connection.cursor() as cursor:

            cursor.execute(query, params)

            return cursor.fetchone()
    def close(self):
        self.connection.close()

