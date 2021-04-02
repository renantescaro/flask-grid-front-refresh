from threading import Thread
import random
import time
from datetime import datetime

class Dados(Thread):
    def __init__(self, **kwargs):
        super(Dados, self).__init__(**kwargs)
        self.id     = int(0)
        self.dados  = []
        self._canais = ['site', 'americanas', 'mercado livre', 'dafiti']


    def run(self):
        while True:
            self.dados.append(self._gerar())
            time.sleep(10)


    def get(self):
        return self.dados


    def _id(self):
        self.id = (self.id + 1)
        return self.id


    def _numero(self):
        return random.randint(10000, 30000)


    def _hora(self):
        now = datetime.now()
        return str(now.strftime("%H:%M:%S"))


    def _canal(self):
        return random.choice(self._canais)


    def _gerar(self):
        return {
            'id'     : self._id(),
            'numero' : self._numero(),
            'canal'  : self._canal(),
            'hora'   : self._hora()
        }