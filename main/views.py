from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404

# Create your views here.
from django.urls import reverse

from main.forms import DocumentForm, ItemForm
from main.models import Operation, Document, ItemEntry, Item


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


def docs(request):
    """Хендлер кнопки Документы"""
    context = {
        "nipa": 123,
    }
    return render(request, "docs.html", context)


def docs_in(request):
    """Хендлер кнопки Документы-Приходная накладная"""
    documents = Document.objects.filter(
        doc_number__isnull=False,
        doc_type=0
    ).exclude(doc_number='').values('pk', 'doc_number', 'date_created', 'description')
    doc_number = request.GET.get('doc_number')
    if doc_number:
        documents = documents.filter(doc_number=doc_number)
    context = {
        "documents": documents,
    }
    return render(request, "docs_in.html", context)


def docs_in_create(request):
    operation = Operation(operation_type=0)
    operation.save()
    document = Document(doc_type=0, operation=operation)
    document.save()

    return HttpResponseRedirect(reverse('main:docs_in_edit', args=(document.pk,)))


def docs_in_edit(request, document_id):
    """Хендлер кнопки Документы-Приходная накладная - Добавить/Изменить"""
    document = get_object_or_404(Document, pk=document_id, doc_type=0)

    if request.method == "POST":
        form = DocumentForm(request.POST)
        if form.is_valid():
            document.doc_number = form.cleaned_data["doc_number"]
            document.description = form.cleaned_data["description"]
            document.save()
            return HttpResponseRedirect(reverse('main:docs_in_edit', args=(document.pk,)))
    else:
        form = DocumentForm({"doc_number": document.doc_number, "description": document.description})

    result = []
    for e in document.operation.entries.all():
        result.append({
            'pk': e.pk,
            'name': e.item.name,
            'factory_number': e.item.factory_number,
            'passport_number': e.item.passport_number,
            'weight': e.item.weight,
        })
    context = {
        "items": result,
        "document": document,
        "form_doc": form,
        "form_item": ItemForm()
    }

    return render(request, "docs_in_edit.html", context)


def docs_in_add_item(request, document_id):
    document = get_object_or_404(Document, pk=document_id, doc_type=0)

    if request.method == "POST":
        form = ItemForm(request.POST)
        if form.is_valid():
            # найдем такой же груз
            items = Item.objects.filter(factory_number=form.cleaned_data["factory_number"])
            if items.exists():
                # пока берем первый, но вообще единица должна быть уникальной
                item = items.first()
            else:
                item = Item(
                    name=form.cleaned_data["name"],
                    factory_number=form.cleaned_data["factory_number"],
                    passport_number=form.cleaned_data["passport_number"],
                    weight=form.cleaned_data["weight"],
                )
                item.save()
            entry = ItemEntry(
                description=form.cleaned_data["description"],
                item=item,
                operation=document.operation
            )
            entry.save()
    return HttpResponseRedirect(reverse('main:docs_in_edit', args=(document.pk,)))


def docs_in_del_item(request, item_id):
    entry = get_object_or_404(ItemEntry, pk=item_id, operation__operation_type=0)
    document = entry.operation.documents.first()
    entry.delete()
    return HttpResponseRedirect(reverse('main:docs_in_edit', args=(document.pk,)))


def docs_in_print(request, document_id):
    document = get_object_or_404(Document, pk=document_id, doc_type=0)

    result = []
    for e in document.operation.entries.all():
        result.append({'name': e.item.name})
    context = {
        "doc_number": document.doc_number,
        "date_created": document.date_created,
        "items": result,
    }
    return render(request, "docs_in_print.html", context)


def docs_out(request):
    """Хендлер кнопки Документы-Расходная накладная"""
    documents = Document.objects.filter(
        doc_number__isnull=False,
        doc_type=1
    ).exclude(doc_number='').values('pk', 'doc_number', 'date_created', 'description')
    doc_number = request.GET.get('doc_number')
    if doc_number:
        documents = documents.filter(doc_number=doc_number)
    context = {
        "documents": documents,
    }
    return render(request, "docs_out.html", context)


def docs_out_create(request):
    operation = Operation(operation_type=1)
    operation.save()
    document = Document(doc_type=1, operation=operation)
    document.save()

    return HttpResponseRedirect(reverse('main:docs_out_edit', args=(document.pk,)))


def docs_out_edit(request, document_id, **kwargs):
    """Хендлер кнопки Документы-Расходная накладная - Добавить/Изменить"""
    document = get_object_or_404(Document, pk=document_id, doc_type=1)

    if request.method == "POST":
        form = DocumentForm(request.POST)
        if form.is_valid():
            document.doc_number = form.cleaned_data["doc_number"]
            document.description = form.cleaned_data["description"]
            document.save()
            return HttpResponseRedirect(reverse('main:docs_out_edit', args=(document.pk,)))
    else:
        form = DocumentForm({"doc_number": document.doc_number, "description": document.description})

    result = []
    for e in document.operation.entries.all():
        result.append({
            'pk': e.pk,
            'name': e.item.name,
            'factory_number': e.item.factory_number,
            'passport_number': e.item.passport_number,
            'weight': e.item.weight,
        })
    context = {
        "items": result,
        "document": document,
        "form_doc": form,
        "error_message": kwargs.get('error_message'),
    }

    return render(request, "docs_out_edit.html", context)


def docs_out_print(request, document_id):
    document = get_object_or_404(Document, pk=document_id, doc_type=1)

    result = []
    for e in document.operation.entries.all():
        result.append({'name': e.item.name})
    context = {
        "doc_number": document.doc_number,
        "date_created": document.date_created,
        "items": result,
    }
    return render(request, "docs_out_print.html", context)


def docs_out_add_item(request, document_id):
    document = get_object_or_404(Document, pk=document_id, doc_type=1)

    if request.method == "POST":
        # найдем такой же груз
        item = Item.objects.filter(factory_number=request.POST["factory_number"])
        if item.exists():
            item = item.first()
            # проверяем, что последней проводкой был приход
            entries = item.entries.values('pk', 'date_created', 'operation__operation_type').order_by('date_created')
            if entries.exists() and entries.last()['operation__operation_type'] == 0:
                entry = ItemEntry(item=item, operation=document.operation)
                entry.save()

    return HttpResponseRedirect(reverse('main:docs_out_edit', args=(document.pk, )))


def docs_out_del_item(request, item_id):
    entry = get_object_or_404(ItemEntry, pk=item_id, operation__operation_type=1)
    document = entry.operation.documents.first()
    entry.delete()
    return HttpResponseRedirect(reverse('main:docs_out_edit', args=(document.pk,)))


def get_items_report(request):
    item_name = request.GET.get('item_name')
    factory_number = request.GET.get('factory_number')
    status = request.GET.get('status')

    queryset = Item.objects.all()
    if item_name:
        queryset = queryset.filter(name__contains=item_name)
    if factory_number:
        queryset = queryset.filter(factory_number=factory_number)

    result = []
    for item in queryset:
        data = {
            'name': item.name,
            'factory_number': item.factory_number,
            'passport_number': item.passport_number,
            'weight': item.weight
        }
        # находим статус груза
        if item.entries.exists():
            last_entry = item.entries.last()
            if last_entry.operation.operation_type == 0:
                data['current_status'] = "На хранении"
                data['date_arrival'] = last_entry.date_created
                data['date_departure'] = ""
                data['entry_in'] = last_entry.operation.documents.last().doc_number
                data['entry_out'] = ""
            else:
                data['current_status'] = "Отгружен"
                last_arrival = item.entries.filter(operation__operation_type=0).order_by('date_created').last()
                data['date_arrival'] = last_arrival.date_created if last_arrival else item.date_created
                data['date_departure'] = last_entry.date_created
                data['entry_in'] = last_arrival.operation.documents.last().doc_number
                data['entry_out'] = last_entry.operation.documents.last().doc_number
        result.append(data)
    if status:
        result = [r for r in result if r['current_status'] == status]
    return render(request, "reports.html", {'total': len(result), 'records': result})
