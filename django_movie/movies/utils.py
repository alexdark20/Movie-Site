from.models import *


class DataMixin:
    def get_user_context(self,**kwargs):
        context=kwargs
        context['genres'] = Genre.objects.all()
        return context
