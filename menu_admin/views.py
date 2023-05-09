from http.client import HTTPResponse
from rest_framework import mixins, viewsets
from django.shortcuts import render

from menu_admin.models import MenuItem
from menu_admin.serilaizers import AccountSerializer


class Register_token_in_the_views(mixins.ListModelMixin, viewsets.GenericViewSet):
    queryset = MenuItem.objects.all()
    serializer_class = AccountSerializer

    def get_queryset(self):
        return MenuItem.objects.all()


def main_view(request) -> HTTPResponse:
    if request.method == 'GET':

        return render(request, 'menu_admin/index.html')


def second_view(request) -> HTTPResponse:
    if request.method == 'GET':

        return render(request, 'menu_admin/index.html')


def third_view(request) -> HTTPResponse:
    if request.method == 'GET':

        return render(request, 'menu_admin/index.html')


def fourth_view(request) -> HTTPResponse:
    if request.method == 'GET':

        return render(request, 'menu_admin/index.html')


def fifth_view(request) -> HTTPResponse:
    if request.method == 'GET':

        return render(request, 'menu_admin/index.html')


def sixth_view(request) -> HTTPResponse:
    if request.method == 'GET':

        return render(request, 'menu_admin/index.html')
