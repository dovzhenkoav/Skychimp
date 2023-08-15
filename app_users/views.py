from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views import generic

from app_users.models import User
from app_users.forms import UserRegisterForm, RecoverPasswordForm
from services.email import get_verification_code, send_registration_email
from services.recover_password import user_set_random_password


class UserRegisterView(generic.CreateView):
    model = User
    form_class = UserRegisterForm
    template_name = 'app_users/register.html'
    success_url = reverse_lazy('app_users:register_confirmation')

    def form_valid(self, form):
        """Send verification code after registration."""
        if form.is_valid():
            new_form = form.save()
            new_form.verify_code = get_verification_code()

            send_registration_email(new_form.email, new_form.verify_code)

            new_form.save()
        return super().form_valid(form)


class UserRegisterConfirmationView(generic.TemplateView):
    template_name = 'app_users/register_confirmation.html'


def verify_view(request, code):
    """Verify user profile and makes it active."""
    user = User.objects.get(verify_code=str(code))
    user.is_active = True
    user.verify_code = 'NULL'
    user.save()
    return redirect('app_users:login')


def recover_password_view(request):
    """User forget password page. Can set another password to user. And send email with new password."""
    if request.method == 'POST':
        recover_form = RecoverPasswordForm(request.POST)
        if recover_form.is_valid():
            email = recover_form.cleaned_data['email']
            try:
                user = User.objects.get(email=email)

                user_set_random_password(user)

                return redirect('app_users:recover_password_confirmation')
            except ObjectDoesNotExist:
                form = RecoverPasswordForm()
                context = {'form': form,
                           'user_does_not_exists': recover_form.cleaned_data['email']}
                return render(request, 'app_users/recover_password.html', context=context)
    else:
        form = RecoverPasswordForm()
        context = {'form': form}
        return render(request, 'app_users/recover_password.html', context=context)


class RecoverPasswordConfirmationView(generic.TemplateView):
    template_name = 'app_users/recover_password_confirmation.html'
