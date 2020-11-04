from django.db import models


class Works(models.Model):

    StepFilter = "All"
    WorksImage = models.ImageField(verbose_name="Project title image", upload_to='WorksImages/')
    WorksImage2nd = models.ImageField(verbose_name="Second supporting image", upload_to='WorksImages/', default="null")
    WorksImage3rd = models.ImageField(verbose_name="Third supporting image", upload_to='WorksImages/', default="null")
    WorksTitle = models.CharField(verbose_name="Project title and name", max_length=100, default="Work Title")
    WorksSummary = models.CharField(verbose_name="Brief project description", max_length=150, default="Enter home view tag")
    WorksContent = models.TextField(verbose_name="Full project article", default="Enter content here")


    class WorksFilterType(models.TextChoices):
        DEVELOPMENT = 'Development'
        ARTORDESIGN = 'ArtorDesign'

    WorksFilterTypeChar = models.CharField(
        max_length=13,
        choices=WorksFilterType.choices,
        default=WorksFilterType.DEVELOPMENT,
        verbose_name="Content type for filter"
    )

    def __str__(self):
        return self.WorksTitle

    class Meta:
        verbose_name = "Current project"  # for some reason Django tacks an "s" on the end
