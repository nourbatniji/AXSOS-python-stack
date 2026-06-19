from django.db import models
import bcrypt, re
from datetime import date, datetime

# Create your models here.

class UserManager(models.Manager):
    def reg_validation(self, postData):
        errors = {}
        email_regex = re.compile(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$')
        pass_regex = re.compile(r'^(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[a-zA-Z]).{8,}$')
        if len(postData['first_name']) < 4 :
            errors['firstname_valid'] = 'First name should be at least 4 characters'
        if len(postData['last_name']) < 4 : 
            errors['lastname_valid'] = 'Last name should be at least 4 characters'

        if not email_regex.match(postData['email']): 
            errors['email_valid']  = 'Invalid email'
        
        if get_email(postData['email']): 
            errors['not_unique']  = 'Email already exists'

        if not pass_regex.match(postData['password']): 
            errors['pass_valid']  = 'Password should be at least 8 characters'

        if not pass_regex.match(postData['confirm_pw']): 
            errors['confirmpw_valid']  = 'Password confirmation should be at least 8 characters'

        if postData['password'] != postData['confirm_pw']:
            errors['matching']  = 'Passwords do not match'

        if not postData['birthday']:
            errors['no_date']  = 'Please choose a date'


        #user is 18 or more
        current_year = datetime.now().year
        year = datetime.strptime(postData['birthday'], "%Y-%m-%d").year
        if (current_year - year) < 18 : 
            errors['invalid_user']  = 'User should be 18 years or older'

        return errors
    
    def login_validation(self, postData):
        login_errors = {}
        email_regex = re.compile(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$')
        pass_regex = re.compile(r'^(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[a-zA-Z]).{6,}$')

        if not email_regex.match(postData['email']): 
            login_errors['login_email_valid']  = 'Invalid email'

        if not get_email(postData['email']): 
            login_errors['login_not_unique']  = 'Email does not exist'

        if not pass_regex.match(postData['password']): 
            login_errors['login_pass_valid']  = 'Password should be at least 8 characters'

        return login_errors



class GameManager(models.Manager):
    def game_validation(self, postData):
        errors ={}
        if len(postData['game_name']) < 2 :
            errors['gamename_valid'] = 'Game name should be at least 2 characters'

        if len(postData['desc']) == '':
            errors['gamename_valid'] = "Description can't be empty"
        
        current_time = datetime.now()
        release = datetime.strptime(postData['release_date'], "%Y-%m-%d")

        if release>current_time:
            errors['releasedate_valid'] = "Release date can't be in the future"
        print(errors)
        return errors


def user_directory_path(instance, filename):

    # file will be uploaded to MEDIA_ROOT / user_<id>/<filename>
    return 'user_{0}/{1}'.format(instance.user.id, filename)


class User(models.Model):
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    email = models.CharField(max_length=255)
    birthday = models.DateField()
    password = models.CharField(max_length=255)
    avatar = models.ImageField(upload_to='avatars/', default='avatars/default.png')  
    objects = UserManager()
    #user_games
    #favorites

class Game(models.Model):
    game_name =  models.CharField(max_length=100)
    genre =  models.CharField(max_length=45)
    release_date = models.DateField()
    desc = models.TextField()
    uploaded_by = models.ForeignKey(User, related_name='user_games', on_delete=models.CASCADE)
    objects = GameManager()
    #favorite
    
class FavoriteGame(models.Model):
    rate = models.IntegerField()
    user = models.ManyToManyField(User, related_name='favorites')
    game = models.ForeignKey(Game, related_name='favorites', on_delete=models.CASCADE)

def create_user(postData, filesData):
    hashed_pw = bcrypt.hashpw(postData['password'].encode(), bcrypt.gensalt()).decode()
    now = date.today()
    print(now)
    print(postData['birthday'])
    return User.objects.create(
        first_name=postData['first_name'],
        last_name=postData['last_name'],
        email=postData['email'],
        birthday=postData['birthday'],
        password=hashed_pw,
        avatar=filesData.get('avatar')
    )

def get_email(email):
    return User.objects.filter(email=email)

def get_user_by_id(id):
    return User.objects.get(id=id)

def create_game(postData):
    user = User.objects.get(id=postData['user_id'])
    return Game.objects.create(
        game_name=postData['game_name'],
        genre=postData['genre'],
        release_date=postData['release_date'],
        desc=postData['desc'],
        uploaded_by=user
    )

def get_all_games():
    return Game.objects.all()

def get_game_by_id(id):
    return Game.objects.get(id=id)

def update_game(postData, id):
    game_to_edit = Game.objects.get(id=id)
    game_to_edit.game_name = postData['game_name']
    game_to_edit.genre = postData['genre']
    game_to_edit.release_date = postData['release_date']
    game_to_edit.desc = postData['desc']
    game_to_edit.save()


def delete_game(postData):
    game_to_delete = Game.objects.get(id=postData['game_id'])
    game_to_delete.delete()


def order_games():
    return Game.objects.all().order_by('release_date')


def order_favs():
    return FavoriteGame.objects.all().order_by('release_date')

def add_game_to_favorite(postData):
    this_user = User.objects.get(id=postData['user_id'])
    this_game = Game.objects.get(id=postData['game_id'])
    favorite = FavoriteGame.objects.create(rate=postData['rate'], game=this_game)
    favorite.save()
    favorite.user.add(this_user)


def get_games_fans(id):
    this_game = Game.objects.get(id=id)
    #returned users
    return this_game.favorites.all()
    

def get_user_favorites(id):
    this_user = User.objects.get(id=id)
    #returns games
    return this_user.favorites.all()
    


