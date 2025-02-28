from django.urls import path
from .views import SpreadsheetViewSet, SpreadsheetLinkView, SpreadsheetSizeView
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'spreadsheets', SpreadsheetViewSet)

urlpatterns = [
    path('spreadsheets/<int:pk>/link/', SpreadsheetLinkView.as_view(), name='spreadsheet-link'),
    path('spreadsheets/<int:spreadsheet_id>/size/', SpreadsheetSizeView.as_view(), name='spreadsheet-size'),
]

urlpatterns += router.urls
