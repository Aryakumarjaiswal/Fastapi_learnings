from fastapi import FastAPI
app=FastAPI()#initialise in variable 

@app.get('/')
def intro():

    return "Congratulations Aryan for your First Fastapi app"
#In ternimal write
#uvicorn file_name_without.py:initialised_variable --reload(--reload auto restarts server if any change occurs)
#i.e uvicorn main:app --reload
