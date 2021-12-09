import csv
import database_interface

#export function
def export():
    vaccines_records_array = database_interface.retrieve_vaccines()
    f = open('student_vaccines.csv', 'w', newline = "")
    writer = csv.writer(f)
    writer.writerow(["Name", "Birthday Date", "Gender", "Vaccination Date", "Vaccination type"])
    writer.writerows(vaccines_records_array)
    f.close()

