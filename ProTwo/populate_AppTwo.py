import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ProTwo.settings')

import django
django.setup()

from AppTwo.models import User
from faker import Faker

fakegen = Faker()

def populate(N=5):
    for entry in range(N):
        fake_first = fakegen.first_name()
        fake_last = fakegen.last_name()
        fake_email = fakegen.free_email()

        user = User.objects.get_or_create(first_name=fake_first,last_name=fake_last,email=fake_email)[0]

if __name__ == '__main__':
    print('populating script!')
    populate(20)
    print("Populating complete!")