from django.shortcuts import render

# Create your views here.
from main.models import Operation, Document


def login(request):
    context = {
        "nipa": 123,
    }
    return render(request, "login.html", context)


def index(request):
    context = {
        "nipa": 123,
    }
    return render(request, "index.html", context)


def list(request):
    """Хендлер кнопки Грузы"""
    context = {
        "nipa": 123,
    }
    return render(request, "list.html", context)


def docs(request):
    """Хендлер кнопки Документы"""
    context = {
        "nipa": 123,
    }
    return render(request, "docs.html", context)


def reports(request):
    """Хендлер кнопки Отчеты"""
    context = {
        "nipa": 123,
    }
    return render(request, "reports.html", context)


def docs_in(request):
    """Хендлер кнопки Документы-Приходная накладная"""
    documents = Document.objects.all().values('pk', 'doc_number', 'date_created', 'description')
    context = {
        "documents": documents,
    }
    return render(request, "docs_in.html", context)


def docs_out(request):
    """Хендлер кнопки Документы-Расходная накладная"""
    context = {
        "nipa": 123,
    }
    return render(request, "docs_out.html", context)


def docs_in_edit(request, document_id):
    """Хендлер кнопки Документы-Приходная накладная - Добавить/Изменить"""
    document = Document.objects.get(pk=document_id)
    result = []
    for e in document.operation.entries.all():
        result.append({'description': e.item.description})
    context = {
        "nipa": 123,
        "items": result
    }
    return render(request, "docs_in_edit.html", context)


def docs_out_edit(request):
    """Хендлер кнопки Документы-Расходная накладная - Добавить/Изменить"""
    context = {
        "nipa": 123,
    }
    return render(request, "docs_out_edit.html", context)


def docs_in_create(request):
    context = {
        "nipa": 123,
    }
    return render(request, "docs_in_edit.html", context)