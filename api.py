from fastapi import FastAPI

app = FastAPI()

authif = [
{
    'list_id':'',
    'keymaster':'',
    'steam_api_server':'',
    'max_players_server':'',
    'server_owner':'',
    'server_id':'',
    'server_developer':''
},
]

@app.get("/")
def auth():
    return authif