# Generated by Django 4.0.5 on 2022-08-19 14:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AutoBatirApp', '0007_alter_permit_constructionplan'),
    ]

    operations = [
        migrations.AlterField(
            model_name='permit',
            name='ConstructionPlan',
            field=models.FileField(null=True, upload_to='docs_const_plan/pdfs/'),
        ),
        migrations.AlterField(
            model_name='permit',
            name='LandOwnerShipDoc',
            field=models.FileField(null=True, upload_to='docs_landownership/pdfs/'),
        ),
    ]
