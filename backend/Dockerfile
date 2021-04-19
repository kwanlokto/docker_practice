FROM python:3.7

RUN pip install pipenv

WORKDIR /app/backend

# We create the requirements.txt first to leverage Docker cache
COPY Pipfile /Pipfile
RUN pipenv lock --keep-outdated --requirements > requirements.txt

RUN pip install -r requirements.txt

EXPOSE 5000

COPY . .

CMD ["python", "app.py", "runserver"]
