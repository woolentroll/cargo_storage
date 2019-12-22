from django.shortcuts import render

# Create your views here.
from test_cargo.models import Operation, Document


def test_login(request):
    context = {
        "nipa": 123,
    }
    return render(request, "test_login.html", context)


def test_cargo_index(request):
    context = {
        "nipa": 123,
    }
    return render(request, "test_cargo_index.html", context)


def test_cargo_list(request):
    """Хендлер кнопки Грузы"""
    context = {
        "nipa": 123,
    }
    return render(request, "test_cargo_list.html", context)


def test_cargo_docs(request):
    """Хендлер кнопки Документы"""
    context = {
        "nipa": 123,
    }
    return render(request, "test_cargo_docs.html", context)


def test_cargo_reports(request):
    """Хендлер кнопки Отчеты"""
    context = {
        "nipa": 123,
    }
    return render(request, "test_cargo_reports.html", context)


def test_cargo_docs_in(request):
    """Хендлер кнопки Документы-Приходная накладная"""
    documents = Document.objects.all().values('pk', 'doc_number', 'date_created', 'description')
    context = {
        "documents": documents,
    }
    return render(request, "test_cargo_docs_in.html", context)


def test_cargo_docs_out(request):
    """Хендлер кнопки Документы-Расходная накладная"""
    context = {
        "nipa": 123,
    }
    return render(request, "test_cargo_docs_out.html", context)


def test_cargo_docs_in_edit(request, document_id):
    """Хендлер кнопки Документы-Приходная накладная - Добавить/Изменить"""
    document = Document.objects.get(pk=document_id)
    result = []
    for e in document.operation.entries.all():
        result.append({'description': e.item.description})
    context = {
        "nipa": 123,
        "items": result
    }
    return render(request, "test_cargo_docs_in_edit.html", context)


def test_cargo_docs_out_edit(request):
    """Хендлер кнопки Документы-Расходная накладная - Добавить/Изменить"""
    context = {
        "nipa": 123,
    }
    return render(request, "test_cargo_docs_out_edit.html", context)


def test_cargo_docs_in_create(request):
    context = {
        "nipa": 123,
    }
    return render(request, "test_cargo_docs_in_edit.html", context)