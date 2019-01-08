from django.db import models

# Create your models here.

class Type(models.Model):
    """Model representing a project type."""
    name = models.CharField(max_length=255, help_text='Enter a project type (e.g. Churn, Python, Neural Network)')

    def __str__(self):
        """String for representing the Model object."""
        return self.name


from django.urls import reverse  # Used to generate URLs by reversing the URL patterns


class Project(models.Model):
    """Model representing a project (but not a specific copy of a projet)."""
    title = models.CharField(max_length=255)

    summary = models.TextField(max_length=1000, help_text='Enter a brief description of the project')

    date = models.DateField(null=True)
    # ManyToManyField used because a type can contain many projects. A project can have many types.
    project_type = models.ManyToManyField(Type, help_text='Select a type for this project')

    repo_link = models.URLField(null=True)
    image = models.ImageField(null=True)


    def __str__(self):
        """String for representing the Model object."""
        return self.title

    def get_absolute_url(self):
        """Returns the url to access a detail record for this project."""
        return reverse('project-detail', args=[str(self.id)])

