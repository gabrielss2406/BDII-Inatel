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


class TeacherCLI(SimpleCLI):
    def __init__(self, crud):
        super().__init__()
        self.crud = crud
        self.add_command("create", self.create_teacher)
        self.add_command("read", self.read_teacher)
        self.add_command("update", self.update_teacher)
        self.add_command("delete", self.delete_teacher)

    def create_teacher(self):
        print("Criando professor")
        name = input("Nome do professor: ")
        ano_nasc = input("Ano de nascimento do professor: ")
        cpf = input("CPF do professor: ")
        try:
            self.crud.create(name, int(ano_nasc), cpf)
            print(f"Professor {name} criado!")
        except Exception as e:
            print(f"Erro ao criar professor! {e}")

    def read_teacher(self):
        print("Lendo professor")
        name = input("Nome do professor: ")
        try:
            result = self.crud.read(name)
            for i in result:
                print("Nome: ", i["t.name"])
                print("Ano de nascimento: ", i["t.ano_nasc"])
                print("Cpf: ", i["t.cpf"])
        except Exception as e:
            print(f"Erro ao ler professor! {e}")

    def update_teacher(self):
        print("Atualizando professor")
        name = input("Nome do professor: ")
        newCpf = input("Novo CPF do professor: ")
        try:
            self.crud.update(name,newCpf)
            print("Atualizado!")
        except Exception as e:
            print(f"Erro ao atualizar professor! {e}")

    def delete_teacher(self):
        print("Deletando professor")
        name = input("Nome do professor: ")
        try:
            self.crud.delete(name)
            print("Deletado!")
        except Exception as e:
            print(f"Erro ao deletar professor! {e}")