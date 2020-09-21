from django.test import TestCase
from django.contrib.auth.models import User
from movies.models import Movie
from rating.models import Rating


class UserTestCase(TestCase):

     def test_setUp(self):
     	User.objects.create(id="1",username="jadid3",email="jadid3@gmail.com",password="qwerty123")
     	User.objects.create(id="2",username="aang",email="aang@gmail.com",password="windhelm")
     	User.objects.create(id="3",username="Hughie",email="hugh@gmail.com",password="saskara")
     	Movie.objects.create(id="21",owner_id="1",name="Alien",director="Ridley")
     	Movie.objects.create(id="22",owner_id="2",name="300",director="Jack")
     	Movie.objects.create(id="23",owner_id="3",name="Saving Private Ryan",director="steven")
     	Rating.objects.create(id="31",owner_id=User.objects.get(id="1"),movie_id=Movie.objects.get(id="21"),rate="8")
     	Rating.objects.create(id="32",owner_id=User.objects.get(id="2"),movie_id=Movie.objects.get(id="22"),rate="9")
     	Rating.objects.create(id="33",owner_id=User.objects.get(id="3"),movie_id=Movie.objects.get(id="23"),rate="10")



     	

