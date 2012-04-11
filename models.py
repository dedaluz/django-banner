from django.db import models
from django.utils.translation import ugettext_lazy as _
from sorl.thumbnail import ImageField


from managers import PublicManager

class FeaturedSlide(models.Model):
    """
    (Featured description)
    """
    STATUS_CHOICES = (
        (0, _('Private')),
        (1, _('Draft')),
        (2, _('Public')),
    )
    
    caption = models.CharField(_('caption'), blank=True, max_length=255)
    description = models.TextField(blank=True)
    image  = ImageField(_('picture'), upload_to='teasers', blank=True,)
    link    = models.URLField(blank=True, verify_exists=True)
    status  = models.IntegerField(_('status'), choices=STATUS_CHOICES, default=2)
    # position field
    position = models.PositiveSmallIntegerField("Position")
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    objects = PublicManager()
    
    class Meta:
        verbose_name = u'Featured Slide'
        verbose_name_plural = 'Featured Slides'
        ordering = ('position',)
    
    
    # If using the get_absolute_url method, put the following line at the top of this file:
    from django.db.models import permalink
    
    @permalink
    def get_absolute_url(self):
        return ('featured_detail_view_name', [str(self.id)])
    
class FeaturedAlbum(models.Model):
    """Image gallery for slider"""
    name = models.CharField(max_length=150)
    images = models.ManyToManyField(SliderImage, blank=True)

    class Meta:
        verbose_name = u'Featured Album'
        verbose_name_plural = u'Featured Albums'

    def __unicode__(self):
        return self.name
