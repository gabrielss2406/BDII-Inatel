from database import Database
from classes import *
from motoristaDAO import MotoristaDAO
from cli import MotoristaCLI

db = Database(database="Urbe", collection="motoristas")
motoristaModel = MotoristaDAO(database=db)

motoristaCLI = MotoristaCLI(motoristaModel)
motoristaCLI.run()
