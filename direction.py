# -*- coding: utf-8 -*-
"""
hierarchical prompt usage example
"""
from __future__ import print_function, unicode_literals

from PyInquirer import style_from_dict, Token, prompt, Separator

from examples import custom_style_1
from examples import custom_style_2
from examples import custom_style_3

from pprint import pprint



def ask_what_to_do():
    what_to_do_prompt = {
        'type': 'list',
        'name': 'mainoption',
        'message': 'What do you want to do?',
        'choices': [
            'Install New Server', 
            'Update Existing Server',
            Separator(), 
            'Get Installed Server Version']
    }
    answers = prompt(what_to_do_prompt, style=custom_style_3)
    return answers['mainoption']

def ask_where_to_install():
    where_to_install_prompt = {
        'type': 'input',
        'name': 'install_path',
        'message': 'Where do you want to install factorio?',
    }
    answers = prompt(where_to_install_prompt)
    return answers['install_path']


def ask_path_to_update_server():
    path_to_update_server = {
        'type': 'input',
        'name': 'update_path',
        'message': 'Where is factorio installed? ',
    }
    answers = prompt(path_to_update_server)
    return answers['update_path']
# TODO better to use while loop than recursion!



def confirm_where_to_install(path):
    confirm_where_to_install = {
        'type': 'confirm',
        'name': 'confirm_where_to_install',
        'message': 'Are you sure you want to install in ' + path + " ?",
    }
    answers = prompt(confirm_where_to_install)
    return answers['confirm_where_to_install']


def confirm_where_to_update_server(path):
    confirm_where_to_update = {
        'type': 'confirm',
        'name': 'confirm_where_to_update',
        'message': 'Are you sure you want to update factorio in ' + path + " ?",
    }
    answers = prompt(confirm_where_to_update)
    return answers['confirm_where_to_update']

def main():
    option = ask_what_to_do()
    if(option == 'Install New Server'):
        install_path = ask_where_to_install()
        print(install_path)
        yesorno = confirm_where_to_install(install_path)
        if(yesorno):
            print("aright installing")
        if(yesorno == False):
            print("Please Try Again")
        
    if(option == 'Update Existing Server'):
        update_path = ask_path_to_update_server()
        print(update_path)
        yesorno = confirm_where_to_update_server(update_path)
        if(yesorno):
            print("Aright updating factorio")
        if(yesorno == False):
            print("please try again")
    
    if(option == 'Get Installed Server Version'):
        print("Getting the installed server version")
        



if __name__ == '__main__':
    main()
