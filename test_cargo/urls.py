from django.urls import path
from . import views

urlpatterns = [
    path("", views.test_login, name="test_login"),
    path("index/", views.test_cargo_index, name="test_cargo_index"),
    path("list/", views.test_cargo_list, name="test_cargo_list"),
    path("docs/", views.test_cargo_docs, name="test_cargo_docs"),
    path("reports/", views.test_cargo_reports, name="test_cargo_reports"),
    path("docs/in/", views.test_cargo_docs_in, name="test_cargo_docs_in"),
    path("docs/out/", views.test_cargo_docs_out, name="test_cargo_docs_out"),
    path("docs/in/create/", views.test_cargo_docs_in_create, name="test_cargo_docs_in_create"),
    path("docs/in/<int:document_id>/", views.test_cargo_docs_in_edit, name="test_cargo_docs_in_edit"),
    path("docs/out/edit/", views.test_cargo_docs_out_edit, name="test_cargo_docs_out_edit"),
]
