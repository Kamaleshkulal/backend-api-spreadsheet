from django.db import models

class Spreadsheet(models.Model):
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class SpreadsheetSize(models.Model):
    spreadsheet = models.OneToOneField(Spreadsheet, related_name="size", on_delete=models.CASCADE)
    rows = models.IntegerField(default=10)  # Default row count
    columns = models.IntegerField(default=5)  # Default column count

    def __str__(self):
        return f"Size of {self.spreadsheet.name}: {self.rows}x{self.columns}"

class Cell(models.Model):
    spreadsheet = models.ForeignKey(Spreadsheet, related_name="cells", on_delete=models.CASCADE)
    row = models.IntegerField()
    column = models.IntegerField()
    value = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"Cell ({self.row}, {self.column}) in {self.spreadsheet.name}"

class SpreadsheetLink(models.Model):
    spreadsheet = models.OneToOneField(Spreadsheet, related_name="link", on_delete=models.CASCADE)
    link = models.URLField(max_length=500 , null=True , blank=True)  # URL to the Google Sheet or any link to the document

    def __str__(self):
        return f"Link for {self.spreadsheet.name}"
