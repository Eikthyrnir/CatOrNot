import sqlite3
import datetime
def get_connect():
    with sqlite3.connect('bd/file.db') as db:
        cursor = db.cursor()
        query = """ CREATE TABLE IF NOT EXISTS images(
            id              INTEGER PRIMARY KEY,
            tg_file_id      VARCHAR NOT NULL,
            user_id         INTEGER NOT NULL,
            is_cat          INTEGER NOT NULL,
            uploaded_at     VARCHAR NOT NULL
        )"""
        cursor.execute(query)
        db.commit()


def true_answers(id):
    with sqlite3.connect('bd/file.db') as db:
        cursor = db.cursor()
        query = """ SELECT COUNT(*) FROM images WHERE is_cat=1 AND user_id = ?"""
        cursor.execute(query, (id,))
        result = cursor.fetchall()[0]
        db.commit()
        return result[0]

def false_answers(id):
    with sqlite3.connect('bd/file.db') as db:
        cursor = db.cursor()
        query = """ SELECT COUNT(*) FROM images WHERE is_cat=0 AND user_id = ?"""
        cursor.execute(query, (id,))
        result = cursor.fetchall()[0]
        db.commit()
        return result[0]

def all_photos(id):
    with sqlite3.connect('bd/file.db') as db:
        cursor = db.cursor()
        query = """ SELECT COUNT(*) FROM images WHERE user_id = ?"""
        cursor.execute(query, (id,))
        result = cursor.fetchall()[0]
        db.commit()
        return result[0]

def insert_data(tg_file_id, user_id, is_cat, uploaded_at):
    with sqlite3.connect('bd/file.db') as db:
        cursor = db.cursor()
        query = """ INSERT INTO images(tg_file_id, user_id, is_cat, uploaded_at) VALUES (?,?,?,?);"""
        cursor.execute(query, (tg_file_id, user_id, is_cat, uploaded_at))
        db.commit()

