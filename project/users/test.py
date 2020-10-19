from django.test import TestCase
from django.test import Client
from . import models

c = Client()

def test_get_api(url):
    response = c.get(all_member)
    if response.status_code == 200:
        print("************ URL ' {} ' working *************".format(url))
    else:
        raise Exception("{} not working".format(url))

print("\nTesting member api's \n")
all_member = '/member/'
test_get_api(all_member)


class MemberTest(TestCase):

    def setUp(self):
        members = [
            {"first_name":"member",
            "last_name":"member last",
            "email":"test@email.com",
            "role":"Regular",
            "phone":"9887098870"
            },
            {"first_name":"member_1",
            "last_name":"member last_1",
            "email":"test1@email.com",
            "role":"Admin",
            "phone":"9887098871"
            }
        ]
        for member in members:
            models.Member.objects.create(
                first_name=member['first_name'],
                last_name=member['last_name'],
                email=member['email'],
                role=member['role'],
                phone=member['phone']
                )
        
    def test_count(self):
        self.assertEqual(models.Member.objects.count(), 2)

    def test1(self):
        print("Filter query 1")
        m = models.Member.objects.filter(email="test1@email.com").first()
        self.assertEqual(m.first_name, 'member_1')
        self.assertTrue(isinstance(m, models.Member))

    def test2(self):
        print("Filter query 2")
        m = models.Member.objects.filter(phone="9887098870").first()
        self.assertEqual(m.email, 'test@email.com')
        self.assertTrue(isinstance(m, models.Member))
    

    def test_edit(self):
        m = models.Member.objects.filter(phone="9887098870").first()
        m.role = "Admin"
        m.save()
        m = models.Member.objects.filter(phone="9887098870").first()
        self.assertEqual(m.role, 'Admin')

    def test_del(self):
        models.Member.objects.filter(phone="9887098870").delete()
        self.assertEqual(models.Member.objects.count(), 1)
