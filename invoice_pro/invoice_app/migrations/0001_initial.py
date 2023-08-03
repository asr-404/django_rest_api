# Generated by Django 4.2.4 on 2023-08-02 13:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Invoice",
            fields=[
                ("date", models.DateField()),
                (
                    "invoice_no",
                    models.CharField(max_length=50, primary_key=True, serialize=False),
                ),
                ("customer_name", models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name="InvoiceDetails",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("descripton", models.CharField(max_length=100)),
                ("quantity", models.IntegerField()),
                ("unit_price", models.IntegerField()),
                ("price", models.IntegerField()),
                (
                    "invoice_no",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="invoice_app.invoice",
                    ),
                ),
            ],
        ),
    ]
