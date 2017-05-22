from rest_framework import serializers, exceptions
from django.contrib.auth.models import User
from custom_user.models import UserProfile
from dateutil.relativedelta import relativedelta
import datetime


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class UserProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    allowed = serializers.SerializerMethodField()
    bizzfuzz = serializers.SerializerMethodField()

    def get_allowed(self):
        years = relativedelta(datetime.now(), self.birthday).years
        return 'allow' if years > 13 else 'blocked'

    def get_bizzfuzz(self):
        if self.rand_field % 3 == 0 and self.rand_field % 5 == 0:
            return "BizzFuzz"
        if self.rand_field % 3 == 0:
            return "Bizz"
        if self.rand_field % 5 == 0:
            return "Fuzz"
        return None

    class Meta:
        model = UserProfile
        fields = ('user','birthday', 'bizzfuzz', 'rand_field', 'allowed')
