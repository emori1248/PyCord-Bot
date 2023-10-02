import psycopg2
from dotenv import load_dotenv
import os


def iterate_query(cursor, max_rows=10):
    while True:
        rows = cursor.fetchmany(max_rows)
        if not rows:
            break
        for row in rows:
            yield row

def query_db(guild_id, max_rows=10):
    # load_dotenv()

    try:
        conn = psycopg2.connect(
            host=os.environ["PGHOST"],
            port=os.environ["PGPORT"],
            database=os.environ["PGDATABASE"],
            user=os.environ["PGUSER"],
            password=os.environ["PGPASSWORD"])

        cursor = conn.cursor()

        print(f'Querying {guild_id}:')

        cursor.execute(f'SELECT "rule_name","rule_type","rule_content" FROM "Rule" WHERE guild_id=\'{guild_id}\'')

        rule_list = []
        for row in iterate_query(cursor, max_rows):
            rule_list.append(row)

        cursor.close()
        
        return rule_list

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
            print('Database connection closed.')
