from django.db import models
from django.contrib.auth.models import User


class Menu(models.Model):
    name = models.CharField(max_length=50)
    code = models.CharField(max_length=10)

    class Meta:
        db_table = 'tbl_menu'

    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.name


class Role(models.Model):
    name = models.CharField(max_length=50)

    class Meta:
        db_table = 'tbl_role'

    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.name


class Privilege(models.Model):
    menu = models.ForeignKey(Menu, on_delete=models.PROTECT)
    role = models.ForeignKey(Role, on_delete=models.CASCADE)
    access = models.BooleanField(default=False)

    class Meta:
        db_table = 'tbl_privilege'

    def __str__(self):
        return self.menu.name

    def __unicode__(self):
        return self.menu.name


class UserProfile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    role = models.ForeignKey(Role, on_delete=models.PROTECT)

    class Meta:
        db_table = 'tbl_user_profile'

    def __str__(self):
        return self.user.username

    def __unicode__(self):
        return self.user.username
