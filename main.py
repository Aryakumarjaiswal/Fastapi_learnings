from fastapi import FastAPI
app=FastAPI()#initialise in variable 

@app.get('/')
def wish():

    return "Congratulations Aryan for your First Fastapi app"


@app.get('/job/')
def job_intro():
    
    return "I'm AI Developer in MaitriAI"


Bag=["Apple","Banana","Mango","Chickoo"]

@app.get('/bag')
def show_item():
    return Bag


Bag=["Apple","Banana","Mango","Chickoo"]
@app.get('/bag/{item_no}')
def fruits(item_no):

    
    
    if len(Bag)<int(item_no):
        return "False"
    return Bag[int(item_no)]


