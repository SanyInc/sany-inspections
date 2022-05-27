from django.apps import AppConfig


class ChecklistsConfig(AppConfig):
    name = 'checklists'

    def ready(self):
        import checklists.signals 