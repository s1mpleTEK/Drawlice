import random

dice_art = {1: "-----\n|   |\n| o |\n|   |\n-----",
            2: "-----\n|o  |\n|   |\n|  o|\n-----",
            3: "-----\n|o  |\n| o |\n|  o|\n-----",
            4: "-----\n|o o|\n|   |\n|o o|\n-----",
            5: "-----\n|o o|\n| o |\n|o o|\n-----",
            6: "-----\n|o o|\n|o o|\n|o o|\n-----"}

class Dice:
    """
    Le status correspond à l'attaque ou la defense du joueur;
    il est défaut en 'None' mais peut passer en 'Atk' ou en 'Def' selon le chiffre de _status.

    Le stock correspond à la somme des nombres stocker après un double ou un triple.

    On dit qu'il y a eu un 'double' quand deux dès possèdent un chiffre identique.
    On dit qu'il y a eu un 'triple' quand tous les dès possèdent un chiffre identique.
    """
    def __init__(self):
        self.status = None
        self._status = 0
        self.magic = 0,
        self.physic = 0
        self.stock = 0

    # Permet d'afficher les dès
    def display(self):
        print(f"Blanc: {self._status}  Bleu: {self.magic}  Rouge: {self.physic}")

    # Permet de lancer les dès
    def roll(self):
        self.status = self.set_status(random.randint(1, 6))
        self.magic = random.randint(1, 6)
        self.physic = random.randint(1, 6)
        self.display()
        self.db_tp_verification([self._status, self.magic, self.physic])

    # Permet de changer la valuer de status et de _status
    def set_status(self, number):
        self._status = number
        return 'Def' if (number % 2 == 0) else 'Atk'

    # Permet la vérifiaction des doubles ou des triples
    def db_tp_verification(self, dices):
        counter = 0
        _sum = []
        for i in range(len(dices)):
            if dices[i] == dices[i-1] or dices[i] == dices[i-2]:
                _sum.append(dices[i])
                counter += 1

        if len(_sum) == 2:
            print("wow un double!!")
            self.stock += sum(_sum)
            print(f"Stock: {self.stock}")
            return self.roll()
        elif len(_sum) == 3:
            print("wow un triple!!")
            self.stock += sum(_sum)
            print(f"Stock: {self.stock}")
            return self.roll()