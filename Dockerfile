
FROM python:3.9

WORKDIR /code

# copy requirements, make use of cache
COPY ./requirements.txt /code/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

# cat web app # change to cats or dogs
COPY ./app-dogs /code/app

# run app
CMD ["fastapi", "run", "app/main.py", "--port", "80"]