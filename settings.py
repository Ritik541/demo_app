"""
Django settings for demoproject project.

Generated by 'django-admin startproject' using Django 5.2.1.

For more information on this file, see
https://docs.djangoproject.com/en/5.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.2/ref/settings/
"""

from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-o&+242n%=^#oravw)ohpa8pp6*1u4h$=o+36(t^t@af!9j7klp'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contr'
    'ib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'demoapp',
    'rest_framework'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'demoproject.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'demoproject.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.2/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql',
#         'NAME': BASE_DIR / 'db.sqlite3',
#     }
# }
# import psycopg2

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql',
#         'NAME': 'demodb',       # 👈 Replace with your DB name
#         'USER': 'demouser',                 # 👈 Your PostgreSQL username
#         'PASSWORD': 'testing321',        # 👈 Your PostgreSQL password
#         'HOST': 'localhost',                # or '127.0.0.1'
#         'PORT': '5432',                     # default PostgreSQL port
#     }
# }

# settings.py

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'demodb',             # Your database name
        'USER': 'postgres',           # Your PostgreSQL username
        'PASSWORD': '1234',     # Your PostgreSQL password
        'HOST': 'localhost',          # Or your DB host
        'PORT': '5432',               # Default PostgreSQL port
    }
}



# import psycopg2

# # Replace with your database credentials
# DATABASE_NAME = "demodb"
# DATABASE_USER = "demouser"
# DATABASE_PASSWORD = "testing321"
# DATABASE_HOST = "localhost"  # or your host/IP address
# DATABASE_PORT = 5432

# try:
#     # Establish a connection to the database
#     connection = psycopg2.connect(
#         dbname=demodb,
#         user=demouser,
#         password=testing321,
#         host=localhost,
#         port=5432
#     )

#     # Create a cursor object to execute SQL queries
#     cursor = connection.cursor()

#     # Example: Execute a SELECT query
#     cursor.execute("SELECT * FROM your_table;")  # Replace 'your_table'

#     # Fetch all the results
#     records = cursor.fetchall()

#     # Print the results
#     print("Data from the database:")
#     for record in records:
#         print(record)

#     # Close the cursor and connection
#     cursor.close()
#     connection.close()

# except psycopg2.Error as e:
#     print("Error connecting to PostgreSQL:")
#     print(e)
 



# Password validation
# https://docs.djangoproject.com/en/5.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/5.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.2/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/5.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
