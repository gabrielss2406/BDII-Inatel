class Player:
    def __init__(self, db):
        self.db = db

    def create_player(self, player_name):
        query = "CREATE (:Player {name: $player_name})"
        parameters = {"player_name": player_name}
        self.db.execute_query(query, parameters)

    def update_player(self, player_name, new_player_name):
        query = "MATCH (p:Player {name: $player_name})" \
                "SET p.name = $new_player_name"
        parameters = {"player_name": player_name, "new_player_name": new_player_name}
        self.db.execute_query(query, parameters)

    def delete_player(self, player_name):
        query = "MATCH (p:Player {name: $player_name})" \
                "DETACH DELETE p"
        parameters = {"player_name": player_name}
        self.db.execute_query(query, parameters)

    def get_players(self):
        query = "MATCH (p:Player) return p.name"
        result = self.db.execute_query(query)
        return [node["p.name"] for node in result]
