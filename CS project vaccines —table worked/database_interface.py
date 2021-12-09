import sqlite3

#insert data into database
def insert_vaccines(name, birthday, gender, vaccination_date, vaccination_type):
    conn = sqlite3.connect('vaccines_info.db')
    conn.execute("INSERT INTO VACCINES (NAME, BIRTHDAY, GENDER, VACCINATION_DATE, VACCINATION_TYPE) \
        VALUES (?,?,?,?,?)", (name, birthday, gender, vaccination_date, vaccination_type))
    conn.commit()
    conn.close()
    

#access data from the DB & use it
def retrieve_vaccines():
    results = []
    conn = sqlite3.connect('vaccines_info.db')
    cursor = conn.execute("SELECT * from VACCINES")
    for row in cursor:
        results.append(list(row)) 
        
    return results

#access data for specific student via name
def student_search(student_name):
    results = []
    conn = sqlite3.connect('vaccines_info.db')
    cursor = conn.execute("SELECT NAME, BIRTHDAY, GENDER, VACCINATION_DATE, VACCINATION_TYPE from VACCINES where NAME == ?", (student_name,))
    for row in cursor:
        results.append(list(row)) 

    return results