FROM python:3.6
COPY ./MyApp /app

WORKDIR /app

RUN pip install pipenv
RUN pipenv install --python 3.6
RUN pipenv install -d --ignore-pipfile
RUN pipenv run pip freeze > requirements.txt
RUN pip install -r requirements.txt
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]