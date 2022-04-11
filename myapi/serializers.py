


from rest_framework import serializers

from .models import Emp

class EmpSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)

    class Meta:
        model = Emp
        fields = ('id', 'location', 'department', 'category', 'subcategory')


'''



from rest_framework import serializers

from .models import Emp

class EmpSerializer(serializers.HyperlinkedModelSerializer):

    id = serializers.IntegerField(read_only=True)
    location = serializers.CharField(required=False, allow_blank=True, max_length=100)
    department = serializers.CharField(required=False, allow_blank=True, max_length=100)
    category = serializers.CharField(required=False, allow_blank=True, max_length=100)
    subcategory = serializers.CharField(required=False, allow_blank=True, max_length=100)


    def create(self, validated_data):

        return Emp.objects.create(**validated_data)

    def update(self, instance, validated_data):

        instance.location = validated_data.get('location', instance.location)
        instance.department = validated_data.get('department', instance.department)
        instance.category = validated_data.get('category', instance.category)
        instance.subcategory = validated_data.get('subcategory', instance.subcategory)
        instance.save()
        return instance




'''