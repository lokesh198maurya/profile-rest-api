from rest_framework import serializers


class HelloSerializers(serializers.Serializer):
    """Serializers a name filed for testing our API view"""

    name = serializers.CharField(max_length=10)