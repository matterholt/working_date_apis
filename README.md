# working_date_apis

get more familiar working with backends tech. 

## TASKS  

1. basic routing

2. path params

3. query params



1. send a date as a url param, and will return the dates that are associated with the path

2. multiple routes

3. create a REST API

4. return static files html/css/js

5. 

## FLASK

[Flask](https://flask.palletsprojects.com/en/2.3.x/)

<strong>app root: </strong>./servers/python_flask/src

<strong>environment</strong> 'source .venv_flask/bin/activate'

<strong>Run : </strong> @ root: 'flask --app flaskr run --debug'

## Dates for sheep life

.../api/sheep/gestation?event=lambing?date=2


## FastAPI

- build in tool, redoc,self documentation, pydatic
- order matters
- pre declared paths, use python Enum
    - if the path is something that the developer know and has coded it. oppose to a name or sime other information that the user could place in. 
- a param that has a path to some thing else in the api, OpenAPI does not support but FastAPI is able to handle the request
    - internal tool 'Starlette' -> declare param with "...:path" 
- has error checks and autocompletion, 
- able to parse data that sends and recieves
- built in data validation
- automated doc and annotations


### extra routes for understanding api

- http://127.0.0.1:8000/docs
- http://127.0.0.1:8000/redoc
- http://127.0.0.1:8000/openapi.json



### notes
https://www.digitalocean.com/community/tutorials/use-expressjs-to-get-url-and-post-parameters#step-2-using-req-query-with-url-parameters

