# Generated by Django 4.1.7 on 2023-04-03 11:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("agents", "0006_remove_branch_additional_cash_and_more"),
        ("vault_manager", "0022_rename_check_number_withdraw_cheque_number"),
    ]

    operations = [
        migrations.AddField(
            model_name="zonevault",
            name="location",
            field=models.ForeignKey(
                default="",
                on_delete=django.db.models.deletion.CASCADE,
                related_name="location",
                to="agents.branch",
            ),
        ),
    ]