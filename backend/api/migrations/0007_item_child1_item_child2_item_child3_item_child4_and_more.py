# Generated by Django 5.0.3 on 2024-07-06 08:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_item_spouse_address'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='child1',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='item',
            name='child2',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='item',
            name='child3',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='item',
            name='child4',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='item',
            name='child5',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
