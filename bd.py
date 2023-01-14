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

def get_max_id(id):
    with sqlite3.connect('bd/file.db') as db:
        cursor = db.cursor()
        query = """SELECT id FROM images ORDER BY id DESC LIMIT 1"""
        cursor.execute(query)
        result = cursor.fetchall()
        for i in result:
            maxVal = i[0]
        db.commit()
        return maxVal

def true_answers(id):
    with sqlite3.connect('bd/file.db') as db:
        cursor = db.cursor()
        query = """ SELECT is_cat, user_id FROM images WHERE is_cat=1"""
        cursor.execute(query)
        result = cursor.fetchall()
        sum = 0
        for i in result:
            if i[1]==id:
                sum = sum + 1
        db.commit()
        return sum

def false_answers(id):
    with sqlite3.connect('bd/file.db') as db:
        cursor = db.cursor()
        query = """ SELECT is_cat, user_id FROM images WHERE is_cat=0"""
        cursor.execute(query)
        result = cursor.fetchall()
        sum = 0
        for i in result:
            if i[1]==id:
                sum = sum + 1
        db.commit()
        return sum

def all_photos(id):
    with sqlite3.connect('bd/file.db') as db:
        cursor = db.cursor()
        query = """ SELECT id, user_id FROM images"""
        cursor.execute(query)
        result = cursor.fetchall()
        sum = 0
        for i in result:
            if i[1]==id:
                sum = sum + 1
        db.commit()
        return sum

def insert_data(id,tg_file_id, user_id, is_cat, uploaded_at):
    with sqlite3.connect('bd/file.db') as db:
        cursor = db.cursor()
        query = """ INSERT INTO images(id, tg_file_id, user_id, is_cat, uploaded_at) VALUES (?,?,?,?,?);"""
        cursor.execute(query, (id, tg_file_id, user_id, is_cat, uploaded_at))
        db.commit()

