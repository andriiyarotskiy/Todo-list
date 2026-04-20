import datetime

from django import forms
from django.utils import timezone

from todo.models import Task, Tag


class TaskForm(forms.ModelForm):
    deadline = forms.DateTimeField(
        initial=timezone.now() + datetime.timedelta(days=1),
        required=False,
        widget=forms.widgets.DateTimeInput(
            attrs={
                "type": "datetime-local",
                "min": timezone.now().isoformat(),
            },
        ),
    )
    content = forms.CharField(
        required=True, widget=forms.widgets.TextInput(attrs={"placeholder": "content"})
    )

    tags = forms.ModelMultipleChoiceField(
        queryset=Tag.objects.all(),
        required=False,
        widget=forms.widgets.CheckboxSelectMultiple,
    )

    def clean_deadline(self):
        deadline = self.cleaned_data.get("deadline")
        if deadline and deadline < timezone.now():
            raise forms.ValidationError("The date cannot be earlier than today.")
        return deadline

    class Meta:
        model = Task
        fields = "__all__"
