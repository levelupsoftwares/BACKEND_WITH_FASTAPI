# Learning Backend with FastAPI

![FastAPI](https://img.shields.io/badge/FastAPI-009688?style=flat-square&logo=fastapi&logoColor=white) is a modern ,high performance web framework for building APIs with Python

### Built On

![Static Badge](https://img.shields.io/badge/Pydantic-v2-red?style=for-the-badge&logo=pydantic&logoColor=white) + ![Static Badge](https://img.shields.io/badge/Starlette-v0.45-purple?style=for-the-badge&logo=starlette&logoColor=white)

---
### Reason 
![Static Badge](https://img.shields.io/badge/Starlette-v0.45-purple?style=for-the-badge&logo=starlette&logoColor=white) manages how your API recieves requests and send back responses.

![Static Badge](https://img.shields.io/badge/Pydantic-v2-red?style=for-the-badge&logo=pydantic&logoColor=white) is used to check and validate the data come into API in correct + right format

---
### Why FastAPI is fast to code 

1. **Automatic input validation** 
2. **Auto generated , Interective Documentation**
3. **Seamless Integration with Modern Ecosystem** (ML/DL libraries ,OAuth ,JWT ,SQL Alchemy ,Docker ,Kubernetes etc)

---

## Setup & Installation

### Project Setup
```bash
uv init project_name
cd project_name
uv venv
```

---
### Vritual Enviornment Activation
#### Linux & Mac
```bash
source .venv/bin/activate 
```
#### Windows
```bash
.venv\Scripts\activate
```

---
### Installing FastAPI library 

```bash
uv add fastapi[all]
```


---

## FastAPI Basics
### Creating a FastAPI Application
```
from fastapi import FastAPI

app = FastAPI()
```
* `FastAPI()` creates the application instance.
* Think of app as the *entry point* of the backend.
* Every incoming HTTP request first reaches this `app` instance.

---
### Creating API Endpoints


```
@app.get('/')
def home():
    return {"message":"hello backend with fastapi"}

```
* `@app.get("/")` register the a **Get endpoint**.
* It tells FastAPI:
        "If a `GET` request comes to `/`, execute the `home()` function."
* `@app.get("/)` is a **decorator factory** that returns a decorater to register the function
 with the given route.