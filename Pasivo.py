import time
from modo import Modo

class Pasivo(Modo):
    def __init__(self):
        super().__init__()

    def dormir(self, bicho):
        print(" ... ")
        time.sleep(3)

    def __str__(self):
        return ": Pasivo"