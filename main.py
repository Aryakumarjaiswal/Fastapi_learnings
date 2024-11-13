from fastapi import FastAPI
app=FastAPI()#initialise in variable 
#level 0
@app.get('/')
def wish():

    return "Congratulations Aryan for your First Fastapi app"


@app.get('/job/')
def job_intro():
    
    return "I'm AI Developer in MaitriAI"

#level 1
Bag=["Apple","Banana","Mango","Chickoo"]

@app.get('/bag')#'/bag' is path parameter
def show_item():
    return Bag


Bag=["Apple","Banana","Mango","Chickoo"]
@app.get('/bag/{item_no}')
def fruits(item_no):

    
    
    if len(Bag)<int(item_no):
        return "False"
    return Bag[int(item_no)]

#level2:query parameter
# When you declare other function parameters that are not part of the path parameters,
# they are automatically interpreted as "query" parameters.
#The query is the set of key-value pairs that go after the ? in a URL, separated by & characters.
@app.get('/bbag1')
def query_func(limit):#limit is query parameter
    return {'1':f"{limit} blog from DB"}
# http://127.0.0.1:8000/Get?limit=23
@app.get('/Get')
def key_vale_query1(limit,item):
    return f"Limit of {item} is {limit}"
#for http://127.0.0.1:8000/Get?limit=23&item=banana

@app.get('/Get2')
def key_vale_query1(limit=1,item="Apple"):#Setting default value
    return f"Limit of {item} is {limit}"

#Level 3
# Import FastAPI
from fastapi import FastAPI

# Create an instance of FastAPI
app = FastAPI()

# Define a POST route
@app.post("/create-item")
def create_item(name: str, price: float):
    
    return {"name": name, "price": price}

@app.post('/item/')
def Print():
    return("Creating...")

#Use below standard way to extrac informations
from fastapi import FastAPI
from pydantic import BaseModel
app=FastAPI()

class Credential(BaseModel):
    name:str
    age:int


@app.post('/Info')
def Informations(request:Credential):
    return request




#to run above you've to do that via /docs.


