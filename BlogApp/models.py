from django.db import models


# Create your models here.
class Blog(models.Model):
    BlogImage = models.ImageField(verbose_name="Title image for post", upload_to='BlogImages/')
    BlogTitle = models.CharField(verbose_name="Blog title",max_length=100)
    BlogPubDate = models.DateField(verbose_name="Publish date")
    BlogCopy = models.TextField(verbose_name="Blog article content")

    def SummaryTextLimit(self):
        LimitChar = int((225-len("   ... Read More")))
        LimitRead = self.BlogCopy
        if len(LimitRead) > LimitChar:
            while LimitRead[LimitChar] != ' ':
                LimitChar -= 1
            return self.BlogCopy[:LimitChar] + "   ... Read More"
        else:
            return self.BlogCopy

    def __str__(self):
        return self.BlogTitle
