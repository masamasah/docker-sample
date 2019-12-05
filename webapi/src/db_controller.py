import psycopg2

host = "db"
database = "test01"
user = "test01"
password = "test01"

def get_connection():
  return psycopg2.connect(host=host, database=database, user=user,password=password)

def getTest():
  with get_connection() as conn:
      with conn.cursor() as cur:
        cur.execute('SELECT * FROM test')
        res = cur.fetchone()
  return {"val": res[0]}