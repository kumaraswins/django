from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _
from suit.apps import DjangoSuitConfig

class UsersConfig(AppConfig):
    name = "project.users"
    verbose_name = _("Users")

    def ready(self):
        try:
            import project.users.signals  # noqa F401
        except ImportError:
            pass



class SuitConfig(DjangoSuitConfig):
    layout = 'vertical'