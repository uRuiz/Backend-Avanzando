from django.utils.translation import ugettext as _
from django.contrib.auth.models import User
from rest_framework import serializers

from followers.models import Relationship


class RelationshipUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User


class RelationshipSerializer(serializers.ModelSerializer):

    class Meta:
        model = Relationship
        read_only_fields = ('origin',)

    def validate(self, attrs):
        request_user = self.context.get('request').user
        if request_user == attrs.get('target'):
            raise serializers.ValidationError(_("You cannot follow yourself"))
        if Relationship.objects.filter(origin=request_user, target=attrs.get('target')).exists():
            raise serializers.ValidationError(_("You already follow this user"))
        return attrs
