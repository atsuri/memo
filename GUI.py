import PySimpleGUI as sg
import requests
import csv

sg.theme('Purple')
layout = [[sg.Text('メモを追加'), sg.Input(key='-MEMO-')],
    [sg.CalendarButton('日付選択', close_when_date_chosen=False, key='-DATE-', format='%Y-%m-%d')],
    [sg.Text('', key='-ACT-')],
    [sg.Button('決定'), sg.Button('終了')]]
window = sg.Window('ひとことメモ', layout)   

# log保存ファイル
file = "memolog.csv"

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == '終了':
        break
    if event == '決定':
        memo = str(values["-DATE-"]) + " " + str(values["-MEMO-"])
        window['-ACT-'].update(f'最近登録したメモ：{values["-MEMO-"]}\n日付：{values["-DATE-"]}')
        requests.post('http://localhost:8080/add',data={"memo": memo})
        # ファイル書込み
        with open(file, 'a', encoding="utf_8") as fileobj:
            text = csv.writer(fileobj)
            text.writerow([memo])
    
