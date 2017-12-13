"""A generic RPG character generator."""
from random import randint



class Character(object):
    """Our Character object."""

    def __init__(self, name):
        self.name = name
        self.level = 1
        self.health = 0
        self.defense = 0
        self.strength = 0
        self.intelligence = 0
        self.charisma = 0
        self.dexterity = 0
        self.luck = 0
        self.equipment = []


def main():
    try:
        print_intro()
    except KeyboardInterrupt:
        print()
        print('Exiting!')


def make_character(user_choice, char_name):
    if user_choice == 'Fighter':
        character = Character(char_name)
        character.health = randint(10, 30)
        character.defense = randint(10, 20)
        character.strength = randint(10, 20)
        character.intelligence = randint(1, 10)
        character.charisma = randint(1, 10)
        character.dexterity = randint(5, 15)
        character.luck = randint(1, 10)
    elif user_choice == 'Mage':
        character = Character(char_name)
        character.health = randint(5, 15)
        character.defense = randint(1, 10)
        character.strength = randint(1, 10)
        character.intelligence = randint(10, 30)
        character.charisma = randint(1, 10)
        character.dexterity = randint(5, 15)
        character.luck = randint(1, 10)
    elif user_choice == 'Thief':
        character = Character(char_name)
        character.health = randint(5, 15)
        character.defense = randint(1, 10)
        character.strength = randint(5, 15)
        character.intelligence = randint(5, 10)
        character.charisma = randint(10, 20)
        character.dexterity = randint(10, 30)
        character.luck = randint(10, 20)
    elif user_choice == 'Cleric':
        character = Character(char_name)
        character.health = randint(5, 15)
        character.defense = randint(5, 15)
        character.strength = randint(5, 15)
        character.intelligence = randint(10, 20)
        character.charisma = randint(10, 20)
        character.dexterity = randint(1, 10)
        character.luck = randint(1, 10)
    return print_character_info(character)


def print_intro():
    intro = """
    +-----------------------------------+
    |                                   |
    |                                   |
    |          Welcome to the           |
    |        Character Creation         |
    |              Screen               |
    |                                   |
    |                                   |
    +-----------------------------------+

    Choose one of the following options:

    1. Fighter
    2. Mage
    3. Thief
    4. Cleric
    """
    print(intro)
    make_character(class_choice(), character_name())


def character_name():
    char_name = input('Name your character: ')
    really_sure = input("Are you sure about {}? y/n".format(char_name))
    if really_sure.lower() == 'y':
        return char_name
    else:
        character_name()


def class_choice():
    user_choice = input('>>> ')
    if user_choice == '1':
        return 'Fighter'
    elif user_choice == '2':
        return 'Mage'
    elif user_choice == '3':
        return 'Thief'
    elif user_choice == '4':
        return 'Cleric'
    else:
        raise ValueError("YOU DIDN'T FOLLOW THE RULES!!!!")



def print_character_info(char):
    info = """
    Here is your character:
    Name: {}
    Health: {}
    Defense: {}
    Strength: {}
    Intelligence: {}
    Charisma: {}
    Dexterity: {}
    Luck: {}
    """.format(char.name, char.health, char.defense, char.strength, char.intelligence, char.charisma, char.dexterity, char.luck)
    print(info)
    choice = input('If you want to re-choose press 1 otherwise press 2: ')
    if choice == '1':
        main()
    else:
        print('Enjoy!!')
        return


if __name__ == '__main__':
    main()
