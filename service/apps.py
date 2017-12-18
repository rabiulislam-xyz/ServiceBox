from django.apps import AppConfig
import algoliasearch_django as algoliasearch

class ServiceConfig(AppConfig):
    name = 'service'

    def ready(self):
        service = self.get_model('Service')
        algoliasearch.register(service)