from django.conf import settings
from django.core.management import call_command
from django.core.management.base import BaseCommand
from project.users.models import  Member, User

user_admin = [
    {"name":"admin","password":"password"}
]
members = [
    {
    "first_name":"Test",
    "last_name":"test",
    "email":"test@gmail.com",
    "phone":"9884080111",
    "role":"Admin"
},{
    "first_name":"Test1",
    "last_name":"test1",
    "email":"test1@gmail.com",
    "phone":"9884080112",
    "role":"Regular"
}
]
def create_superuser(username, password):
    print('Creating user {}:{}'.format(username, password))
    user, _ = User.objects.get_or_create(username=username)
    user.is_staff = True
    user.is_superuser = True
    user.save()
    user.set_password(password)
    user.save()
    return user


class Command(BaseCommand):

    def handle(self, *args, **options):

        call_command('makemigrations')
        call_command('migrate')

        if settings.DEBUG:
            print('Debug mode on')

        #print('Creating users')
        for k in user_admin:
            create_superuser(k["name"],k["password"])
        
        print('Creating members')
        for member in members:
            Member.objects.get_or_create(
                first_name=member['first_name'],
                last_name=member['last_name'],
                email=member['email'],
                phone=member['phone'],
                role=member['role'],)
        


