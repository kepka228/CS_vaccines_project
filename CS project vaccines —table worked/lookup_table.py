import PySimpleGUI as sg
import database_interface

#TABLE
def create(name):
    student_records_array = database_interface.student_search(name)
    headings = ['Name', 'Birthday Date', 'Gender', 'Vaccination Date', 'Vaccine type']


    student_results_layout = [
        [sg.Table(values=student_records_array, headings = headings,  max_col_width=35,
                    auto_size_columns=True,
                    display_row_numbers=True,
                    justification='right',
                    num_rows=10,
                    key='-TABLE-',
                    row_height=35,
                    tooltip= name + 'Table')],
        [sg.Button("Exit")]
    ]

    search_results_window = sg.Window(name + "Records", student_results_layout, modal=True)

    while True:
        event, values = search_results_window.read()
        if event == "Exit" or event == sg.WIN_CLOSED:
            break
        
    search_results_window.close() 