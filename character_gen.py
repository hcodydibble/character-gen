"""A generic RPG character generator."""
import random


class Character(object):
    """Our Character object."""

    def __init__(self, name=None):
        self.name = name
        self.level = 1
        self.health = 0
        self.defense = 0
        self.strength = 0
        self.intelligence = 0
        self.charisma = 0
        self.dexterity = 0
        self.luck = 0
        self.equipment = {'weapon': None, 'armor': None, 'misc': 0}
        self.gold = random.randint(50, 150)
        self.char = None

    def main(self):
        try:
            self.print_intro()
        except KeyboardInterrupt:
            print()
            print('Exiting!')

    def make_character(self, user_choice, char_name):
        if user_choice == 'Fighter':
            character = Character(char_name)
            character.health = random.randint(10, 30)
            character.defense = random.randint(10, 20)
            character.strength = random.randint(10, 20)
            character.intelligence = random.randint(1, 10)
            character.charisma = random.randint(1, 10)
            character.dexterity = random.randint(5, 15)
            character.luck = random.randint(1, 10)
        elif user_choice == 'Mage':
            character = Character(char_name)
            character.health = random.randint(5, 15)
            character.defense = random.randint(1, 10)
            character.strength = random.randint(1, 10)
            character.intelligence = random.randint(10, 30)
            character.charisma = random.randint(1, 10)
            character.dexterity = random.randint(5, 15)
            character.luck = random.randint(1, 10)
        elif user_choice == 'Thief':
            character = Character(char_name)
            character.health = random.randint(5, 15)
            character.defense = random.randint(1, 10)
            character.strength = random.randint(5, 15)
            character.intelligence = random.randint(5, 10)
            character.charisma = random.randint(10, 20)
            character.dexterity = random.randint(10, 30)
            character.luck = random.randint(10, 20)
        elif user_choice == 'Cleric':
            character = Character(char_name)
            character.health = random.randint(5, 15)
            character.defense = random.randint(5, 15)
            character.strength = random.randint(5, 15)
            character.intelligence = random.randint(10, 20)
            character.charisma = random.randint(10, 20)
            character.dexterity = random.randint(1, 10)
            character.luck = random.randint(1, 10)
        self.char = character
        return self.print_character_info(character)


    def print_intro(self):
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
        self.make_character(self.class_choice(), self.character_name())

    def character_name(self):
        char_name = input('Name your character: ')
        really_sure = input("Are you sure about {}? y/n: ".format(char_name))
        if really_sure.lower() == 'y':
            return char_name
        else:
            self.character_name()

    def class_choice(self):
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
            raise ValueError("The gods are a fickle bunch who have decided to strike you down before you even got started. Better luck next time.")

    def get_equipment(self):
        shopkeep_intro = """
        "Welcome to the shop! What would you like to shop for today?"

        1. Weapons
        2. Armor
        3. Misc
        """

        print(shopkeep_intro)
        print('Gold: {}'.format(self.gold))
        choice = input(">>> ")
        if choice == '1':
            self.buy_weapons()
        elif choice == '2':
            self.buy_armor()
        elif choice == '3':
            self.buy_misc()

    def buy_weapons(self):
        shopkeep_weapon = """
        "An excellent choice! Can't go off into the world without a way to defend yourself.
        What kind of weapon are you looking for?"

        1. Sword - 50G
        2. Stave - 20G
        3. Dagger - 10G
        4. Mace - 50G
        """
        print(shopkeep_weapon)
        weapon_choice = input(">>> ")
        if weapon_choice == '1':
            if self.gold < 50:
                print("Sorry, you don't have enough gold for that.")
                self.buy_weapons()
            print('There you are!')
            self.char.equipment['weapon'] = 'Sword'
            self.gold = self.gold - 50
            self.print_character_info_again(self.char)
        elif weapon_choice == '2':
            if self.gold < 20:
                print("Sorry, you don't have enough gold for that.")
                self.buy_weapons()
            print('There you are!')
            self.char.equipment['weapon'] = 'Stave'
            self.gold = self.gold - 20
            self.print_character_info_again(self.char)
        elif weapon_choice == '3':
            if self.gold < 10:
                print("Sorry, you don't have enough gold for that.")
                self.buy_weapons()
            print('There you are!')
            self.char.equipment['weapon'] = 'Dagger'
            self.gold = self.gold - 10
            self.print_character_info_again(self.char)
        elif weapon_choice == '4':
            if self.gold < 50:
                print("Sorry, you don't have enough gold for that.")
                self.buy_weapons()
            print('There you are!')
            self.char.equipment['weapon'] = 'Mace'
            self.gold = self.gold - 50
            self.print_character_info_again(self.char)
        else:
            raise ValueError("The shopkeep doesn't appreciate your tone and decides to cut your adventure short. Better luck next time.")

    def buy_armor(self):
        shopkeep_armor = """
        "A wise choice. Going on an adventure without protection would be a poor idea.
        What kind of armor are you looking for?"

        1. Heavy - 50G
        2. Medium - 35G
        3. Light - 20G
        """
        print(shopkeep_armor)
        armor_choice = input(">>> ")
        if armor_choice == '1':
            if self.gold < 50:
                print("Sorry, you don't have enough gold for that.")
                self.buy_weapons()
            print('There you are!')
            self.char.equipment['armor'] = 'Heavy'
            self.gold = self.gold - 50
            self.print_character_info_again(self.char)
        elif armor_choice == '2':
            if self.gold < 35:
                print("Sorry, you don't have enough gold for that.")
                self.buy_weapons()
            print('There you are!')
            self.char.equipment['armor'] = 'Medium'
            self.gold = self.gold - 35
            self.print_character_info_again(self.char)
        elif armor_choice == '3':
            if self.gold < 20:
                print("Sorry, you don't have enough gold for that.")
                self.buy_weapons()
            print('There you are!')
            self.char.equipment['armor'] = 'Light'
            self.gold = self.gold - 20
            self.print_character_info_again(self.char)
        else:
            raise ValueError("The shopkeep doesn't appreciate your tone and decides to cut your adventure short. Better luck next time.")

    def buy_misc(self):
        shopkeep_misc = """
        "Oh...I was hoping you wouldn't choose this. Ummm...well I guess I have some of this wa....
        POTIONS! I have potions for sale! 10G each. How many would you like?"
        """
        print(shopkeep_misc)
        number_of_potions = input(">>> ")
        if number_of_potions == '0':
            print("Probably a good choice, it was just water anyways.")
        elif self.gold < int(number_of_potions) * 10:
            print("Sorry, you don't have enough gold for that many.")
            self.buy_misc()
        print("Excellent....Excellent! You won't regret this decision. Not. At. All.")
        self.char.equipment['misc'] += int(number_of_potions)
        self.gold = self.gold - int(number_of_potions) * 10
        self.print_character_info_again(self.char)


    def print_character_info(self, char):
        info = """
        Here is your character:
        Name: {}
        Level: {}
        Health: {}
        Defense: {}
        Strength: {}
        Intelligence: {}
        Charisma: {}
        Dexterity: {}
        Luck: {}
        Equipment:
            Weapon: {}
            Armor: {}
            Potions: {}
        """.format(char.name,
                   char.level,
                   char.health,
                   char.defense,
                   char.strength,
                   char.intelligence,
                   char.charisma,
                   char.dexterity,
                   char.luck,
                   char.equipment['weapon'],
                   char.equipment['armor'],
                   char.equipment['misc'])
        print(info)
        choice = input('If you want to re-choose press 1 otherwise press 2 to continue: ')
        if choice == '1':
            self.main()
        else:
            self.get_equipment()

    def print_character_info_again(self, char):
        info = """
        Here is your character:
        Name: {}
        Level: {}
        Health: {}
        Defense: {}
        Strength: {}
        Intelligence: {}
        Charisma: {}
        Dexterity: {}
        Luck: {}
        Equipment:
            Weapon: {}
            Armor: {}
            Potions: {}
        """.format(char.name,
                   char.level,
                   char.health,
                   char.defense,
                   char.strength,
                   char.intelligence,
                   char.charisma,
                   char.dexterity,
                   char.luck,
                   char.equipment['weapon'],
                   char.equipment['armor'],
                   char.equipment['misc'])
        print(info)
        moar = input('Would you like to buy more equipment? You have {} gold left. y/n: '.format(self.gold))
        if moar == 'y':
            self.get_equipment()
        else:
            print('You depart on your grand adventure. Good luck!')
            return


if __name__ == '__main__':
    start = Character()
    start.main()
