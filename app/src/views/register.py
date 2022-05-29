from typing import Any, Dict
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth import login
from ..forms.register import RegisterForm

class Register(CreateView):
    form_class = RegisterForm
    template_name = 'register.html'
    success_url = reverse_lazy('index')

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        return context

    def form_valid(self, form: RegisterForm):
        user = form.save()
        login(self.request, user)
        return redirect('index')
