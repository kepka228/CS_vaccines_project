from datetime import datetime

#checks is vaccine before bday
def is_vaccine_before_birthday(birthday, vaccine_date):
    birthday_object = datetime.strptime(birthday, '%Y-%m-%d %H:%M:%S')
    vaccine_object = datetime.strptime(vaccine_date, '%Y-%m-%d %H:%M:%S')
    is_vacine_before_birthday = birthday_object < vaccine_object
    return vaccine_object < birthday_object

#separate validation for input in student search
def validate_search(values):
    is_valid = True
    values_invalid = []
    
    if len(values["-STUDENT-"]) ==0:
        values_invalid.append("Name")
        is_valid = False
        
    result = [is_valid, values_invalid]
    return result

#validation of input in main window
def validate(values):
    is_valid = True
    values_invalid = []
    
    if len(values['-NAME-']) == 0:
        values_invalid.append("Name")
        is_valid = False 
        
    if len(values['-BDAY-']) == 0:
        values_invalid.append("Birthdate Date")
        is_valid = False 
        
    if not values['-MALE-'] and not values['-FEMALE-']:
        values_invalid.append("Gender")
        is_valid = False         
        
    if len(values['-DATE-']) == 0:
        values_invalid.append("Vaccine Date")
        is_valid = False     
        
    if len(values['-BDAY-']) != 0 and len(values['-DATE-']) != 0 and is_vaccine_before_birthday(values['-BDAY-'], values['-DATE-']):
        values_invalid.append("Vaccine date comes before the birthday")
        is_valid = False 
        
    try:
        print(values['-VACCINE-'][0])
    
    except:
        values_invalid.append("Vaccine Type")
        is_valid = False
    
    result = [is_valid, values_invalid]
    return result

#creation of error msg with problems
def create_error_msg(values_invalid):
    error_msg = ''
    for value_invalid in values_invalid:
        error_msg +=("\nInvalid" + ":"+ value_invalid)
    return error_msg