from database import Database
from pokedex import Pokedex
from helper.WriteAJson import writeAJson

db = Database(database="pokedex", collection="pokemons")
db.resetDatabase()

pokedex = Pokedex(db)
pokedex.strong_against("Charmander")
pokedex.weak_against("Kakuna")
pokedex.strong_against_type("Fire")
pokedex.get_final_evolutions()