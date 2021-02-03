from __future__ import annotations
from abc import ABC, abstractmethod

class Command(ABC):
    """ Interfaz comando """
    @abstractmethod
    def execute(self):
        pass

class ComandoImprimir(Command):
    def __init__(self, payload):
        self._payload = payload
    def execute(self):
        print(self._payload)


class ComandoCalculoComplejo(Command):
    def __init__(self, receiver):
        self.receiver = receiver
    def execute(self):
        print('Realizando calculo complejo...')
        self.receiver.calculate_a()
        self.receiver.calculate_b()
    
class Calculador:
    def calculate_a(self):
        print('Calculando a...')

    def calculate_b(self):
        print('Calculando b...')

class Calculadora:
    _on_start = None
    _on_finish = None

    """
    Initialize commands.
    """

    def set_on_start(self, command: Command):
        self._on_start = command

    def set_on_finish(self, command: Command):
        self._on_finish = command

    def realizar_calculos(self):
        
        if isinstance(self._on_start, Command):
            self._on_start.execute()

        if isinstance(self._on_finish, Command):
            self._on_finish.execute()

if __name__ == '__main__':
    calculadora = Calculadora()
    calculador = Calculador()
    calculadora.set_on_start(ComandoCalculoComplejo(calculador))
    calculadora.set_on_finish(ComandoImprimir("La respuesta esta en tu corazon ...."))
    calculadora.realizar_calculos()
    