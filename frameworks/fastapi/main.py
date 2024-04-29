from fastapi import FastAPI
import json
from enum import Enum


class Specie_Name(str, Enum):
    cats = "cats"
    dogs = "dogs"
    rabbit = "rabbits"
    sheep = "sheeps"


def load_sample_json (file):
    with open(file) as f:
        data = json.load(f)
        return data



app = FastAPI()

@app.get("/")
async def root():
    return {"messssage":"hello world"}


@app.get("/pets")
async def get_pets():
    db_pets = load_sample_json("../sample_data/pets.json")
    return db_pets


@app.get("/pets/{name}")
async def get_pets(name:str):
    db_pets = load_sample_json("../sample_data/pets.json")
    
    working = list(filter(lambda x: x['name'] == name, db_pets['pets']))
    return working

@app.get("/users")
async def read_users():
    return ["Rick", "Morty"]


# will send the first response since it is declared first
@app.get("/users")
async def read_users2():
    return ["Bean", "Elfo"]


@app.get("/pets/type/{species}")
async def get_species(species:Specie_Name ):
    if species is Specie_Name.cats:
        return {"species": "Cats",}
    if species == Specie_Name.dogs:
        return {"species":"Dogs"}

    return {"species":species, "message": "all messages"}