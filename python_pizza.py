# -*- coding: utf-8 -*-

from __future__ import print_function, unicode_literals
import regex

from pprint import pprint
from PyInquirer import style_from_dict, Token, prompt
from PyInquirer import Validator, ValidationError

import colorama
from colorama import Fore
from colorama import Style


style = style_from_dict({
    Token.QuestionMark: '#33CC00 bold',
    Token.Selected: '#2196f3 bold', #default
    Token.Instruction: '',  # default
    Token.Answer: '#E91E63 bold',
    Token.Question: '',
})


class PhoneNumberValidator(Validator):
    def validate(self, document):
        ok = regex.match('^(?:(?:\+|00)33[\s.-]{0,3}(?:\(0\)[\s.-]{0,3})?|0)[1-9](?:(?:[\s.-]?\d{2}){4}|\d{2}(?:[\s.-]?\d{3}){2})$', document.text)
        if not ok:
            raise ValidationError(
                message='Veuillez enter un numéro de téléphone valide',
                cursor_position=len(document.text))  # Move cursor to end


class NumberValidator(Validator):
    def validate(self, document):
        try:
            int(document.text)
        except ValueError:
            raise ValidationError(
                message='Veuillez entrer un numéro de téléphone',
                cursor_position=len(document.text))  # Move cursor to end


colorama.init()
print(Fore.GREEN + Style.BRIGHT + "-> Salut, " + Style.RESET_ALL + Style.BRIGHT + "bienvenue chez " + Style.RESET_ALL + Fore.RED + Style.BRIGHT + "Pizza Python !" + Style.RESET_ALL)
print("")
print(Fore.BLUE + Style.BRIGHT + "-> Créé " + Style.RESET_ALL + Style.BRIGHT + "par " + Style.RESET_ALL + Fore.RED + Style.BRIGHT + "MyWare" + Style.RESET_ALL)
print("")
print("--------------------------------------------------")
print("")
print("")

questions = [
    {
        'type': 'confirm',
        'name': 'livraison',
        'message': 'Voulez vous être livré ?',
        'default': True
    },
    {
        'type': 'input',
        'name': 'nom',
        'message': 'Quel est votre nom ?',
    },
    {
        'type': 'input',
        'name': 'téléphone',
        'message': 'Quel est votre numéro de téléphone ?',
        'validate': PhoneNumberValidator
    },
    {
        'type': 'rawlist',
        'name': 'taille',
        'message': 'Quelle est la taille de pizza que vous voulez ?',
        'choices': ['Grand', 'Moyen', 'Petit'],
        'filter': lambda val: val.lower()
    },
    {
        'type': 'input',
        'name': 'quantité',
        'message': 'Combien de pizzas voulez-vous ?',
        'validate': NumberValidator,
        'filter': lambda val: int(val)
    },
    {
        'type': 'checkbox',
        'name': 'garnitures',
        'message': 'Garnitures :',
        'choices': [
            {
                'key': 'c',
                'name': 'Chorizo',
                'value': 'chorizo'
            },
            {
                'key': 'j',
                'name': 'Jambon',
                'value': 'jambon'
            },
            {
                'key': 'm',
                'name': 'Mozzarella',
                'value': 'mozzarella'
            },
            {
                'key': 'e',
                'name': 'Emmental',
                'value': 'emmental'
            },
            {
                'key': 'h',
                'name': 'Champignon',
                'value': 'champignon'
            }
        ]
    },
    {
        'type': 'list',
        'name': 'boisson',
        'message': 'Vous pouvez aussi avoir une boisson gratuite :',
        'choices': ['Eau', 'Pepsi', '7up', 'Coca-Cola', 'Fanta', 'Jus d\'orange', 'Jus de pomme']
    },
    {
        'type': 'input',
        'name': 'commentaire',
        'message': 'Un commentaire ?',
        'default': 'Tout va bien, merci !'
    },
    {
        'type': 'list',
        'name': 'cadeau',
        'message': 'Parce que vous avec laissez un commentaire, vous gagnez un cadeau à choisir entre :',
        'choices': ['Gâteau', 'Frites', 'Jouet'],
        'when': lambda answers: answers['commentaire'] != 'Tout va bien, merci !'
    }
]

answers = prompt(questions, style=style)
print("")
print("--------------------------------------------------")
print("")
print(Fore.YELLOW + 'Reçu de commande : ' + Style.RESET_ALL)
pprint(answers)

print("")
print("--------------------------------------------------")
print("")
input("Appuyez sur ENTRÉE pour terminer le programme.")
