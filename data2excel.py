#!/usr/bin/env python3

import openpyxl,json

def json2excel():
    '''this function will transform json to excel'''
    with open('./result.json', 'r') as f:
        data = json.load(f)
    new_list = list()
    for i,j in data.items():
        new_list += [[i,' \n'.join(j[0:len(j)-1]),j[len(j)-1]]]
    wb = openpyxl.Workbook()
    ws = wb.active
    for i in range(1,len(data.keys())+1):
        for j in range(1,4):
            ws.cell(row=i,column=j,value=str(new_list[i-1][j-1]))
    wb.save('result.xlsx')
    print("done! \ncheck out result.xlsx file in current directory.")


if __name__ == '__main__':
    json2excel()


