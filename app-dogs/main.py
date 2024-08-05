from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles

app = FastAPI()

# app.mount("/imgs", StaticFiles(directory="imgs"), name='images')
@app.get("/", response_class=HTMLResponse)
def serve():
    return """
    <html>
        <head>
            <title>World Invasion Homepage</title>
        </head>
        <body>
            <h1><center>Welcome to the Dog World!</center></h1>
            <center><img src="imgs/dogs.png"></center>
        </body>
    </html>
    """