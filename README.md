
# Movies DB

### To use the payload use the generated token from registration add these in headers in Postman
key: Authorization  value: Token {generated token}
key: Content-Type value: application/json

The package provide a  REST interface for local sqlite instance and movies databse

In order to run this project on local environment you need to django installed and also

1. pip install -r requirements.txt

2. Set up db:

>python manage.py makemigrations 

>python manage.py migrate

3. Run your application locally:

>python manage.py runserver

4. Check your application on http://127.0.0.1:8000

5. Run database input tests

>python manage.py test

5. Api Endpoints

http://127.0.0.1:8000/api/register/
http://127.0.0.1:8000/api/login/  
http://127.0.0.1:8000/api/user/ 
http://127.0.0.1:8000/api/user/movies
http://127.0.0.1:8000/api/user/rating


6. eg payload for each API 



### use to register user
i> http://127.0.0.1:8000/api/register/

    {
        "username": "jahid",
        "email":"jahid@gmail.com",
        "password":"qwerty12345"
    }



### use the generated token  to login

ii> http://127.0.0.1:8000/api/login/

    {
        "username": "jahid",
        "password":"qwerty12345"
    }



### Use this to check current user and id

iii> http://127.0.0.1:8000/api/user/



###  use to input movies

iv> http://127.0.0.1:8000/api/movies/

    {
        "name": "Alien",
        "director":"Ridley scott"
    }



### to rate movies betwwen 1 to 10, use genrrated user id and movie id

v> http://127.0.0.1:8000/api/rating/

    {
        "owner_id": "1",
        "movie_id":"1",
        "rate":"9"
    }



### to change current user password

vi> http://127.0.0.1:8000/api/change-password/

    {
        "old_password": "qwerty12345",
        "new_password":"qwerty123"
    }





















