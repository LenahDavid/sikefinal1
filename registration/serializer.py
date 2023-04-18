from .models import table
from rest_framework import serializers
from .models import table

class TableSerializers(serializers.ModelSerializer):
    

    class Meta:
        model=table
        fields =('id','Firstname', 'Lastname', 'surname', 'Email', 'Phone_number', 'Age', 'Gender', 'nationality', 'City', 'country', 'address1', 'Address2', 'PostalCode', 'Password')

