# Generated by Django 2.2.9 on 2020-05-06 21:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cursos', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='avaliacao',
            options={'ordering': ['id'], 'verbose_name': 'Avaliação', 'verbose_name_plural': 'Avaliações'},
        ),
        migrations.AlterModelOptions(
            name='curso',
            options={'ordering': ['id'], 'verbose_name': 'Curso', 'verbose_name_plural': 'Cursos'},
        ),
        migrations.AlterField(
            model_name='avaliacao',
            name='curso',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='avaliacoes', to='cursos.Curso'),
        ),
    ]