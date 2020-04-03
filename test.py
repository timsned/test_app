import PySimpleGUI as sg


def win1():
    layout = [  [sg.Combo(['male', 'female'])],
                [sg.Button('Ok'), sg.Button('Cancel')] ]

    window = sg.Window('Window Title', layout)

    event, values = window.read()
    if event == 'Ok':
        return values[0]
      



def win2(gender):
    male = ['1', '2', '3']
    female = ['4', '5', '6']

    if gender == 'male':
        event_list = male
    else:
        event_list = female     

    layout = [  [sg.Combo(event_list)],
                [sg.Button('Ok'), sg.Button('Cancel')] ]

    window = sg.Window('Window Title', layout)

    event, values = window.read()
    print(values[0])
    window.close()


while True:
    gender = win1()
    win2(gender)
window.close()
