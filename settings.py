DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'default_db',
        'USER': 'db_user',
        'PASSWORD': 'db_password',
        'HOST': 'localhost',
        'PORT': '5432',
    },
    'tenant1': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'tenant1_db',
        'USER': 'db_user',
        'PASSWORD': 'db_password',
        'HOST': 'localhost',
        'PORT': '5432',
    },
    'tenant2': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'tenant2_db',
        'USER': 'db_user',
        'PASSWORD': 'db_password',
        'HOST': 'localhost',
        'PORT': '5432',
    },  
}

