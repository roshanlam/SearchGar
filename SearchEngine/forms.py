from django.forms import ModelForm, Textarea
from .models import SumbitWebsiteModel

class SubmitWebsiteForm(ModelForm):
    class Meta:
        model = SumbitWebsiteModel
        fields = "__all__"
        widgets = {
            'body': Textarea()
        }
