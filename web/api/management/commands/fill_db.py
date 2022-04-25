from random import choice, getrandbits

from django.contrib.auth.hashers import make_password
from django.core.management.base import BaseCommand
from api.models import Article, User

ADJECTIVES = ('important', 'useless', 'stinky', 'saggy', 'fast', 'unique',
              'disgusting', 'ridiculous', 'inappropriate')
NAMES = ('alex', 'july', 'sam', 'bob', 'emma', 'rose', 'oliver', 'jack')
ACTIONS = ('jumped', 'run', 'ate', 'stroke', 'did', 'screwed')
OBJECTS = ('a laptop', 'a book', 'a fish', 'a mouse', 'a table', 'a phone')
WHEN = ('yesterday', 'just now', '5 minutes ago', 'tomorrow', 'next week')


class Command(BaseCommand):
    help = 'Fill database with some initial set of users and articles'

    @staticmethod
    def create_test_user(name):
        return User(email=f'{name}@gmail.com',
                    role='A',
                    password=make_password('testertester1'),
                    first_name=name,
                    last_name=choice(ADJECTIVES))

    @staticmethod
    def create_test_articles(author):

        random_title = f"{choice(NAMES)} " \
               f"{choice(ACTIONS)} " \
               f"{choice(OBJECTS)} " \
               f"{choice(WHEN)}"

        return Article(author=author,
                       title=random_title,
                       content=f'Very {choice(ADJECTIVES)} article!',
                       public=bool(getrandbits(1)))

    def handle(self, *args, **options):
        test_users = [self.create_test_user(name) for name in NAMES]
        User.objects.bulk_create(test_users)

        test_articles = [self.create_test_articles(author) for author in test_users]
        Article.objects.bulk_create(test_articles)
