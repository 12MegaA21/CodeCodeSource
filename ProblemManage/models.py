from django.db import models

# Create your models here.
# class Admin(models.Model):
#     username = models.CharField(verbose_name="Name", max_length=32)
#     pwd = models.CharField(verbose_name="Password", max_length=32)

class Tag(models.Model):
    Tag_name = models.CharField(verbose_name="Tag Name", max_length=64)

class Problem(models.Model):
    pid = models.CharField(verbose_name="#", max_length=32)
    title = models.CharField(verbose_name="Title", max_length=64)
    # tags = models.CharField(verbose_name="Tags", max_length=128)
    tags = models.ManyToManyField(verbose_name="Tag List", to=Tag)
    author = models.CharField(verbose_name="Author", max_length=32)
    rate = models.IntegerField(verbose_name="Rate")
    url = models.CharField(verbose_name="Url", max_length=128)
    ac_num = models.IntegerField(verbose_name="AC Number")
    isFree = models.BooleanField(verbose_name="Free", default=True)

class ProblemStatement(models.Model):
    # pid = models.ForeignKey(verbose_name="#", to="Problem", on_delete=models.CASCADE)
    pid = models.OneToOneField(verbose_name="#", to=Problem, on_delete=models.CASCADE)
    title = models.CharField(verbose_name="Title", max_length=64)
    time_limit = models.CharField(verbose_name="Time Limit", max_length=32)
    memory_limit = models.CharField(verbose_name="Memory Limit", max_length=32)
    input_file = models.CharField(verbose_name="Input File", max_length=64)
    output_file = models.CharField(verbose_name="Output File", max_length=64)
    content = models.TextField(verbose_name="Main Content")
    input_spec = models.TextField(verbose_name="Input Specification")
    output_spec = models.TextField(verbose_name="Output Specification")
    samples = models.TextField(verbose_name="Samples")
    note = models.TextField(verbose_name="Notes")

class Admin(models.Model):
    account = models.CharField(verbose_name="Account", max_length=64)
    password = models.CharField(verbose_name="Password", max_length=64)
    nickname = models.CharField(verbose_name="NickName", max_length=64)