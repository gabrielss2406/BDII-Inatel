class Query:
    def __init__(self, db):
        self.db = db

    def profissionais(self, profissao):
        query = "MATCH (n:{profissao}) RETURN n.nome"
        query = query.format(profissao=profissao)
        result = self.db.execute_query(query)
        return [node["n.nome"] for node in result]

    def pais_de(self, nome):
        query = "MATCH (n1:Pessoa {nome: $nome})-[:PAI_DE]-(n2:Pessoa) RETURN n2.nome"
        parameters = {"nome": nome}
        result = self.db.execute_query(query,parameters)
        return [node["n2.nome"] for node in result]

    def donos_de(self, nome):
        query = "MATCH (n1:Pessoa)-[:DONO_DE]-(n2:Pet {nome: $nome}) RETURN n1.nome"
        parameters = {"nome": nome}
        result = self.db.execute_query(query,parameters)
        return [node["n1.nome"] for node in result]
