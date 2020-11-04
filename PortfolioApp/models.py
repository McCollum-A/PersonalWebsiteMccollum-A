from django.db import models


class Portfolio(models.Model):

    PortfolioImage = models.ImageField(verbose_name="Project title image", upload_to='PortfioloImages/')
    PortfolioSummary = models.TextField(verbose_name="Project summary, single view", default="Explain the piece here")
    PortfolioTitle = models.CharField(verbose_name="Project title or name", max_length=100, default="Project Title")
    PortfolioTag = models.CharField(verbose_name="Project tag for gallery view", max_length=150)
    PortfolioItemDate = models.CharField(verbose_name="Year of completion", max_length=9, default="2020")

    class Meta:
        verbose_name="Portfolio piece"


    def __str__(self):
        return self.PortfolioTitle
