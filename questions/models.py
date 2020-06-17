from django.db import models


class QestionCategory(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Question(models.Model):
    category = models.ForeignKey(QestionCategory,
                                 on_delete=models.CASCADE,
                                 null=True,
                                 related_name='questions')
    question_text = models.TextField()
    published = models.BooleanField(default=False)

    def __str__(self):
        return self.question_text
