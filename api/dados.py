from threading import Thread
import random
import time

class Dados(Thread):
    def __init__(self, **kwargs):
        super(Dados, self).__init__(**kwargs)
        self.id    = int(0)
        self.dados = []


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
        return random.randint(100, 300)


    def _hora(self):
        return time.time()


    def _gerar(self):
        return {
            'id'     : self._id(),
            'numero' : self._numero(),
            'hora'   : self._hora()
        }