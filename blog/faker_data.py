import random

from faker import Faker
from .models import Post
fake=Faker()

def create_data():
    for i in range(100):
        post_content=fake.sentence()
        post_title=fake.name()
        post_author=random.randint(1,5)

        post=Post.objects.create(post_title=post_title,post_content=post_content,post_author_id=post_author)
        post.save()