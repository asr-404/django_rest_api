from django.db import models

# Create your models here.
class Invoice(models.Model):
    date = models.DateField()
    invoice_no = models.CharField(max_length=50,primary_key=True)
    customer_name = models.CharField(max_length=100)

    def __str__(self):
        return self.invoice_no
    



class InvoiceDetails(models.Model):
    invoice_no = models.ForeignKey(Invoice, on_delete=models.CASCADE)
    descripton=models.CharField(max_length=100)
    quantity=models.IntegerField()
    unit_price=models.IntegerField()
    price= models.IntegerField()
    

    def __str__(self):
        return f"{self.invoice_no} - {self.pk}"