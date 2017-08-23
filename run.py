#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import data2excel
from bash2data import execute_bash,data2json

if __name__ == '__main__':
    dic = {}
    dic['id'] = execute_bash('bash sh/template.sh')
    dic['1'] = execute_bash('bash sh/1.sh')
    dic['2'] = execute_bash('bash sh/2.sh')
    dic['3'] = execute_bash('bash sh/3.sh')
    dic['4'] = execute_bash('bash sh/4.sh')
    data2json(dic)
    data2excel.json2excel()
