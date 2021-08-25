from django.db import models
from django.db.models.fields.related import ForeignKey
from django.db.models.deletion import PROTECT
from django.contrib.auth.models import AbstractUser
from creditcards.models import CardNumberField, CardExpiryField, SecurityCodeField
from django.utils.translation import gettext_lazy as _


class User(AbstractUser):
    first_name = models.CharField(max_length=30, default='')
    last_name = models.CharField(max_length=30, default='')
    username = models.CharField(max_length=30, unique=True)
    email = models.EmailField()    

    def __str__(self):
        return self.username


# class User(models.Model):
#   username = models.CharField(max_length=50, unique=True)
#   password = models.CharField(max_length=50, unique=True)
#   first_name = models.CharField(max_length=50)
#   last_name = models.CharField(max_length=50)
#   email = models.EmailField()
#   user_address = models.ForeignKey('Address', on_delete=PROTECT, related_name="addy")
#   created = models.DateTimeField(auto_now_add=True)
#   updated = models.DateTimeField(auto_now=True)

#   def __str__(self):
#     return "User"


class Address(models.Model):
  user_address = models.ForeignKey('User', on_delete=PROTECT, related_name='uname')
  address_id = models.IntegerField(primary_key=True)
  address_line1 = models.TextField()
  address_line2 = models.TextField()
  city = models.TextField()
  state = models.CharField(max_length=2)
  postal_code = models.PositiveIntegerField()
  country = models.TextField(blank=True)
  phone = models.CharField(max_length=15)

  def _str_(self):
    return "Address"


class Payment(models.Model):
    cc_number = CardNumberField(_('card number'))
    cc_expiry = CardExpiryField(_('expiration date'))
    cc_code = SecurityCodeField(_('security code'))
    user_name = models.ForeignKey('User', on_delete=PROTECT, related_name='ccname')

    def __str__(self):
      return 'CreditCard'