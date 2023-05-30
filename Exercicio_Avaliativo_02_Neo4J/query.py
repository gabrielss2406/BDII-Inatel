class Query:
    def __init__(self, db):
        self.db = db

    def questao1_a(self):
        query = "MATCH (n:Teacher {name: 'Renzo'}) RETURN n.ano_nasc,n.cpf"
        result = self.db.execute_query(query)
        return ["Ano de nascimento: "+str(node["n.ano_nasc"])+" - CPF: "+node["n.cpf"] for node in result]

    def questao1_b(self):
        query = "MATCH (n:Teacher) WHERE n.name =~ 'M.*' return n.name,n.cpf"
        result = self.db.execute_query(query)
        return ["Nome: "+node["n.name"]+" - CPF: "+node["n.cpf"] for node in result]

    def questao1_c(self):
        query = "MATCH (n:City) return n.name"
        result = self.db.execute_query(query)
        return ["Nome: "+node["n.name"] for node in result]

    def questao1_d(self):
        query = "MATCH (n:School) WHERE n.number >= 150 AND n.number <= 550 return n.name,n.address,n.number"
        result = self.db.execute_query(query)
        return ["Nome: "+node["n.name"]+" - Endereco: "+node["n.address"]+" - Numero: "+str(node["n.number"]) for node in result]


    def questao2_a(self):
        query = "MATCH (t:Teacher) RETURN HEAD(COLLECT({name: t.name, ano_nasc: t.ano_nasc})).name as " \
                "professor_mais_jovem, HEAD(COLLECT({name: t.name, ano_nasc: t.ano_nasc})).ano_nasc as " \
                "ano_nasc_professor_mais_jovem, LAST(COLLECT({name: t.name, ano_nasc: t.ano_nasc})).name as " \
                "professor_mais_velho, LAST(COLLECT({name: t.name, ano_nasc: t.ano_nasc})).ano_nasc as " \
                "ano_nasc_professor_mais_velho "
        result = self.db.execute_query(query)
        return [node for node in result]

    def questao2_b(self):
        query = "MATCH (n:City) RETURN AVG(n.population) as MED_POP"
        result = self.db.execute_query(query)
        return ["Média da população: "+str(node["MED_POP"]) for node in result]

    def questao2_c(self):
        query = "MATCH (c:City {cep: '37540-000'}) RETURN REPLACE(c.name, 'a', 'A') as new_name"
        result = self.db.execute_query(query)
        return [node["new_name"] for node in result]

    def questao2_d(self):
        query = "MATCH (t:Teacher) RETURN SUBSTRING(t.name, 3, 1) AS new_name"
        result = self.db.execute_query(query)
        return [node["new_name"] for node in result]

