import sqlite3


def create_table():
    connection = sqlite3.connect('cinema.db')
    connection.execute("""
    CREATE TABLE "Seat" (
        "seat_id"	TEXT,
        "taken"	INTEGER,
        "price"	REAL
    );
    """)

    connection.commit()
    connection.close()


def insert_record():
    connection = sqlite3.connect('cinema.db')
    connection.execute("""
    INSERT INTO "Seat" ("seat_id", "taken", "price") VALUES ("A3", "0", "90"), ("A4", "1", "190"), ("b1", "0", "40") 
    """)
    connection.commit()
    connection.close()


def select_all():
    connection = sqlite3.connect('cinema.db')
    cursor = connection.cursor()
    cursor.execute("""
    SELECT * FROM "Seat"
    """)
    result = cursor.fetchall()
    return result


def select_specific_columns(column_name):
    connection = sqlite3.connect('cinema.db')
    cursor = connection.cursor()
    cursor.execute(f"""
    SELECT {column_name} FROM "Seat"
    """)
    result = cursor.fetchall()
    return result


def select_with_condition(condition):
    connection = sqlite3.connect('cinema.db')
    cursor = connection.cursor()
    cursor.execute(f"""
    SELECT * FROM "Seat" WHERE {condition}
    """)
    result = cursor.fetchall()
    return result


def update_value():
    connection = sqlite3.connect('cinema.db')
    connection.execute("""
    UPDATE "Seat" SET "taken"=1
    """)
    connection.commit()
    connection.close()


def update_value_with_cond(sett, cond):
    connection = sqlite3.connect('cinema.db')
    connection.execute(f"""
    UPDATE "Seat" SET {sett} WHERE {cond} 
    """)
    connection.commit()
    connection.close()


def delete_record():
    connection = sqlite3.connect('cinema.db')
    connection.execute("""
    DELETE FROM "Seat" WHERE seat_id="A4"
    """)
    connection.commit()
    connection.close()
