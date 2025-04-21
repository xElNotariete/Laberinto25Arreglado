import time
from modo import Modo

class Agresivo(Modo):
    def __init__(self):
        super().__init__()

    def dormir(self, bicho):
        print("Descansando...")
        time.sleep(1)

    def __str__(self):
        return " : Agresivo"