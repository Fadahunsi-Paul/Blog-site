# Generated by Django 5.0.3 on 2024-03-09 19:19

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0003_alter_user_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='id',
            field=models.UUIDField(default=uuid.UUID('b7283f21-0c54-4886-b850-2b334ff92812'), editable=False, primary_key=True, serialize=False),
        ),
    ]
