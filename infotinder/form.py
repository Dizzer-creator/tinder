from allauth.account.forms import SignupForm
from django import forms


class MyCustomSignUpForm(SignupForm):
    def __init__(self, *args, **kwargs):
        FUND = "Фонд"
        COMPANY = "Компания"
        PRIVATE = "Частное лицо"
        ORGANIZATION_TYPE = [
            (FUND, "Фонд"),
            (COMPANY, "Компания"),
            (PRIVATE, "Частное лицо"),
        ]
        super(MyCustomSignUpForm, self).__init__(*args, **kwargs)
        self.fields["Имя:"] = forms.CharField(required=True, widget=forms.TextInput(attrs={"placeholder": "Имя"}))
        self.fields["Фамилия:"] = forms.CharField(
            required=True, widget=forms.TextInput(attrs={"placeholder": "Фамилия"})
        )
        self.fields["Тип организации:"] = forms.ChoiceField(required=False, choices=ORGANIZATION_TYPE)

    def save(self, request):
        first_name = self.cleaned_data.pop("Имя:")
        last_name = self.cleaned_data.pop("Фамилия:")
        organization_type = self.cleaned_data.pop("Тип организации:")
        user = super(MyCustomSignUpForm, self).save(request)
        user.first_name = first_name
        user.last_name = last_name
        user.organization_types = organization_type
        user.save()
        return user
