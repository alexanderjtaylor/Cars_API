# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-b360davu2j=b4@l8wjs-s$3@6xep&5_9o1xm5v+n=0#_8bhz38'

# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'cars_database',
        'HOST': 'localhost',
        'USER': 'root',
        'PASSWORD': 'password'
    }
}