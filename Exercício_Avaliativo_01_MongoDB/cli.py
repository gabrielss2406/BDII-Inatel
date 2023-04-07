from classes import *


class SimpleCLI:
    def __init__(self):
        self.commands = {}

    def add_command(self, name, function):
        self.commands[name] = function

    def run(self):
        while True:
            command = input("Entre com um comando: ")
            if command == "quit":
                print("Goodbye!")
                break
            elif command in self.commands:
                self.commands[command]()
            else:
                print("Comando invalido, tente novamente.")


class MotoristaCLI(SimpleCLI):
    def __init__(self, motorista_model):
        super().__init__()
        self.motorista_model = motorista_model
        self.add_command("create", self.create_motorista)
        self.add_command("read", self.read_motorista)
        self.add_command("update", self.update_motorista)
        self.add_command("delete", self.delete_motorista)

    def create_motorista(self):
        notas = 0
        corridas = []
        nome = input("Entre com o nome do passageiro: ")
        documento = input("Entre com o documento do passageiro: ")
        passageiro = Passageiro(nome, documento)

        qntCorridas = int(input("Entre com quantas corridas serão cadastradas (1+):"))
        for i in range(qntCorridas):
            nota = int(input(f"{i + 1} - Entre com a nota: "))
            notas += nota
            distancia = float(input(f"{i + 1} - Entre com a distancia: "))
            valor = float(input(f"{i + 1} - Entre com o valor: "))
            corrida = Corrida(nota, distancia, valor, passageiro.to_dict())
            corridas.append(vars(corrida))

        motorista = Motorista(corridas, notas//qntCorridas)
        self.motorista_model.create_motorista(motorista)

    def read_motorista(self):#64301b64ff8fd6f295727421
        id = input("Entre com o id: ")
        motorista = self.motorista_model.read_motorista_by_id(id)
        if motorista:
            print(f"Nota média: {motorista['nota']}")
            for x in motorista['corridas']:
                print(f"==== Corrida ====")
                print(f"Nota: {x['nota']}")
                print(f"Distancia: {x['distancia']}")
                print(f"Valor: {x['valor']}")
                print(f"Nome passageiro: {x['passageiro']['nome']}")
                print(f"Documento passageiro: {x['passageiro']['documento']}")

    def update_motorista(self):
        id = input("Entre com o id: ")
        motorista = self.motorista_model.read_motorista_by_id(id)

        if motorista:
            corridas_new = []
            nome = input("Entre com o nome do passageiro: ")
            documento = input("Entre com o documento do passageiro: ")
            passageiro = Passageiro(nome, documento)
            qntCorridas = int(input("Entre com quantas corridas serão cadastradas (1+):"))
            for i in range(qntCorridas):
                nota = int(input(f"{i + 1} - Entre com a nota: "))
                distancia = float(input(f"{i + 1} - Entre com a distancia: "))
                valor = float(input(f"{i + 1} - Entre com o valor: "))
                corrida = Corrida(nota, distancia, valor, passageiro.to_dict())
                corridas_new.append(vars(corrida))
            self.motorista_model.update_motorista(id,corridas_new)

    def delete_motorista(self):
        id = input("Entre com o id: ")
        self.motorista_model.delete_motorista(id)

    def run(self):
        print("Bem vindo ao Motorista CLI!")
        print("Comandos disponiveis: create, read, update (add novas corridas), delete, quit")
        super().run()