from django.db import models
from django.contrib.auth.models import User


# Current Finance detail table
class Finance(models.Model):
    invoice = models.IntegerField()
    fee_paid = models.IntegerField()
    date_invoiced = models.DateField()
    date_paid = models.DateField()
    transaction_id = models.CharField(max_length=150)
    balance = models.IntegerField()
    student = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return '{}({})'.format(
            self.student,
            self.transaction_id
        )


# Finance History deals with all past transactions of the student and list them....Every entry is a particular trx
class FinanceHistory(models.Model):
    date_posted = models.DateField()
    type = models.CharField(max_length=20)
    trx_id = models.CharField(max_length=50)
    description = models.CharField(max_length=50)
    amount = models.IntegerField()
    student = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return '{}({})'.format(
            self.type,
            self.student
        )



  







