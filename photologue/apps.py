from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class PhotologueConfig(AppConfig):
    name = 'photologue'
    verbose_name = _('Работа с изображениями')
