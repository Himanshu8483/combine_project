# Generated by Django 5.2.3 on 2025-06-15 05:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_alter_order_productprice_alter_order_totalamount'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='productImage',
            field=models.URLField(blank=True, max_length=300),
        ),
        migrations.AlterField(
            model_name='order',
            name='productName',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='order',
            name='productPrice',
            field=models.FloatField(blank=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='quantity',
            field=models.IntegerField(blank=True, default=1),
        ),
        migrations.AlterField(
            model_name='order',
            name='totalAmount',
            field=models.FloatField(blank=True),
        ),
    ]
