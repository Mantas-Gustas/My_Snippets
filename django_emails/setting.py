"""
Settings for Sending Emails in Django
The value changes according to the type of email services. These settings are to be added in the settings.py file of the project.

These are the settings for sending email in Django via Gmail.
"""


#DataFlair
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_USE_TLS = True
EMAIL_PORT = 587
EMAIL_HOST_USER = 'your_account@gmail.com'
EMAIL_HOST_PASSWORD = 'your accounts password'


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