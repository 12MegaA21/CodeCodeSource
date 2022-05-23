from django.db import models

# Create your models here.
# class Admin(models.Model):
#     username = models.CharField(verbose_name="Name", max_length=32)
#     pwd = models.CharField(verbose_name="Password", max_length=32)

class Problem(models.Model):
    pid = models.CharField(verbose_name="#", max_length=32)
    title = models.CharField(verbose_name="Title", max_length=64)
    tags = models.CharField(verbose_name="Tags", max_length=128)
    author = models.CharField(verbose_name="Author", max_length=32)
    rate = models.IntegerField(verbose_name="Rate")
    url = models.CharField(verbose_name="Url", max_length=128)
    ac_num = models.IntegerField(verbose_name="AC Number")

class ProblemStatement(models.Model):
    pid = models.ForeignKey(verbose_name="#", to="Problem", on_delete=models.CASCADE)
    title = models.CharField(verbose_name="Title", max_length=64)
    time_limit = models.CharField(verbose_name="Time Limit", max_length=32)
    memory_limit = models.CharField(verbose_name="Memory Limit", max_length=32)
    input_file = models.CharField(verbose_name="Input File", max_length=64)
    output_file = models.CharField(verbose_name="Output File", max_length=64)
    content = models.CharField(verbose_name="Main Content", max_length=4096)
    input_spec = models.CharField(verbose_name="Input Specification", max_length=4096)
    output_spec = models.CharField(verbose_name="Output Specification", max_length=4096)
    samples = models.CharField(verbose_name="Samples", max_length=4096)
    note = models.CharField(verbose_name="Notes", max_length=4096)
