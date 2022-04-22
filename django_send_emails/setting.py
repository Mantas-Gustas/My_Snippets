"""
Settings for Sending Emails in Django
The value changes according to the type of email services. These settings are to be added in the settings.py file of the project.

These are the settings for sending email in Django via Gmail.
"""



EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_USE_SSL = False
EMAIL_HOST_USER = env('EMAIL_HOST_USER')  # this is where you need to create your ENVIRON Variable
EMAIL_HOST_PASSWORD = env('EMAIL_HOST_PASSWORD')  # the EMAIL_USER and EMAIL_PASS are Enviro Variables holding sensitive info
# to create enviro variables see below instructions
# 1. Install Django Environ - In your terminal, inside the project directory, type: pip install django-environ
# 2. Import environ in settings.py - import environ
# 3. Initialise environ - Below your import in settings.py:
""" import environ
# Initialise environment variables #
env = environ.Env()
environ.Env.read_env() """
# 4. Create your .env file - In the same directory as settings.py, create a file called ‘.env’
# 5. Declare your environment variables in .env - Make sure you don’t use quotations around strings.
# 6. IMPORTANT: Add your .env file to .gitignore
# 7. Replace all references to your environment variables in settings.py

"""
EMAIL_BACKEND
This setting specifies the backend that we are going to use for sending an email in Django. There are multiple backends that Django provides.

EMAIL_HOST
This setting is to specify your email service provider. We are using the setting for Gmail.

EMAIL_HOST_USER
It is the account name from which we will send an email.

EMAIL_HOST_PASSWORD
The password of the email account that we are using.

EMAIL_PORT
This is the setting for Gmail, you can get yours on the web. It is the port used by the SMTP server.

EMAIL_USE_TLS
This setting specifies whether the Email uses a TLS connection or not. It is True for Gmail.

EMAIL_USE_SSL
False for Gmail.
"""