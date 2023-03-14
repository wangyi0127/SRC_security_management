# Generated by Django 4.1.7 on 2023-03-13 15:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('srcmodel', '0003_alter_businesstype_type_name_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='businesstype',
            options={'verbose_name': '业务类型表', 'verbose_name_plural': '业务类型表'},
        ),
        migrations.AlterModelOptions(
            name='companyinformation',
            options={'verbose_name': '公司信息表', 'verbose_name_plural': '公司信息表'},
        ),
        migrations.AlterModelOptions(
            name='department',
            options={'verbose_name': '部门表', 'verbose_name_plural': '部门表'},
        ),
        migrations.AlterModelOptions(
            name='industrytype',
            options={'verbose_name': '行业类型表', 'verbose_name_plural': '行业类型表'},
        ),
        migrations.AlterModelOptions(
            name='leakinformation',
            options={'verbose_name': '漏洞信息表', 'verbose_name_plural': '漏洞信息表'},
        ),
        migrations.AlterModelOptions(
            name='leakrank',
            options={'verbose_name': '漏洞等级表', 'verbose_name_plural': '漏洞等级表'},
        ),
        migrations.AlterModelOptions(
            name='manageuserdetail',
            options={'verbose_name': '运营用户信息表', 'verbose_name_plural': '运营用户信息表'},
        ),
        migrations.AlterModelOptions(
            name='project',
            options={'verbose_name': '项目信息表', 'verbose_name_plural': '项目信息表'},
        ),
        migrations.AlterModelOptions(
            name='projectstatus',
            options={'verbose_name': '项目状态表', 'verbose_name_plural': '项目状态表'},
        ),
        migrations.AlterModelOptions(
            name='projecttype',
            options={'verbose_name': '项目类型表', 'verbose_name_plural': '项目类型表'},
        ),
        migrations.AlterModelOptions(
            name='rewardlevel',
            options={'verbose_name': '奖励等级表', 'verbose_name_plural': '奖励等级表'},
        ),
        migrations.AlterModelOptions(
            name='rewardtype',
            options={'verbose_name': '奖励类型表', 'verbose_name_plural': '奖励类型表'},
        ),
        migrations.AlterModelOptions(
            name='skillrequirements',
            options={'verbose_name': '技能要求表', 'verbose_name_plural': '技能要求表'},
        ),
        migrations.AlterModelOptions(
            name='user',
            options={'verbose_name': '用户表', 'verbose_name_plural': '用户表'},
        ),
        migrations.AlterModelOptions(
            name='userdetail',
            options={'verbose_name': '安全人员信息表', 'verbose_name_plural': '安全人员信息表'},
        ),
    ]