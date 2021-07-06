from django.db import models

class Portfolio(models.Model):
    """A portfolio as regard a particular project."""
    text = models.CharField(max_length=200)
    description = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """Returns a string representation of the model."""
        return self.text

class BackgroundImage(models.Model):
    """Image used as background for each project display."""
    portfolio = models.ForeignKey(Portfolio, on_delete=True)

    def __str__(self):
        """Return a string representation of img. background path"""
        return f"{self.text}"