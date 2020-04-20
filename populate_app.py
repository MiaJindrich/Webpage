import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Webpage.settings')

import django
django.setup()

# fake population script
import random
from app.models import UserProfileInfo, Topic, Article, AccessRecord
from faker import Faker

# create an instance of Faker
fake = Faker()
# make list of topics
topics = ['Health', 'Social', 'Business', 'News', 'Entertainment', 'Education']

# create user profiles first
def add_user():
    users = UserProfileInfo.objects.all()
    return users

def add_toppic():
    t = Topic.objects.get_or_create(top_name=random.choice(topics))[0]
    t.save()                                      
    return t

def populate(n=1):
    for entry in range(n):
        # get the topic for entry
        auth = random.choice(add_user())
        top = add_toppic()
        
        # create fake data for that entry
        fake_name = fake.sentence(nb_words=6, variable_nb_words=True, ext_word_list=None)
        fake_url = fake.url()
        fake_date = fake.date()
        
        # create fake article entry for that topic
        article = Article.objects.get_or_create(author=auth, topic=top, name=fake_name, url=fake_url)[0]

        # create fake accessrecord entry for that webpage
        accessrecord = AccessRecord.objects.get_or_create(name=article, date=fake_date)[0]

if __name__ == '__main__':
    print('Populating script!')
    populate(5)
    print('Population complete!')