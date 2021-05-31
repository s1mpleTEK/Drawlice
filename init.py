from src.main import main
from src.Class.Game_Class import Game

if __name__ == "__main__":
    try:
        main(Game())
    except Exception:
        exit(-1)