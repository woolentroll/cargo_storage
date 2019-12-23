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
    factory_number = forms.CharField(
        label="Заводской номер",
        max_length=60,
        widget=forms.TextInput(attrs={
            "placeholder": "Введите заводской номер"
        })
    )
    passport_number = forms.CharField(
        label="Номер паспорта",
        max_length=60,
        widget=forms.TextInput(attrs={
            "placeholder": "Введите номер паспорта"
        })
    )
    weight = forms.IntegerField(
        label="Вес",
        widget=forms.NumberInput(attrs={
            "placeholder": "0"
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
