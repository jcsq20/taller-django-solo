import os

from django.db import models
from django.utils.translation import gettext as _
from geoposition.fields import GeopositionField
from solo.models import SingletonModel


def create_path_category(instance, filename):
    return os.path.join(
        str('image-default'),
        filename
    )


class SiteConfigurationM(SingletonModel):
    #page_facebook_url: str = models.CharField(verbose_name=_('Page of Facebook'), max_length=255, blank=True, null=True,
    #                                          default='#')
    #page_twitter_url: str = models.CharField(verbose_name=_('Page of Twitter'), max_length=255, blank=True, null=True,
    #                                         default='#')
    #page_instagram_url: str = models.CharField(verbose_name=_('Page of Instagram'), max_length=255, blank=True,
    #                                           null=True, default='#')
    #location: GeopositionField = GeopositionField(verbose_name=_('Location'), blank=True, null=True)
    #image: str = models.ImageField(
    #    verbose_name=_('Icon'), upload_to=create_path_category, blank=True, null=True
    #)

    def __str__(self):
        return "Site Configuration"

    class Meta:
        verbose_name = _("Site Configuration")
        verbose_name_plural = _('Site Configurations')