import psycopg2
import time


def connect_to_bd():
    time.time()
    # Create a connection credentials to the PostgreSQL database
    try:
        connection = psycopg2.connect(
            user="stilpert",
            password="citizen2000",
            host="localhost",
            port="5432",
            database="movie_Industry"
        )

        # Handle the error throws by the command that is useful when using python while working with PostgreSQL
    except (Exception, psycopg2.Error) as error:
        print("Error connecting to PostgreSQL database", error)

    # Close the database connection
    finally:
        return connection


def select_all(connection, table_name):
    try:
        cursor = connection.cursor()
        query = f"select * from {table_name}"
        cursor.execute(query)
        items = cursor.fetchall()
    except (Exception, psycopg2.Error) as error:
        print("Error while fetching data from PostgreSQL", error)
        items = None
    finally:
        if connection:
            cursor.close()
        return items


def select_by_pr(connection, attribute, parameter, table_name):
    try:
        cursor = connection.cursor()
        query = f"select * from {table_name} where {attribute}='{parameter}'"
        cursor.execute(query)
        item = cursor.fetchall()
    except (Exception, psycopg2.Error) as error:
        print("Error while fetching data from PostgreSQL", error)
        item = False
    finally:
        if connection:
            cursor.close()
        return item


def search(search_word):
    connection = None
    try:
        connection = connect_to_bd()
        cursor = connection.cursor()
        list_tables = {"movies", "actors", "studios"}
        res = []
        timestamp = time.time()
        for name_table in list_tables:
            q = f"SELECT column_name FROM information_schema.columns WHERE " \
                f"( table_schema = 'public' AND table_name = '{name_table}' ) ORDER BY column_name;"
            cursor.execute(q)
            list_columns = cursor.fetchall()
            for name_column in list_columns:
                if "id" in name_column[0] or "age" in name_column[0] or "budget" in name_column[0]:

                    if search_word.isdigit():
                        q = f"SELECT DISTINCT * FROM {name_table} " \
                           f"WHERE {name_column[0]}={int(search_word)} "
                    else:
                        continue
                else:
                    q = f"SELECT DISTINCT * FROM {name_table} WHERE {name_column[0]} LIKE '%{search_word}%' "
                cursor.execute(q)
                row = cursor.fetchone()
                if row is not None:
                    res.append(row)
        time_ms = (time.time()-timestamp)*1000
    finally:
        if connection:
            cursor.close()
            connection.close()
            return {"results": res, "time": time_ms}


def delete_items(connection, attribute, parameter, table_name):
    try:
        cursor = connection.cursor()
        query = f"delete from {table_name} where {attribute}='{parameter}'"
        cursor.execute(query)
        connection.commit()
        cursor.close()
        item = True
    except (Exception, psycopg2.Error) as error:
        print("Error while fetching data from PostgreSQL", error)
        item = False
    finally:
        if connection:
            cursor.close()
        return item


def delete_items_by_couple_prs(connection, prs, table_name):
    item = None
    try:
        cursor = connection.cursor()
        pr_str = ""
        for key in prs:
            pr_str += "" + key + "=" + "'" + str(prs[key]) + "' AND "

        query = f"delete from {table_name} where {pr_str[:-5]}"
        cursor.execute(query)
        connection.commit()
        cursor.close()
        item = True
    except (Exception, psycopg2.Error) as error:
        print("Error while fetching data from PostgreSQL", error)
        item = False
    finally:
        if connection:
            cursor.close()
        return item


def insert_one(connection, data, table_name):
    item = None
    try:
        cursor = connection.cursor()
        attr_string = ""
        pr_string = ""
        for key in data:
            attr_string += key + ", "
            pr_string += "\'" + str(data[key]) + "\'" + ", "

        query = f" INSERT INTO {table_name} ({attr_string[:-2]}) VALUES ({pr_string[:-2]})"
        cursor.execute(query)
        connection.commit()
        item = True
    except (Exception, psycopg2.Error) as error:
        print("Error while INSERTING data to PostgreSQL", error)
        item = False
    finally:
        if connection:
            cursor.close()
        return item


def update_one(connection, data, attr, pr, table_name):
    item = None
    try:
        cursor = connection.cursor()
        pr_str = ""
        for key in data:
            pr_str += "" + key + "=" + "'" + str(data[key]) + "', "

        query = f" UPDATE {table_name} SET {pr_str[:-2]} where {attr}='{pr}'"
        cursor.execute(query)
        connection.commit()
        item = True
    except (Exception, psycopg2.Error) as error:
        print("Error while INSERTING data to PostgreSQL", error)
        item = False
    finally:
        if connection:
            cursor.close()
            return item


def generate_items(connection, number, table_name):
    try:
        cursor = connection.cursor()

        query = f" SELECT generate_series(1,{number}) AS id, md5    (random()::text) AS full_name, " \
                f" 'male' AS gender, floor(random() * 80)::int AS age;"
        cursor.execute(query)
        items = cursor.fetchall()
    except (Exception, psycopg2.Error) as error:
        print("Error while INSERTING data to PostgreSQL", error)
        items = None
    finally:
        if connection:
            cursor.close()
            return items


def close_db_connection(connection):
    connection.close()
    print("PostgreSQL connection is now closed")