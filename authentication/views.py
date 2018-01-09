from django.views import generic


class LoginView(generic.TemplateView):
    template_name = 'login.html'
