#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import json
import subprocess
import os


def data2xml(data: dict):
    """this function will transform bash output to xml """
    pass


# dict -> {id:['name','result',sign:Bool]}
def data2json(data: dict):
    """ this function will transform bash output to json """
    with open('./bash2json.json', 'w') as f:
        json.dump(data, f, indent=4)


def execute_bash(script: str) -> list:
    """execute bash and return  contents of first-echo,rest-of-echo,returncode """
    std_handle = subprocess.run(script, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    result_list = []

    if len(std_handle.stderr) != 0:
        stderr = std_handle.stderr.decode('utf-8').strip().split('\n')
        result_list = stderr+[None]
    elif len(std_handle.stdout) != 0:
        stdout = std_handle.stdout.decode('utf-8').strip().split('\n')
        tmp = str()
        if len(stdout) > 2:
            for i in stdout[1:len(stdout)]:
                tmp += i+'\n'
        elif len(stdout) == 2:
            tmp = stdout[1]
        else:
            tmp = None

        result_list = [stdout[0]]+[tmp]

    returncode = std_handle.returncode
    if result_list[0] == 'name':
        returncode = 'returncode'
    result_list += [returncode]
    return result_list


def print_result(data: dict):
    """print result to tty"""
    for keys in data.keys():
        if keys == 'id':
            continue
        print("id:", keys)
        print("name:", data[keys][0])
        print("result:", data[keys][1],)
        print("returncode:", data[keys][2])


def check_root_permission():
    """check permission for someone's need"""
    if os.getuid() != 0:
        print('root permission is needed,please execute \'sudo -i \' to get the permission .')
        exit(0)

if __name__ == '__main__':
    dic = {}
    dic['id'] = execute_bash('echo "name";echo "result";')
    dic['1'] = execute_bash('echo "hello";echo "world";')
    data2json(dic)
    print_result(dic)