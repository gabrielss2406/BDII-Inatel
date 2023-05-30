'''
    Esse arquivo  contem os 3 exercicios, em ordem
    Parte 1 - Questão 1, chamando e exibindo as querys em query.py
    Parte 2 - Questão 2, chamando e exibindo as querys em query.py
    Parte 3 - Questão 3, chamando e exibindo as querys em teacher_crud.py
    Parte 4 - Rodando o TeacherCLI
'''
from database import Database
from query import Query
from teacher_crud import TeacherCRUD
from cli import TeacherCLI

db = Database("bolt://3.236.93.131:7687", "neo4j", "coxswain-tone-listing")

query_db = Query(db)
teacher_crud = TeacherCRUD(db)

# QUESTAO 1
print("==== QUESTÃO 1 ====\n")
result_a = query_db.questao1_a()
print("A) Busque pelo professor “Teacher” cujo nome seja “Renzo”, retorne o ano_nasc e o CPF.")
for i in result_a:
    print(i)

result_b = query_db.questao1_b()
print("B) Busque pelos professores “Teacher” cujo nome comece com a letra “M”, retorne o name e o cpf.")
for i in result_b:
    print(i)

result_c = query_db.questao1_c()
print("C) Busque pelos nomes de todas as cidades “City” e retorne-os.")
for i in result_c:
    print(i)

result_d = query_db.questao1_d()
print(
    "D) Busque pelas escolas “School”, onde o number seja maior ou igual a 150 e menor ou igual a 550, retorne o nome da escola, o endereço e o número.")
for i in result_d:
    print(i)

# QUESTAO 2
print("\n==== QUESTÃO 2 ====\n")
result_a = query_db.questao2_a()
print("A) Encontre o ano de nascimento do professor mais jovem e do professor mais velho.")
for record in result_a:
    print("Nome mais jovem:", record["professor_mais_jovem"])
    print("Ano nascimento mais jovem:", record["ano_nasc_professor_mais_jovem"])
    print("Nome mais jovem:", record["professor_mais_velho"])
    print("Ano nascimento mais jovem:", record["ano_nasc_professor_mais_velho"])

result_b = query_db.questao2_b()
print("B) Encontre a média aritmética para os habitantes de todas as cidades, use a propriedade “population”.")
for i in result_b:
    print(i)

result_c = query_db.questao2_c()
print("C) Encontre a cidade cujo CEP seja igual a “37540-000” e retorne o nome com todas as letras “a” substituídas por “A” .")
for i in result_c:
    print(i)

result_d = query_db.questao2_d()
print("D) Para todos os professores, retorne um caractere, iniciando a partir da 3ª letra do nome.")
for i in result_d:
    print(i)

# QUESTAO 3
print("\n==== QUESTÃO 3 ====\n")
teacher_crud.create(
    "Chris Lima",
    1956,
    "189.052.396-66"
)
result = teacher_crud.read("Chris Lima")
for i in result:
    print("Nome: ", i["t.name"])
    print("Ano de nascimento: ", i["t.ano_nasc"])
    print("Cpf: ", i["t.cpf"])
teacher_crud.update("Chris Lima", "162.052.777-77")
teacher_crud.delete("Chris Lima")

# CLI
print("\n==== CLI ====\n")
cli = TeacherCLI(teacher_crud)
cli.run()

db.close()
