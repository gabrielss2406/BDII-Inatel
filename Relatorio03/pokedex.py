from database import Database
from helper.WriteAJson import writeAJson

class Pokedex:
    def __init__(self, database: Database):
        self.db = database

    def strong_against(self, name):
        weaknesses = self.db.collection.find({"name": name}, {"weaknesses":1, "_id":0})
        strong_against = self.db.collection.find({"type": {"$in": weaknesses[0]["weaknesses"]}})
        writeAJson(strong_against, "Strong_Against_"+name)
        return strong_against

    def weak_against(self, name):
        types = self.db.collection.find({"name": name}, {"type":1, "_id":0})
        weak_against = self.db.collection.find({"weaknesses": {"$all": types[0]["type"]}})
        writeAJson(weak_against, "Weak_Against_" + name)
        return weak_against

    def strong_against_type(self, type_name):
        pokemons = self.db.collection.find({"weaknesses": type_name})
        writeAJson(pokemons, "Strong_Against_Type_" + type_name)
        return pokemons

    def get_final_evolutions(self):
        final = self.db.collection.find({"next_evolution": {"$exists": False} })
        writeAJson(final, "Final_Evolutions")
        return final

