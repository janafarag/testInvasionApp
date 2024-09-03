from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles

app = FastAPI()

app.mount("/code/app/imgs", StaticFiles(directory="/code/app/imgs"), name='images')

# default route
@app.get("/", response_class=HTMLResponse)
def serve():
    return """
    <html>
        <head>
            <title>World Invasion Homepage</title>
        </head>
        <body>
            <h1><center>Welcome to the Dog World!</center></h1>
            <center><img src="/code/app/imgs/dogs.png"></center>
        </body>
    </html>
    """

# /dog-service for ALB
@app.get("/dog-service", response_class=HTMLResponse)
def serve():
    return """
    <html>
        <head>
            <title>World Invasion Homepage</title>
        </head>
        <body>
            <h1><center>Welcome to the Dog World!</center></h1>
            <center><img src="/code/app/imgs/dogs.png"></center>
        </body>
    </html>
    """