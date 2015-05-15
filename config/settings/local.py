"""
Django local(dev) settings for NoLemon project.
Extends base.py
"""

from .base import *


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

INSTALLED_APPS += ('debug_toolbar', )
