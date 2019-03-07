from django import forms
from .models import Zuke_User, User_Filters, Zuke_Subscribed, Videos

class Login_Form(forms.Form):
    email = forms.EmailField(
        widget=forms.EmailInput(
            attrs={"placeholder": "enter email", "class": "form-control fnsbig"}
        )
    )

    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={"placeholder": "enter password", "class": "form-control fnsbig"}
        )
    )


class Change_Password_Form(forms.Form):
    email = forms.EmailField(
        widget=forms.EmailInput(
            attrs={"placeholder": "enter email", "class": "form-control fnsbig"}
        )
    )

    password = forms.CharField(
        label="Current Password",
        widget=forms.PasswordInput(
            attrs={"placeholder": "enter password", "class": "form-control fnsbig"}
        )
    )

    new_password = forms.CharField(
        label="New Password",
        widget=forms.PasswordInput(
            attrs={"placeholder": "enter password", "class": "form-control fnsbig"}
        )
    )

    confirm_password = forms.CharField(
        label="Confirm Password",
        widget=forms.PasswordInput(
            attrs={"placeholder": "enter password", "class": "form-control fnsbig"}
        )
    )

    def clean(self):
        cleaned_data = super(Change_Password_Form, self).clean()
        password = cleaned_data.get("new_password")
        confirm_password = cleaned_data.get("confirm_password")
        if password != confirm_password:
            raise forms.ValidationError("password and confirm_password does not match")


class Add_User_Form(forms.Form):
    class Meta:  
        model = Zuke_User
        fields = "__all__"

    gender = (("Male", "Male"), ("Female", "Female"), ("Other", "Other"))

    name = forms.CharField(
        widget=forms.TextInput(attrs={"class": "form-control fnsbig","placeholder": "enter name",})
    )

    dob = forms.DateField(
        label="date",
        input_formats=['%d/%m/%Y'],
        widget=forms.DateInput(attrs={"class":"form-control","placeholder": "dd/mm/yyyy",}
        )
    )
    sex = forms.ChoiceField(
        choices=gender, widget=forms.RadioSelect(attrs={"class": "ritem form-radio"})
    )
    phone = forms.CharField(
        widget=forms.TextInput(attrs={"class": "form-control fnsbig","placeholder": "enter phone",})
    )

    email = forms.EmailField(
        widget=forms.EmailInput(
            attrs={"placeholder": "enter email", "class": "form-control fnsbig"}
        )
    )

    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={"placeholder": "enter password", "class": "form-control fnsbig"}
        )
    )

class UserFilter_Form(forms.ModelForm):
    class Meta:
        model = User_Filters
        fields = ["search"]

    search = forms.CharField(
        label="",
        widget=forms.TextInput(attrs={"class": "form-control fnsbig","placeholder": "Search",})
    )

class Add_Video_Form(forms.Form):
    gene = (("music","music"),("horror","horror"),("love","love"),("action","action"),("music","music"),("comedy","comedy"))

    video_title = forms.CharField(
        widget=forms.TextInput(attrs={"class": "form-control fnsbig","placeholder": "enter title",})
    )

    vtype = forms.CharField(
        widget=forms.TextInput(attrs={"class": "form-control fnsbig","placeholder": "enter label",})
    )

    label = forms.CharField(
        widget=forms.TextInput(attrs={"class": "form-control fnsbig","placeholder": "enter label",})
    )

    contents = forms.CharField(
        widget=forms.TextInput(attrs={"class": "form-control fnsbig","placeholder": "enter content",})
    )

    genere = forms.ChoiceField(
        choices=gene, widget=forms.Select(attrs={"class": "form-control"})
    )

    no_words =forms.CharField(
        widget=forms.TextInput(attrs={"class": "form-control fnsbig","placeholder": "enter words",})
    )

    no_sentences = forms.CharField(
        widget=forms.TextInput(attrs={"class": "form-control fnsbig","placeholder": "enter matter",})
    )

    description = forms.CharField(
        widget=forms.TextInput(attrs={"class": "form-control fnsbig","placeholder": "enter description",})
    )

    videos = forms.FileField(
        widget=forms.FileInput(attrs={"class": "form-control-file fnsbig"})
    )

    