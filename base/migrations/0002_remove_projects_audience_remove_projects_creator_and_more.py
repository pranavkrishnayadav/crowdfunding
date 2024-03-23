# Generated by Django 5.0.2 on 2024-03-23 08:29

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("base", "0001_initial"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RemoveField(
            model_name="projects",
            name="audience",
        ),
        migrations.RemoveField(
            model_name="projects",
            name="creator",
        ),
        migrations.AlterField(
            model_name="creator",
            name="user",
            field=models.OneToOneField(
                default=None,
                on_delete=django.db.models.deletion.CASCADE,
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AddField(
            model_name="creator",
            name="bio",
            field=models.TextField(blank=True, default=None, null=True),
        ),
        migrations.CreateModel(
            name="Backer",
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
                ("bio", models.TextField(blank=True, default=None, null=True)),
                (
                    "amount_pledged",
                    models.DecimalField(decimal_places=2, max_digits=10),
                ),
                (
                    "user",
                    models.OneToOneField(
                        default=None,
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Project",
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
                ("title", models.CharField(max_length=200)),
                ("description", models.TextField()),
                (
                    "project_type",
                    models.CharField(
                        choices=[
                            ("technology", "Technology"),
                            ("art", "Art"),
                            ("comics", "Comics"),
                            ("games", "Games"),
                            ("publishing", "Publishing"),
                        ],
                        default="technology",
                        max_length=200,
                    ),
                ),
                ("funding_goal", models.DecimalField(decimal_places=2, max_digits=10)),
                (
                    "current_funding",
                    models.DecimalField(decimal_places=2, default=0, max_digits=10),
                ),
                ("start_date", models.DateField(null=True)),
                ("end_date", models.DateField(null=True)),
                (
                    "backers",
                    models.ManyToManyField(
                        related_name="backed_projects", to="base.backer"
                    ),
                ),
                (
                    "creator",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="base.creator"
                    ),
                ),
            ],
        ),
        migrations.DeleteModel(
            name="Audience",
        ),
        migrations.DeleteModel(
            name="Projects",
        ),
        migrations.DeleteModel(
            name="User",
        ),
    ]
