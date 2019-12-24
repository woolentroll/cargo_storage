from django.urls import path
from . import views

app_name = 'main'
urlpatterns = [
    path("", views.login, name="login"),
    path("index/", views.index, name="index"),
    path("docs/", views.docs, name="docs"),
    path("reports/", views.get_items_report, name="reports"),

    path("docs/in/", views.docs_in, name="docs_in"),
    path("docs/in/create/", views.docs_in_create, name="docs_in_create"),
    path("docs/in/<int:item_id>/del_item", views.docs_in_del_item, name="docs_in_del_item"),
    path("docs/in/<int:document_id>/add_item", views.docs_in_add_item, name="docs_in_add_item"),
    path("docs/in/<int:document_id>/", views.docs_in_edit, name="docs_in_edit"),
    path("docs/in/print/<int:document_id>/", views.docs_in_print, name="docs_in_print"),

    path("docs/out/", views.docs_out, name="docs_out"),
    path("docs/out/create/", views.docs_out_create, name="docs_out_create"),
    path("docs/out/<int:item_id>/del_item", views.docs_out_del_item, name="docs_out_del_item"),
    path("docs/out/<int:document_id>/add_item", views.docs_out_add_item, name="docs_out_add_item"),
    path("docs/out/<int:document_id>/", views.docs_out_edit, name="docs_out_edit"),
    path("docs/out/print/<int:document_id>/", views.docs_out_print, name="docs_out_print"),
]
