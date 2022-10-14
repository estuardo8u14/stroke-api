from ast import Str
from fastapi.middleware.cors import CORSMiddleware
import mysql.connector
from pydantic import BaseModel
import uuid
from datetime import datetime
from typing import Union 
from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session
from . import crud, models, schemas
from .database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()
# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class Item(BaseModel):
    table: str
    name: str
    antecedentes: str
    sintomas: str
    entrada: str
    presión: str
    glucometro: str
    extra: str
    Nivel: str
    Preguntas:str 
    Ordenes: str
    Mirada: str
    Campos: str
    Paresia: str
    MotorMsDer: str
    MotorMsizq: str
    MotorMiDer: str
    MotorMiizq: str
    Ataxia: str
    Sensibilidad: str
    Lenguaje: str
    Disartria: str
    Extincion: str
    resultC: str


class Item2(BaseModel):
    table: str
    name: str
    Hyper: str
    Rankin: str
    Age: str
    Glucose: str
    Oneset: str
    Baseline: str
    resultD: str
    
    

class Item4(BaseModel):
    table: str
    name: str
    Diabetes: str
    Rankin: str
    Age: str
    resultH: str

class Item5(BaseModel):
    table: str
    name: str
    Blood: str
    Infarct: str
    Artery: str
    Age: str
    Nih: str
    resultS: str

class Time(BaseModel):
    tot_time: int
    name: str

@app.get("/")
def read_root():

    return "Stroke API"


@app.post("/post_sorted", response_model=Item)
def post_data(item: Item, db: Session = Depends(get_db)):

    mydb = mysql.connector.connect(
        host="sql8.freesqldatabase.com",
        user="sql8521469",
        password="fcge8DjTzk",
        database="sql8521469"
    )
    print(type(item))

    mycursor = mydb.cursor()

    sql = "INSERT INTO "+ item.table +" (name, Antecedentes, Sintomas, Entrada, Presión, Glucometro, Extra, Nivel, Preguntas, Ordenes, Mirada, Campos, Paresia, MotorMsDer, MotorMsizq, MotorMiDer, MotorMiizq, Ataxia, Sensibilidad, Lenguaje, Disartria, Extincion, resultC) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
    val = (
        item.name,
        item.antecedentes,
        item.sintomas,
        item.entrada,
        item.presión,
        item.glucometro,
        item.extra,
        item.Nivel,
        item.Preguntas,
        item.Ordenes,
        item.Mirada,
        item.Campos,
        item.Paresia,
        item.MotorMsDer,
        item.MotorMsizq,
        item.MotorMiDer,
        item.MotorMiizq,
        item.Ataxia,
        item.Sensibilidad,
        item.Lenguaje,
        item.Disartria,
        item.Extincion,
        item.resultC
    )
    mycursor.execute(sql, (val))

    mydb.commit()

    if(int(mycursor.rowcount) > 0):
        return True
    
    else:
        return False


@app.post("/post_dragon", response_model=Item2)
def post_dragon(item2: Item2):

    mydb = mysql.connector.connect(
        host="sql8.freesqldatabase.com",
        user="sql8521469",
        password="fcge8DjTzk",
        database="sql8521469"
    )
    print(type(item2))

    mycursor = mydb.cursor()

    sql = "INSERT INTO "+ item2.table +" (name, Hyper, Rankin, Age, Glucose, Oneset, Baseline, resultD) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
    val = (
        item2.name,
        item2.Hyper,
        item2.Rankin,
        item2.Age,
        item2.Glucose,
        item2.Oneset,
        item2.Baseline,
        item2.resultD
    )
    mycursor.execute(sql, (val))

    mydb.commit()

    if(int(mycursor.rowcount) > 0):
        return True
    
    else:
        return False


@app.post("/post_sedan", response_model=Item5)
def post_dragon(item5: Item5):

    mydb = mysql.connector.connect(
        host="sql8.freesqldatabase.com",
        user="sql8521469",
        password="fcge8DjTzk",
        database="sql8521469"
    )

    mycursor = mydb.cursor()

    sql = "INSERT INTO "+ item5.table +" (name, Blood, Infarct, Artery, Age, Nih, resultS) VALUES (%s, %s, %s, %s, %s, %s, %s)"
    val = (
        item5.name,
        item5.Blood,
        item5.Infarct,
        item5.Artery,
        item5.Age,
        item5.Nih,
        item5.resultS
    )
    mycursor.execute(sql, (val))

    mydb.commit()

    if(int(mycursor.rowcount) > 0):
        return True
    
    else:
        return False


@app.post("/post_hat", response_model=Item4)
def post_hat(item4: Item4):

    mydb = mysql.connector.connect(
        host="sql8.freesqldatabase.com",
        user="sql8521469",
        password="fcge8DjTzk",
        database="sql8521469"
    )
    print(type(item4))

    mycursor = mydb.cursor()

    sql = "INSERT INTO "+ item4.table +" (name, Diabetes, Rankin, Age, resultH) VALUES (%s, %s, %s, %s, %s)"
    val = (
        item4.name,
        item4.Diabetes,
        item4.Rankin,
        item4.Age,
        item4.resultH
    )
    mycursor.execute(sql, (val))

    mydb.commit()

    if(int(mycursor.rowcount) > 0):
        return True
    
    else:
        return False
    

@app.post("/post_time", response_model=Time)
def post_time(time: Time):
    mydb = mysql.connector.connect(
        host="sql8.freesqldatabase.com",
        user="sql8521469",
        password="fcge8DjTzk",
        database="sql8521469"
    )

    mycursor = mydb.cursor()
    name = time.name
    name = str(name)

    sql = "UPDATE hat SET tot_time = %s WHERE name = %s"
    val = (
       time.tot_time,
       name
    )
    mycursor.execute(sql, val)

    mydb.commit()

    if(int(mycursor.rowcount) > 0):
        return True
    
    else:
        return False

@app.get("/get_data")
def get_data():
    mydb = mysql.connector.connect(
        host="sql8.freesqldatabase.com",
        user="sql8521469",
        password="fcge8DjTzk",
        database="sql8521469"
    )

    mycursor = mydb.cursor()

    sql = "SELECT id, name, Antecedentes, Sintomas FROM sorter"
    mycursor.execute(sql)
    results = mycursor.fetchall()

    
    data = []
    
    print(results)

    for result in results:
        dict = {}
        print("id :", result[0], "name :", result[1] )
        dict["id"] = result[0]
        dict["Antecedentes"] = result[2]
        dict["name"] = result[1]
        dict["date"] = result[3]

        data.append(dict)

    print(data)
    return data


@app.get("/get_sorter")
def get_data(id : str):
    mydb = mysql.connector.connect(
        host="sql8.freesqldatabase.com",
        user="sql8521469",
        password="fcge8DjTzk",
        database="sql8521469"
    )

    mycursor = mydb.cursor()

    sql = "SELECT * FROM sorter where id="+ id +""
    mycursor.execute(sql)
    results = mycursor.fetchall()

    
    data = []
    
    print(results)

    for result in results:
        dict = {}
        print("id :", result[0], "name :", result[1] )
        dict["id"] = result[0]
        dict["name"] = result[1]
        dict["Antecedentes"] = result[2]
        dict["Sintomas"] = result[3]
        dict["Entrada"] = result[4]
        dict["Presión"] = result[5]
        dict["Glucometro"] = result[6]
        dict["Extra"] = result[7]
        dict["Nivel"] = result[8]
        dict["Preguntas"] = result[9]
        dict["Ordenes"] = result[10]
        dict["Mirada"] = result[11]
        dict["Campos"] = result[12]
        dict["Paresia"] = result[13]
        dict["MotorMsDer"] = result[14]
        dict["MotorMsizq"] = result[15]
        dict["MotorMiDer"] = result[16]
        dict["MotorMiizq"] = result[17]
        dict["Ataxia"] = result[18]
        dict["Sensibilidad"] = result[19]
        dict["Lenguaje"] = result[20]
        dict["Disartria"] = result[21]
        dict["Extincion"] = result[22]
        dict["resultC"] = result[23]

        data.append(dict)

    print(data)
    return data
    
@app.get("/get_dragon")
def get_data(id : str):
    mydb = mysql.connector.connect(
        host="sql8.freesqldatabase.com",
        user="sql8521469",
        password="fcge8DjTzk",
        database="sql8521469"
    )

    mycursor = mydb.cursor()

    sql = "SELECT * FROM dragon where id="+ id +""
    
    mycursor.execute(sql)
    results = mycursor.fetchall()

    
    data = []
    
    print(results)

    for result in results:
        dict = {}
        print("id :", result[0], "name :", result[1] )
        dict["id"] = result[0]
        dict["name"] = result[1]
        dict["Hyper"] = result[2]
        dict["Rankin"] = result[3]
        dict["Age"] = result[4]
        dict["Glucose"] = result[5]
        dict["Oneset"] = result[6]
        dict["Baseline"] = result[7]
        dict["resultD"] = result[8]

        data.append(dict)

    print(data)
    return data
    


@app.get("/get_sedan")
def get_data(id : str):
    mydb = mysql.connector.connect(
        host="sql8.freesqldatabase.com",
        user="sql8521469",
        password="fcge8DjTzk",
        database="sql8521469"
    )

    mycursor = mydb.cursor()

    sql = "SELECT * FROM sedan where id="+ id +""
    
    mycursor.execute(sql)
    results = mycursor.fetchall()

    
    data = []
    
    print(results)

    for result in results:
        dict = {}
        print("id :", result[0], "name :", result[1] )
        dict["id"] = result[0]
        dict["name"] = result[1]
        dict["Blood"] = result[2]
        dict["Infarct"] = result[3]
        dict["Artery"] = result[4]
        dict["Age"] = result[5]
        dict["Nih"] = result[6]
        dict["resultS"] = result[7]

        data.append(dict)

    print(data)
    return data
    


@app.get("/get_hat")
def get_data(id : str):
    mydb = mysql.connector.connect(
        host="sql8.freesqldatabase.com",
        user="sql8521469",
        password="fcge8DjTzk",
        database="sql8521469"
    )

    mycursor = mydb.cursor()

    sql = "SELECT * FROM hat where id="+ id +""
    
    mycursor.execute(sql)
    results = mycursor.fetchall()

    
    data = []
    
    print(results)

    for result in results:
        dict = {}
        print("id :", result[0], "name :", result[1] )
        dict["id"] = result[0]
        dict["name"] = result[1]
        dict["Diabetes"] = result[2]
        dict["Rankin"] = result[3]
        dict["Age"] = result[4]
        dict["tot_time"] = result[5]
        dict["resultH"] = result[6]

        data.append(dict)

    print(data)
    return data