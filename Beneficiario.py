class Beneficiario:
    def __init__(self, id, nome, email, endereco, causa_beneficiada, historico_doacoes_recebidas):
        self.id = id
        self.nome = nome
        self.email = email
        self.endereco = endereco
        self.causa_beneficiada = causa_beneficiada
        self.historico_doacoes_recebidas = []

    def adicionar_causa(self):
        pass

    def visualizar_doadores(self):
        pass
