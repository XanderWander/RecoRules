import json
import psycopg2


def run_query(name):
    with open("resources/database.conf") as f:
        login = json.load(f)
        conn = psycopg2.connect(
            host=login['host'],
            database=login['database'],
            user=login['user'],
            password=login['password']
        )
        cur = conn.cursor()

        with open(f"resources/{name}.sql") as f2:
            query = ''.join(f2.readlines())
            cur.execute(query)


run_query("order_count")
