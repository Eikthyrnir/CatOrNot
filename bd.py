import sqlite3
import datetime
def get_connect():
    with sqlite3.connect('bd/file.db') as db:
        cursor = db.cursor()
        query = """ CREATE TABLE IF NOT EXISTS images(
            id              INTEGER PRIMARY KEY,
            tg_file_id      INTEGER NOT NULL,
            user_id         INTEGER NOT NULL,
            is_cat          BLOB NOT NULL,
            uploaded_at     INTEGER NOT NULL
        )"""
        cursor.execute(query)
        db.commit()

def get_max_id():
    with sqlite3.connect('bd/file.db') as db:
        cursor = db.cursor()
        query = """SELECT id FROM images ORDER BY id DESC LIMIT 1"""
        cursor.execute(query)
        for row in cursor:
            for elem in row:
                maxVal = elem
        db.commit()
        return maxVal


def insert_data(id,tg_file_id, user_id, is_cat, uploaded_at):
    with sqlite3.connect('bd/file.db') as db:
        cursor = db.cursor()
        query = """ INSERT INTO images(id, tg_file_id, user_id, is_cat, uploaded_at) VALUES (?,?,?,?,?);"""
        cursor.execute(query, (id, tg_file_id, user_id, is_cat, uploaded_at))
        db.commit()

