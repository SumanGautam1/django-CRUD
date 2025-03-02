"""
This is the configuration file for application.
"""
from django.apps import AppConfig


class MyappConfig(AppConfig):
    """
    myApp configuration.
    """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'myApp'
