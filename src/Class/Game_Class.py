from .Player_Class import Player

class Game(Player):
    def __init__(self, more_player = False):
        self.more_player = more_player
        self.players = [Player()]
        self.players.append(Player()) if self.more_player else self.players.append(Player(ai = True))
    
    def __players__(self):
        if self.more_player:
            for i in range(len(self.players)):
                print(f"Pseudo du joueur {i+1}:")
                self.players[i].set_name()
        else:
            print(f"Pseudo du joueur 1:")
            self.players[0].set_name()
        print()

    def start(self):
        print("~~~Drawlice~~~")
        print("\nBienvenu(e) sur Drawlice")
        print("Le premier jeu où tu gagnes seulement avec ta chance!")
        print("Alors il y aura combien de joueur(s)? (1 ou 2)")
        tmp = input("> ")
        while tmp not in ["1", "2"]:
            print("#MAUVAISE ENTRÉ")
            tmp = input("> ")
        self.more_player = True if tmp == "2" else  False
        self.__players__()

    def combat(self):
        tmp = 0
        player1 = self.players[0]
        player2 = self.players[1]
        print()
        for player in self.players:
            player.set_status()
            if player.status == "Atk":
                print(f"{player.name} fait une attaque", end=" ")
                print("magique" if "magic" in player.dmg else "physique", end=" ")
                print("de", player.dmg['magic'] if "magic" in player.dmg else player.dmg['physic'])
            else:
                print(f"{player.name} fait une défense", end=" ")
                print("magique" if "magic" in player.dmg else "physique", end=" ")
                print("de", player.dmg['magic'] if "magic" in player.dmg else player.dmg['physic'])
        print()
        if player1.status == "Atk" and player2.status == "Def":
            if "magic" in player1.dmg and "magic" in player2.dmg:
                tmp = player1.dmg["magic"]-player2.dmg["magic"] if player1.dmg["magic"]-player2.dmg["magic"] > 0 else 0
                player2.pv -= tmp
                print(f"{player1.name} inflige {tmp} dégats magiques à {player2.name}")
            elif "physic" in player1.dmg and "physic" in player2.dmg:
                tmp = player1.dmg["physic"]-player2.dmg["physic"] if player1.dmg["physic"]-player2.dmg["physic"] > 0 else 0
                player2.pv -= tmp
                print(f"{player1.name} inflige {tmp} dégats physiques à {player2.name}")
            else:
                tmp = player1.dmg["magic" if "magic" in player1.dmg else "physic"]
                player2.pv -= tmp
                print(f"{player1.name} inflige {tmp} dégats", end=" ")
                print("magique" if "magic" in player1.dmg else "physique", end=" ")
                print(f"à {player2.name}")
        elif player2.status == "Atk" and player1.status == "Def":
            if "magic" in player1.dmg and "magic" in player2.dmg:
                tmp = player2.dmg["magic"]-player1.dmg["magic"] if player2.dmg["magic"]-player1.dmg["magic"] > 0 else 0
                player1.pv -= tmp
                print(f"{player2.name} inflige {tmp} dégats magiques à {player1.name}")
            elif "physic" in player1.dmg and "physic" in player2.dmg:
                tmp = player2.dmg["physic"]-player1.dmg["physic"] if player2.dmg["physic"]-player1.dmg["physic"] > 0 else 0
                player1.pv -= tmp
                print(f"{player2.name} inflige {tmp} dégats physiques à {player1.name}")
            else:
                tmp = player2.dmg["magic" if "magic" in player2.dmg else "physic"]
                player1.pv -= tmp
                print(f"{player2.name} inflige {tmp} dégats", end=" ")
                print("magique" if "magic" in player2.dmg else "physique", end=" ")
                print(f"à {player1.name}")
        elif player1.status == "Atk" and player2.status == "Atk":
            if "magic" in player1.dmg:
                tmp = player1.dmg["magic"]
                player2.pv -= tmp
                print(f"{player1.name} inflige {tmp} dégats magiques à {player2.name}")
            else:
                tmp = player1.dmg["physic"]
                player2.pv -= tmp
                print(f"{player1.name} inflige {tmp} dégats physiques à {player2.name}")
            if "magic" in player2.dmg:
                tmp = player2.dmg["magic"]
                player1.pv -= tmp
                print(f"{player2.name} inflige {tmp} dégats magiques à {player1.name}")
            else:
                tmp = player2.dmg["physic"]
                player1.pv -= tmp
                print(f"{player2.name} inflige {tmp} dégats physiques à {player1.name}")
        elif player1.status == "Def" and player2.status == "Def":
            print(f"{player1.name} et {player2.name} restent sur la défensive")
        print()
        return

    def loop(self):
        print("Le combat commence!")
        print(f"{self.players[0].name} Vs {self.players[1].name}")
        while True:
            for player in self.players: print(f"{player.name}: {player.pv}/30")
            if self.players[0].pv <= 0 and self.players[1].pv <= 0:
                print("Égalité")
                return
            for i in range(len(self.players)):
                if self.players[i].pv <= 0:
                    print(f"Joueur {self.players[i+1].name} gagne!")
                    return
                print(f"\nTour de {self.players[i].name}:")
                self.players[i].dice.roll()
            self.combat()