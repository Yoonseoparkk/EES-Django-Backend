# Generated by Django 5.0.6 on 2024-06-30 07:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Review',
            fields=[
                ('reviewId', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=128)),
                ('writer', models.CharField(max_length=32)),
                ('content', models.TextField()),
                ('regDate', models.DateTimeField(auto_now_add=True)),
                ('updDate', models.DateTimeField(auto_now=True)),
                ('reviewImage', models.CharField(max_length=100, null=True)),
                ('category', models.CharField(max_length=32, null=True)),
                ('rating', models.DecimalField(decimal_places=1, default=0, max_digits=3)),
                ('reviewCount', models.IntegerField(null=True)),
            ],
            options={
                'db_table': 'review',
            },
        ),
    ]
