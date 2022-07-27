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

if __name__=='__main__':
    import uvicorn

    uvicorn.run("main:app", host="0.0.0.0", port=6000, debug=True)