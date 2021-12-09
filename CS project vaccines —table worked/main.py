import PySimpleGUI as sg
import display_data_table 
import database_interface
import student_lookup
import export_data 
from data_validation import validate
from data_validation import create_error_msg


#color palette
sg.theme('TealMono')

#main window layout
layout = [
          [sg.Text("Enter student name:"), sg.Input(key='-NAME-', do_not_clear= True, font='Cinzel', size=(35, 1))],
          [sg.Text("Enter birthday date"), sg.Input(key='-BDAY-', size=(20,1)), sg.CalendarButton("BIRTHDAY DATE", close_when_date_chosen=True,  target='-BDAY-', location=(0,0), no_titlebar=False )],          
          [sg.Text("                               "), sg.Radio("Male", "RADIO", key='-MALE-'), sg.Radio("Female", "RADIO", key='-FEMALE-'), sg.Radio("Other", "RADIO", key='-OTHER-')],
          [sg.Text("Enter the vaccination date:"), sg.Input(key='-DATE-', size=(20,1)), sg.CalendarButton("DATE OF VACCINATION", close_when_date_chosen=True,  target='-DATE-', location=(0,0), no_titlebar=False )],
          [sg.Text('Choose the vaccine:',size=(30, 1), font='Cinzel',justification='left')],
          [sg.Listbox(values=["Hepatitis A", "Hepatitis B", "Coronavirus", "MMR", "Chickenpox", "Polio"], size=(40, 6), select_mode='single', key='-VACCINE-',)],
          [sg.Button('Submit Data'), sg.Button('See Students Records'),sg.Button('Find Student'), sg.Button('Save As CSV File'), sg.Exit()],
]

window = sg.Window('Vaccine tracker', layout)

storing_array = []

#event loop: input validation, data added to the DB,  button interactions
while True:
    event, values = window.read()
    if event in (sg.WIN_CLOSED, 'Exit'):
        break
    elif event == 'Submit Data':
        result = validate(values)
        if result[0]:
            gender = ''
            if values['-MALE-']: 
                gender += 'Male'
            elif values['-FEMALE-']: 
                gender += 'Female'
            else: 
                gender += 'other'
            database_interface.insert_vaccines(
                values['-NAME-'],
                values['-BDAY-'],
                gender,
                values['-DATE-'],
                values['-VACCINE-'][0])
            sg.popup("Student Data Saved!")
        else:
            error_msg = create_error_msg(result[1])
            sg.popup(error_msg)
    elif event == 'See Students Records':
        display_data_table.create()
    elif event == "Find Student":
        student_lookup.create()
    elif event == "Save As CSV File":
        export_data.export()
        sg.popup("Data saved to a CSV file")
window.close()
