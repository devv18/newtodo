from rest_framework import serializers
from .models import Todo


class TodoSerializer(serializers.ModelSerializer):
    tags = serializers.ListField(child=serializers.CharField(), required=False)

    class Meta:
        model = Todo
        fields = [
                    'id',
                    'timestamp',
                    'title',
                    'description',
                    'due_date',
                    'status',
                    'tags',
                ]

        read_only_fields = ['timestamp']

    def create(self, validated_data):
        tags_data = validated_data.pop('tags', [])
        todo = Todo.objects.create(**validated_data, tags=tags_data)
        return todo

    def update(self, instance, validated_data):
        tags_data = validated_data.pop('tags', [])
        instance.title = validated_data.get('title', instance.title)
        instance.description = validated_data.get('description',
                                                 instance.description)
        instance.due_date = validated_data.get('due_date', instance.due_date)
        instance.status = validated_data.get('status', instance.status)
        instance.tags = tags_data
        instance.save()
        return instance
