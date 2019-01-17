from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import ContractDetails

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')

class ContractDetailsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ContractDetails
        fields = ('url', 'license_name','ethereum_address','validity_date','hardware_id','license_type','contract_bytecode','contract_abi','tx_hash')