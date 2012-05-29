# Django settings for docs project.

# =========================
# = ENVIRONMENT VARIABLES =
# =========================
# Former local settings found below - now using environment variables
# Environment Variables are
#
# AXILENT_DOCS_DEBUG (False)
# AXILENT_DOCS_ADMIN_NAME ('Ops')
# AXILENT_DOCS_ADMIN_EMAIL ('ops@axilent.com')
# AXILENT_DOCS_DB_ENGINE ('django.db.backends.sqlite3')
# AXILENT_DOCS_DB_NAME ('axilentdocs')

# AXILENT_DOCS_PROJECT_ROOT ($PWD)
# AXILENT_DOCS_STATIC_ROOT ('<project-root>/collected-static/')
# AXILENT_DOCS_STATICFILES_DIRS ('<project-root>/common-static/')
# AXILENT_DOCS_STATIC_URL ('/static/')
# AXILENT_DOCS_SECRET_DJANGO_KEY

# AXILENT_DOCS_API_KEY
# AXILENT_DOCS_ENDPOINT ('https://www.axilent.net')



# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# On Unix systems, a value of None will cause Django to use the same
# timezone as the operating system.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = 'America/New_York'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en-us'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale.
USE_L10N = True

# If you set this to False, Django will not use timezone-aware datetimes.
USE_TZ = True

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
#    'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
#     'django.template.loaders.eggs.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    # Uncomment the next line for simple clickjacking protection:
    # 'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'docs.urls'

# Python dotted path to the WSGI application used by Django's runserver.
WSGI_APPLICATION = 'docs.wsgi.application'

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'axilent',
    'docs',
    # Uncomment the next line to enable the admin:
    # 'django.contrib.admin',
    # Uncomment the next line to enable admin documentation:
    # 'django.contrib.admindocs',
)

import os

DEBUG = True if os.environ.get('AXILENT_DOCS_DEBUG',None) else False
TEMPLATE_DEBUG = DEBUG

admin_name = os.environ.get('AXILENT_DOCS_ADMIN_NAME','Ops')
admin_email = os.environ.get('AXILENT_DOCS_ADMIN_EMAIL','ops@axilent.com')
ADMINS = (
    (admin_name,admin_email),
)

MANAGERS = ADMINS

db_engine = os.environ.get('AXILENT_DOCS_DB_ENGINE','django.db.backends.sqlite3')
db_name = os.environ.get('AXILENT_DOCS_DB_NAME','axilentdocs')
DATABASES = {
    'default': {
        'ENGINE': db_engine, # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': db_name,                      # Or path to database file if using sqlite3.
        'USER': '',                      # Not used with sqlite3.
        'PASSWORD': '',                  # Not used with sqlite3.
        'HOST': '',                      # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '',                      # Set to empty string for default. Not used with sqlite3.
    }
}

#project_root = os.environ.get('AXILENT_DOCS_PROJECT_ROOT',os.environ['PWD']+'/../') # locally manage.py is invoked one level down from project root
project_root = os.environ.get('AXILENT_DOCS_PROJECT_ROOT',os.environ['PWD']) # Except for Heroku, we need everything in project root (e.g. <root>/docs, not <root>/docs/docs

# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/home/media/media.lawrence.com/media/"
MEDIA_ROOT = ''

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# Examples: "http://media.lawrence.com/media/", "http://example.com/media/"
MEDIA_URL = ''

# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps' "static/" subdirectories and in STATICFILES_DIRS.
# Example: "/home/media/media.lawrence.com/static/"
static_root = os.environ.get('AXILENT_DOCS_STATIC_ROOT',project_root+'/collected-static/')
STATIC_ROOT = static_root

# URL prefix for static files.
# Example: "http://media.lawrence.com/static/"
static_url = os.environ.get('AXILENT_DOCS_STATIC_URL','/static/')
STATIC_URL = static_url

# Additional locations of static files
staticfiles_dirs = os.environ.get('AXILENT_DOCS_STATICFILES_DIRS',project_root+'/common-static/')
STATICFILES_DIRS = (
    # Put strings here, like "/home/html/static" or "C:/www/django/static".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    staticfiles_dirs,
)

print 'staticfiles dirs are',staticfiles_dirs

# Make this unique, and don't share it with anybody.
# SECRET_KEY = os.environ['AXILENT_DOCS_SECRET_DJANGO_KEY']
SECRET_KEY = '2541b&amp;b6(hg(b8zc7%4=6ylx%&amp;w^#b1uf%f5vd7ovv6^h8!0f^' # TODO!!!!

TEMPLATE_DIRS = (
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
)

# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error when DEBUG=False.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters':{
        'simple':{
            'format':'%(levelname)s %(message)s',
        },
    },
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'formatter':'simple',
            'class': 'logging.StreamHandler'
        },
    },
    'loggers': {
        'django-axilent':{
            'handlers':['console'],
            'level':'DEBUG',
        }
    }
}

AXILENT_API_KEY = os.environ['AXILENT_DOCS_API_KEY']
AXILENT_ENDPOINT = os.environ.get('AXILENT_DOCS_ENDPOINT','https://www.axilent.net')
#AXILENT_API_KEY = '2b9588c57c18414d9b2f529c74d32dc5' # TODO
