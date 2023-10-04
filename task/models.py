from django.db import models

# Create your models here.
class Products(models.Model):
    owner = models.CharField(max_length=255)

class Lessons(models.Model):
    name = models.CharField(max_length=255)
    lessonURL = models.CharField(max_length=2000)
    duration = models.IntegerField()

class Users(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class ProductUserAccess(models.Model):
    userId = models.ForeignKey("Users", on_delete=models.PROTECT)
    productId = models.ForeignKey("Products", on_delete=models.PROTECT)

class LessonInProduct(models.Model):
    lessonId = models.ForeignKey("Lessons", on_delete=models.PROTECT)
    productId = models.ForeignKey("Products", on_delete=models.PROTECT)

class LessonStatus(models.Model):
    LESSON_STATUS = [
        ("V", "Просмотренно"),
        ("N", "Не просмотренно"),
    ]

    userId = models.ForeignKey("Users", on_delete=models.PROTECT)
    productId = models.ForeignKey("Products", on_delete=models.PROTECT)
    lessonId = models.ForeignKey("Lessons", on_delete=models.PROTECT)
    durationViewed = models.IntegerField(default=0)
    status = models.CharField(
        max_length=1,
        choices=LESSON_STATUS,
        default="N",
    )
    lastViewed = models.DateTimeField(null=True)

    def __str__(self):
        return f'{self.userId.id} {self.lessonId.id} {self.durationViewed} {self.status}'

    def save(self, *args, **kwargs):
        if (self.durationViewed / Lessons.objects.get(pk=self.lessonId.id).duration) >= 0.8:
            self.status = "V"

        super().save(*args, **kwargs)
