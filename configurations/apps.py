from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _

class ConfigurationsConfig(AppConfig):
    name = 'configurations'
    verbose_name = _('Configurations')
