from django.test import TestCase
#from django.conf import settings
#import mysite
from .mysite.settings import DATABASES

# Create your tests here.
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
#     }
# }

#getattr(settings, 'STATIC_URL', 'False')
#getattr(mysite.settings, 'STATIC_URL', 'False')
print(DATABASES['default']['NAME'])
#print(settings.CACHES)
