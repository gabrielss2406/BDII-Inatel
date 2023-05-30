from database import Database
from query import Query

db = Database("bolt://100.26.251.2:7687","neo4j","quarters-receivers-task")

query_db = Query(db)

print("aposentados:", query_db.profissionais("Aposentado"))

print("pais de Gabriel:", query_db.pais_de("Gabriel"))
print("pais de Rosemary:", query_db.pais_de("Rosemary"))

print("donos de Tufão:", query_db.donos_de("Tufão"))

db.close()