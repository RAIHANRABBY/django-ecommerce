# Generated by Django 4.0.4 on 2022-06-15 14:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0005_orderitem_shippingaddress_delete_productcatagory_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(default='defaultitem.jpg', upload_to='%d'),
        ),
    ]
