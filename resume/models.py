from django.db import models


class ResumePageModel(models.Model):
    intro = models.TextField(null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.intro[:50]

    class Meta:
        verbose_name = 'Resume Page'
        verbose_name_plural = 'Resume Page'


class EducationsModel(models.Model):
    title = models.CharField(max_length=100)
    from_date = models.DateField()
    to_date = models.DateField()
    present_on = models.BooleanField(null=False)
    institution = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    head = models.ForeignKey(ResumePageModel, on_delete=models.CASCADE, related_name='educations')



    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Education'
        verbose_name_plural = 'Educations'



class ExperiencesModel(models.Model):
    position = models.CharField(max_length=100)
    from_date = models.DateField(null=True, blank=True)
    to_date = models.DateField(null=True, blank=True)
    present_on = models.BooleanField(null=False)
    company = models.CharField(max_length=100)


    text1 = models.TextField(null=True, blank=True)
    text2 = models.TextField(null=True, blank=True)
    text3 = models.TextField(null=True, blank=True)
    text4 = models.TextField(null=True, blank=True)

    head = models.ForeignKey(ResumePageModel, on_delete=models.CASCADE, related_name='experiences')

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.position

    class Meta:
        verbose_name = 'Work Experience'
        verbose_name_plural = 'Work Experiences'


class SummaryModel(models.Model):
    section_title = models.CharField(max_length=25) # someone might call it, for example, "overall"; therefore i made this section name dynamic
    name = models.CharField(max_length=50)
    long_description = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.section_title

    class Meta:
        verbose_name = 'Resume Page Summary'
        verbose_name_plural = 'Resume Page Summary'


class SummarySmallInfosModel(models.Model):
    short_text = models.CharField(max_length=60)
    head = models.ForeignKey(SummaryModel, on_delete=models.CASCADE, related_name='short_texts')

    def __str__(self):
        return self.short_text

    class Meta:
        verbose_name = 'Text'
        verbose_name_plural = 'Texts'