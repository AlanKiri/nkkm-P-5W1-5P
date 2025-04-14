from fastapi import FastAPI

app = FastAPI()

@app.get('/test', tags=['Testavimas'], summary='Grazina NKKM', description="Labai ilgas tekstas kad jus zinotumete kazka")
def get_test():
    return 'NKKM'

tekstas = "Labas"

@app.post('/tekstas/{mano_tekstas}', tags=['tekstas'])
def append_tekst(mano_tekstas):
    global tekstas
    tekstas += mano_tekstas
    return {"ok":True, 'message':tekstas}

@app.get('/tekstas', tags=['tekstas'])
def gauti_tekst():
    return {"ok":True, 'message':tekstas}

@app.delete('/tekstas', tags=['tekstas'])
def delete_tekst():
    global tekstas
    tekstas = ""
    return {"ok":True, 'message':tekstas}

@app.put('/tekstas/{mano_tekstas}', tags=['tekstas'])
def update_tekst(mano_tekstas):
    global tekstas
    tekstas = mano_tekstas
    return {"ok":True, 'message':tekstas}


