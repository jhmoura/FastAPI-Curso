from fastapi import FastAPI

app = FastAPI()

cursos = {
    1:{
        "titulo": "Programação para Leigos",
        "aulas": 112,
        "horas": 58
    },
    2:{
        "titulo":"Algoritmos",
        "aulas": 87,
        "horas": 67
    }
}

#Endpoints

@app.get('/cursos')
async def get_cursos():
    return cursos

@app.get('/cursos/{curso_id}')
async def get_curso_id(curso_id: int):
    curso = cursos[curso_id]
    #curso.update({"id": curso_id})

    return curso

if __name__=='__main__':
    import uvicorn

    uvicorn.run("main:app", host="0.0.0.0", port=6000, debug=True, reload=True)