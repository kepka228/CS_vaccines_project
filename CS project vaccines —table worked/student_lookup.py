import PySimpleGUI as sg
import database_interface
import lookup_table
from data_validation import validate_search
from data_validation import create_error_msg


#search window layout
def create():
    student_search_layout = [[sg.Text("Enter name of the student you need:"), 
                             sg.Input(key='-STUDENT-', do_not_clear= True, font='Cinzel', size=(25, 1))],
                             [sg.Button("Search"), sg.Button("Exit")]]
                             
    student_search = sg.Window("Student Search", student_search_layout, modal=True)
    
#event loop, validation of input, output of data retrieved for specific student from DB
    while True:
        event, values = student_search.read()
        if event == "Exit" or event == sg.WIN_CLOSED:
            break
        elif event == "Search":
            result = validate_search(values)
            if result[0]:
                if len(database_interface.student_search(values["-STUDENT-"])) ==0:
                    sg.popup("No records found for ", values["-STUDENT-"], ".")
                lookup_table.create(values["-STUDENT-"])
            else:
                print(result)
                error_msg = create_error_msg(result[1])
                sg.popup(error_msg)
    student_search.close() 
