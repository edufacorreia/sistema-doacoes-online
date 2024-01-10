from datetime import date

class Doacao:
    def __init__(self, id, doador, causa, data, valor):
        self.id = id
        self.doador = doador
        self.causa = causa
        self.data = data
        self.valor = valor

    def registrar_doacao(self):
        print(f"Doação registrada - ID: {self.id}, Doador: {self.doador}, Causa: {self.causa}, Data: {self.data}, Valor: {self.valor}")