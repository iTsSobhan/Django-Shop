# Generated by Django 4.0.2 on 2022-03-03 07:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0002_alter_articlecategory_url_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='articlecategory',
            name='parent',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='articles.articlecategory', verbose_name='Parent Category'),
        ),
    ]
