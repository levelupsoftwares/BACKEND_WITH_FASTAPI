from fastapi import FastAPI
from fastapi.params import Body
from pydantic import BaseModel


app = FastAPI()

@app.get('/')
def main():
    print("Hello from backend-with-fastapi!")
    return 'hi fasto'


@app.get('/post')
def tempo():
    return 'temo post'

@app.post('/createpost')
def posting(payload:dict = Body(...)):
    return {'new_post':f"title{payload['title']}"}

@app.post('/createuser')
def createuser(payload:dict = Body(...)):
    return {'user created':f" user name:{payload['name'] }and with age {payload['age']} and city:{payload['city']}"}

#schema
class NewUser(BaseModel):
    User_Name:str
    age:int
    bio:dict


@app.post('/newuser')
def newusers(user:NewUser):
    user = user.model_dump()          
    print(user)            #convert pydantic model to dict
    return {'new user is:'+ user['User_Name']}

if __name__ == "__main__":
    main()
