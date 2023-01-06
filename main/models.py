from django.db import models

class Project(models.Model):
    title = models.CharField(max_length=70)
    description = models.TextField()
    image = models.ImageField(upload_to='pics/')
    link = models.CharField(max_length=200)
    technology = models.CharField(max_length=200)

    def __str__(self):
        return self.title


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Post(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    category = models.ManyToManyField(Category, related_name='post')
    created_on = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title 

class Comment(models.Model):
    author = models.CharField(max_length=60)
    body = models.TextField()
    post = models.ForeignKey(Post, on_delete=models.CASCADE)

class Profile(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    resume = models.FileField(upload_to='pdf')
    bio = models.TextField()
    birth_date = models.CharField(max_length=20)
    email = models.EmailField()
    phone_number = models.CharField(max_length=20)

class Skills(models.Model):
    name = models.CharField(max_length=100)
    level = models.PositiveIntegerField()

class Language(models.Model):
    name = models.CharField(max_length=100)
    level = models.PositiveIntegerField()

class Expertise(models.Model):
    name = models.CharField(max_length=100)

class Education (models.Model):
    school = models.CharField(max_length=100)
    major = models.CharField(max_length=300)
    start_end_date = models.CharField(max_length=20)
    desc = models.TextField()