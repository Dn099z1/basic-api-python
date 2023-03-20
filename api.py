from fastapi import FastAPI

app = FastAPI()

authif = [
{
    'example':'',
    'example':'',
    'example':'',
    'example':'',
    'example':'',
    'example':'',
    'example':''
},
]

@app.get("/")
def auth():
    return authif
