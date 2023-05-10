class Match:
    def __init__(self, db):
        self.db = db

    def create_match(self, players_list, result):
        query_c = "CREATE (m:Match{result: $result})" # create part of query
        query_m = "MATCH " # match part of query
        i=0
        parameters = {"result": result}
        for player_name in players_list:
            if i!=0:
                query_m += ", "
            query_m += "(p"+str(i)+":Player{name: $player_name"+str(i)+"})"
            query_c += ", (m)-[:PARTICIPATED]->(p"+str(i)+")"
            param_aux = "player_name"+str(i)
            parameters.update({param_aux: player_name})
            i+=1

        query_m += "\n"
        query = query_m+query_c
        self.db.execute_query(query, parameters)

    def delete_match(self, match_result): # Não gostei de como ficou, mas nao pensei em nada melhor
        query = "MATCH (m:Match {result: $match_result})" \
                "DETACH DELETE m"
        parameters = {"match_result": match_result}
        self.db.execute_query(query, parameters)

    def get_match(self, match_result):
        query = "MATCH (m:Match{result: $match_result}), (m:Match)-[:PARTICIPATED]->(p:Player) RETURN p.name"
        parameters = {"match_result": match_result}
        result = self.db.execute_query(query, parameters)
        return [node["p.name"] for node in result]

    def get_match_per_player(self, player_name):
        query = "MATCH (p:Player{name: $player_name}), (m:Match)-[:PARTICIPATED]->(p:Player) RETURN m.result"
        parameters = {"player_name": player_name}
        result = self.db.execute_query(query, parameters)
        return [node["m.result"] for node in result]

    def update_match(self, result, new_result):
        query = "MATCH (m:Match {result: $result})" \
                "SET m.result = $new_result"
        parameters = {"result": result, "new_result": new_result}
        self.db.execute_query(query, parameters)