from django.db import models

class Zuke_User(models.Model):
    gender = (("Male", "Male"), ("Female", "Female"), ("Other", "Other"))
    user_id = models.AutoField(primary_key=True, editable=False)
    name = models.CharField(max_length=150, unique=True)
    dob = models.DateField()
    sex = models.CharField(max_length=15, choices=gender, default="Male")
    phone = models.CharField(max_length=12, unique=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=50)

    def __str__(self):
        return "{}, {}".format(self.user_id, self.name)

class Videos(models.Model):
    video_id = models.AutoField(primary_key=True)
    video_title = models.CharField(max_length=150)
    label = models.CharField(max_length=150)
    vtype = models.CharField(max_length=150,null=True, blank=True)
    contents = models.CharField(max_length=255,null=True, blank=True)
    genere = models.CharField(max_length=150,null=True, blank=True)
    no_words = models.CharField(max_length=1000,null=True, blank=True)
    no_sentences = models.CharField(max_length=150,null=True, blank=True)
    description  = models.CharField(max_length=150,null=True, blank=True)
    videos = models.FileField(upload_to='')

    def __str__(self):
        return "{}".format(self.video_title)


class Zuke_Subscribed(models.Model):
    user_id = models.ForeignKey(Zuke_User, on_delete=models.CASCADE)
    video_title = models.ManyToManyField(Videos)

class User_Filters(models.Model):
    user_id = models.ForeignKey(Zuke_User, on_delete=models.CASCADE)
    search = models.CharField(max_length=150,null=True, blank=True)
    genere = models.CharField(max_length=150,null=True, blank=True)
    words = models.CharField(max_length=150,null=True, blank=True)

class Issue(models.Model):
    name = models.CharField(max_length=150,null=True, blank=True)
    email = models.CharField(max_length=150,null=True, blank=True)
    issue = models.CharField(max_length=253,null=True, blank=True)


