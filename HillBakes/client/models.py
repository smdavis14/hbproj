from django.db import models
from django.db.models.fields.related import ForeignKey
from django.db.models.deletion import PROTECT
from django.contrib.auth.models import User
from creditcards.models import CardNumberField, CardExpiryField, SecurityCodeField
from django.utils.translation import gettext_lazy as _



class Address(models.Model):
  user_address = models.ForeignKey(User, on_delete=models.PROTECT, related_name='uname')
  address_line1 = models.CharField(max_length=100)
  address_line2 = models.CharField(max_length=100)
  city = models.CharField(max_length=50)
  state = models.CharField(max_length=2)
  postal_code = models.PositiveIntegerField()
  country = models.CharField(max_length=50, blank=True)
  phone = models.CharField(max_length=15)

  def _str_(self):
    return "Address"


class Payment(models.Model):
    cc_number = CardNumberField(_('card number'))
    cc_expiry = CardExpiryField(_('expiration date'))
    cc_code = SecurityCodeField(_('security code'))
    user_name = models.ForeignKey(User, on_delete=models.PROTECT, related_name='ccname')

    def __str__(self):
      return 'CreditCard'