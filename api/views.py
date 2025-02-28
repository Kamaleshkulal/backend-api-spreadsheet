from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Spreadsheet, SpreadsheetLink, Cell, SpreadsheetSize
from .serializers import SpreadsheetSerializer, SpreadsheetLinkSerializer, CellSerializer, SpreadsheetSizeSerializer
from rest_framework import viewsets
from django.shortcuts import get_object_or_404
from .utils.google import create_google_sheet, get_google_sheet_link

class SpreadsheetViewSet(viewsets.ModelViewSet):
    queryset = Spreadsheet.objects.all()
    serializer_class = SpreadsheetSerializer

    def get_cells(self, request, pk=None):
        spreadsheet = get_object_or_404(Spreadsheet, pk=pk)
        cells = Cell.objects.filter(spreadsheet=spreadsheet)
        serializer = CellSerializer(cells, many=True)
        return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        """
        Override the default create method to generate a Google Sheets link after creating a new spreadsheet.
        """
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            # Save the new spreadsheet
            spreadsheet = serializer.save()
            
            # Generate Google Sheet link after creating a new spreadsheet
            google_sheet_link = create_google_sheet(spreadsheet.name)  # Calls the helper function to create the sheet
            
            # Create SpreadsheetLink object to store the Google Sheet link
            spreadsheet_link = SpreadsheetLink.objects.create(spreadsheet=spreadsheet, link=google_sheet_link)
            
            # Associate the link with the spreadsheet
            spreadsheet.link = spreadsheet_link
            spreadsheet.save()
            
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class SpreadsheetLinkView(APIView):
    def get(self, request, pk):
        """
        Retrieves the Google Sheet link for the given spreadsheet.
        """
        try:
            spreadsheet = Spreadsheet.objects.get(pk=pk)
            # Fetch the associated SpreadsheetLink
            link = spreadsheet.link.link  # Assuming the link field on SpreadsheetLink stores the link URL
        except Spreadsheet.DoesNotExist:
            return Response({"error": "Spreadsheet not found"}, status=status.HTTP_404_NOT_FOUND)
        except SpreadsheetLink.DoesNotExist:
            return Response({"error": "Google Sheet link not found"}, status=status.HTTP_404_NOT_FOUND)

        return Response({"link": link}, status=status.HTTP_200_OK)

    def put(self, request, pk):
        """
        Updates the Google Sheet link for the given spreadsheet.
        """
        try:
            spreadsheet = Spreadsheet.objects.get(pk=pk)
            link = spreadsheet.link  # Assuming there's a foreign key relationship to SpreadsheetLink
        except Spreadsheet.DoesNotExist:
            return Response({"error": "Spreadsheet not found"}, status=status.HTTP_404_NOT_FOUND)
        except SpreadsheetLink.DoesNotExist:
            return Response({"error": "Google Sheet link not found"}, status=status.HTTP_404_NOT_FOUND)

        # Update the link in SpreadsheetLink model
        serializer = SpreadsheetLinkSerializer(link, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class SpreadsheetSizeView(APIView):
    def get(self, request, spreadsheet_id):
        """
        Retrieves the size of the spreadsheet.
        """
        try:
            spreadsheet_size = SpreadsheetSize.objects.get(spreadsheet_id=spreadsheet_id)
            serializer = SpreadsheetSizeSerializer(spreadsheet_size)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except SpreadsheetSize.DoesNotExist:
            return Response({"error": "Spreadsheet size not found"}, status=status.HTTP_404_NOT_FOUND)

    def post(self, request, spreadsheet_id):
        """
        Creates a new spreadsheet size record.
        """
        try:
            spreadsheet = Spreadsheet.objects.get(id=spreadsheet_id)
        except Spreadsheet.DoesNotExist:
            return Response({"error": "Spreadsheet not found"}, status=status.HTTP_404_NOT_FOUND)

        serializer = SpreadsheetSizeSerializer(data=request.data, context={'spreadsheet_id': spreadsheet_id})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, spreadsheet_id):
        """
        Deletes a spreadsheet size record.
        """
        try:
            spreadsheet_size = SpreadsheetSize.objects.get(spreadsheet_id=spreadsheet_id)
            spreadsheet_size.delete()
            return Response({"message": "Spreadsheet size deleted"}, status=status.HTTP_204_NO_CONTENT)
        except SpreadsheetSize.DoesNotExist:
            return Response({"error": "Spreadsheet size not found"}, status=status.HTTP_404_NOT_FOUND)
