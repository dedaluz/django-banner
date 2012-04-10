from django.db import models
from django.utils.translation import ugettext_lazy as _
from sorl.thumbnail import ImageField

from bohbou.web.managers import PublicManager

class Featured(models.Model):
    """
    (Featured description)
    """
    STATUS_CHOICES = (
        (0, _('Private')),
        (1, _('Draft')),
        (2, _('Public')),
    )
    
    caption = models.CharField(_('caption'), blank=True, max_length=255)
    image  = ImageField(_('picture'), upload_to='teasers', blank=True,)
    link    = models.URLField(blank=True, verify_exists=True)
    status  = models.IntegerField(_('status'), choices=STATUS_CHOICES, default=2)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    objects = PublicManager()
    
    class Meta:
        verbose_name_plural = 'Featured'
        ordering = ('-created',)
    
    
    # If using the get_absolute_url method, put the following line at the top of this file:
    from django.db.models import permalink
    
    @permalink
    def get_absolute_url(self):
        return ('featured_detail_view_name', [str(self.id)])
    

