import PySimpleGUI as sg
import database_interface

#TABLE layout
def create():
    vaccines_records_array = database_interface.retrieve_vaccines()
    headings = ['Name', 'Birthday Date', 'Gender', 'Vaccination Date', 'Vaccine type']


    storing_window_layout = [
        [sg.Table(values=vaccines_records_array, headings = headings,  max_col_width=35,
                    auto_size_columns=True,
                    display_row_numbers=True,
                    justification='right',
                    num_rows=10,
                    key='-TABLE-',
                    row_height=35,
                    tooltip='Vaccinations Table')],
        [sg.Button("Exit")]
    ]

    storing_window = sg.Window("Student Vaccinations", storing_window_layout, modal=True)

#event loop for closing the table
    while True:
        event, values = storing_window.read()
        if event == "Exit" or event == sg.WIN_CLOSED:
            break
        
    storing_window.close() 