from fastapi import FastAPI

app = FastAPI(title='API Katherine Corrales - Doceria')


@app.get('/')
def read_root():
    return {'message': 'Olá mundo'}
