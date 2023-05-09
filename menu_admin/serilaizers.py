from rest_framework import serializers

from menu_admin.models import MenuItem


class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = MenuItem
        fields = "__all__"