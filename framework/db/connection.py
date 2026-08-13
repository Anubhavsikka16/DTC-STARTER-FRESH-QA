import psycopg # --> Python PostgreSQL driver.


class Database:
#db = Database(...), we will call psycopg.connect(...)
#so when DB object is created, constructor will be called with all the parameters
    def __init__(self,host,port,database,user,password):

        self.connection = psycopg.connect(
            host=host,
            port=port,
            dbname=database,
            user=user,
            password=password
        )
    def fetch_one(self, query, params=None):

        with self.connection.cursor() as cursor:
            #Cursor is a tool that lets Python send SQL commands to the database and retrieve results.
            
            cursor.execute(query, params)

            return cursor.fetchone()
    def close(self):
        self.connection.close()

