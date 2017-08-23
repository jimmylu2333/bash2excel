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
    with open('./result.json', 'w') as f:
        json.dump(data, f, indent=2)


def execute_bash(script: str) -> list:
    """execute bash and return  contents of first-echo,rest-of-echo,returncode """
    std_handle = subprocess.run(script, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    result_list = []
    if std_handle.stderr != b'':
        stderr = std_handle.stderr.decode('utf-8').strip().split('\n')
        result_list = stderr
    else:
        stdout = std_handle.stdout.decode('utf-8').strip().split('\n')
        result_list = stdout

    returncode = std_handle.returncode
    if result_list[0] == 'result':
        returncode = 'returncode'
    result_list += [returncode]
    return result_list


def check_root_permission():
    """check permission for someone's need"""# {{{
    if os.getuid() != 0:
        print('root permission is needed,please execute \'sudo -i \' to get the permission .')
        exit(0)# }}}


if __name__ == '__main__':
    dic = {}
    dic['id'] = execute_bash('bash sh/template.sh')
    dic['1'] = execute_bash('bash sh/1.sh')
    dic['2'] = execute_bash('bash sh/2.sh')
    dic['3'] = execute_bash('bash sh/3.sh')
    dic['4'] = execute_bash('bash sh/4.sh')
    data2json(dic)
