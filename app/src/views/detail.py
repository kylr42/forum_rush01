from typing import Any, Dict
from django.views.generic import DetailView
from ..models.article import Article

class Detail(DetailView):
    model = Article
    template_name = 'detail.html'
    context_object_name = 'post'

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        return context
