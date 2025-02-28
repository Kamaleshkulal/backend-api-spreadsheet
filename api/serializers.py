from rest_framework import serializers
from .models import Spreadsheet, Cell, SpreadsheetSize, SpreadsheetLink

class SpreadsheetSizeSerializer(serializers.ModelSerializer):
    class Meta:
        model = SpreadsheetSize
        fields = ['rows', 'columns']

    def create(self, validated_data):
        spreadsheet_id = self.context['spreadsheet_id']
        spreadsheet_size, created = SpreadsheetSize.objects.update_or_create(
            spreadsheet_id=spreadsheet_id,
            defaults=validated_data
        )
        return spreadsheet_size

class CellSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cell
        fields = '__all__'

class SpreadsheetLinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = SpreadsheetLink
        fields = ['spreadsheet', 'link']

class SpreadsheetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Spreadsheet
        fields = ['id', 'name', 'created_at']
