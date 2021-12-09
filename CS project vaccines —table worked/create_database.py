import sqlite3

#DB created
conn = sqlite3.connect('vaccines_info.db')
query = (''' CREATE TABLE VACCINES
            (NAME               TEXT    NOT NULL,
            BIRTHDAY                TEXT    NOT NULL,
            GENDER              TEXT    NOT NULL,
            VACCINATION_DATE                TEXT    NOT NULL,
            VACCINATION_TYPE                TEXT    NOT NULL);''')
conn.execute(query)
conn.close()