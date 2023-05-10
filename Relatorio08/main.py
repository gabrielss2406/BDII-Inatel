from database import Database
from player import Player
from match import Match

db = Database("bolt://44.201.66.198:7687","neo4j","fault-interchange-brush")
db.drop_all()

player_db = Player(db)
match_db = Match(db)

# Criando players
player_db.create_player("ElPandaDLMX")
player_db.create_player("Xicoloso")
player_db.create_player("Mestre_Tiao")
player_db.create_player("Hollow Fenrir")
player_db.create_player("Ewel")

# Atualizando player
player_db.update_player("Ewel", "ewelzika1")

# Deletando player
player_db.delete_player("Hollow Fenrir")

# Retornando players
print("PLAYERS: ")
for player in player_db.get_players():
    print(player)

# Criando match
match_db.create_match(["ElPandaDLMX", "Xicoloso"], "ElPandaDLMX vence de Xicoloso")
match_db.create_match(["ElPandaDLMX", "Xicoloso", "ewelzika1"], "Xicoloso vence de ElPandaDLMX")
match_db.create_match(["Xicoloso", "ewelzika1"], "Xicoloso PERDE de ewelzika1")

# Deletando match
match_db.delete_match("ElPandaDLMX vence de Xicoloso")

# Buscando partida especifica
print("\nPLAYERS DESSA MATCH: ")
for match in match_db.get_match("Xicoloso vence de ElPandaDLMX"):
    print(match)

# Atualizando um resultado de partida
match_db.update_match("Xicoloso vence de ElPandaDLMX", "Xicoloso perde de ElPandaDLMX")

# Buscando pelo player
print("\nHISTÓRICO (Xicoloso):")
for match in match_db.get_match_per_player("Xicoloso"):
    print(match)

db.close()