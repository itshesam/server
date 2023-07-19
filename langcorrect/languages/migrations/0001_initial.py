# Generated by Django 4.2.3 on 2023-07-19 13:25

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import model_utils.fields


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Language",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                (
                    "created",
                    model_utils.fields.AutoCreatedField(
                        default=django.utils.timezone.now, editable=False, verbose_name="created"
                    ),
                ),
                (
                    "modified",
                    model_utils.fields.AutoLastModifiedField(
                        default=django.utils.timezone.now, editable=False, verbose_name="modified"
                    ),
                ),
                ("is_removed", models.BooleanField(default=False)),
                ("en_name", models.CharField(max_length=120, unique=True)),
                ("family_code", models.CharField(default="N/A")),
                ("code", models.CharField(max_length=7, unique=True)),
            ],
            options={
                "ordering": ["code"],
            },
        ),
        migrations.CreateModel(
            name="LanguageLevel",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                (
                    "created",
                    model_utils.fields.AutoCreatedField(
                        default=django.utils.timezone.now, editable=False, verbose_name="created"
                    ),
                ),
                (
                    "modified",
                    model_utils.fields.AutoLastModifiedField(
                        default=django.utils.timezone.now, editable=False, verbose_name="modified"
                    ),
                ),
                ("is_removed", models.BooleanField(default=False)),
                (
                    "level",
                    models.CharField(
                        choices=[
                            ("A1", "Beginner"),
                            ("A2", "Elementary"),
                            ("B1", "Intermediate"),
                            ("B2", "Upper-Intermediate"),
                            ("C1", "Advanced"),
                            ("C2", "Proficient"),
                            ("N", "Native"),
                        ],
                        default="A1",
                        max_length=2,
                    ),
                ),
                ("language", models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to="languages.language")),
                ("user", models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                "unique_together": {("user", "language")},
            },
        ),
    ]
