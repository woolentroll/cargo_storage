from django.urls import path
from . import views

app_name = 'main'
urlpatterns = [
    path("", views.login, name="login"),
    path("index/", views.index, name="index"),
    path("list/", views.list, name="items_list"),
    path("docs/", views.docs, name="docs"),
    path("reports/", views.reports, name="reports"),
    path("docs/in/", views.docs_in, name="docs_in"),
    path("docs/out/", views.docs_out, name="docs_out"),
    path("docs/in/create/", views.docs_in_create, name="docs_in_create"),
    path("docs/in/<int:document_id>/add_item", views.docs_in_add_item, name="docs_in_add_item"),
    path("docs/in/<int:document_id>/", views.docs_in_edit, name="docs_in_edit"),
    path("docs/out/edit/", views.docs_out_edit, name="docs_out_edit"),
]
