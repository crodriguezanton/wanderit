from django.utils.translation import ugettext as _

CRONJOB_TYPE_CHOICES = (
    (0, _('Continuous')),
    (1, _('Fixed Time')),
    (2, _('Interval')),
    (3, _('Dialy')),
    (4, _('Weekly')),
    (5, _('Monthly')),
)

PRIORITY = (
    (0, _('Realtime')),
    (1, _('High')),
    (2, _('Medium')),
    (3, _('Low')),
)

TIME_UNITS = (
    (0, _('Seconds')),
    (1, _('Minutes')),
    (2, _('Hours')),
)