from django import forms


class DocumentForm(forms.Form):
    doc_number = forms.CharField(
        label="Номер документа",
        max_length=60,
        widget=forms.TextInput(attrs={
            "placeholder": "Document number"
        })
    )
    description = forms.CharField(
        label="Описание",
        max_length=200,
        widget=forms.Textarea(
            attrs={
                "placeholder": "Leave a description!"
            })
    )


class ItemForm(forms.Form):
    name = forms.CharField(
        label="Название груза",
        max_length=60,
        widget=forms.TextInput(attrs={
            "placeholder": "Введите название груза"
        })
    )
    description = forms.CharField(
        label="Описание",
        max_length=200,
        widget=forms.Textarea(
            attrs={
                "placeholder": "Введите описание"
            })
    )
