from .models import *

class CreateBD:
    def __init__(self):
        ProductUserAccess.objects.create(userId_id=1, productId_id=1)
        ProductUserAccess.objects.create(userId_id=1, productId_id=2)
        ProductUserAccess.objects.create(userId_id=1, productId_id=3)

        ProductUserAccess.objects.create(userId_id=2, productId_id=3)

        ProductUserAccess.objects.create(userId_id=3, productId_id=1)
        ProductUserAccess.objects.create(userId_id=3, productId_id=2)

        for lessons in LessonInProduct.objects.filter(productId=1):
            LessonStatus(userId_id=1, productId_id=1, lessonId_id=lessons.lessonId.id).save()
            LessonStatus(userId_id=3, productId_id=1, lessonId_id=lessons.lessonId.id).save()

        for lessons in LessonInProduct.objects.filter(productId=2):
            LessonStatus(userId_id=1, productId_id=2, lessonId_id=lessons.lessonId.id).save()
            LessonStatus(userId_id=3, productId_id=2, lessonId_id=lessons.lessonId.id).save()

        for lessons in LessonInProduct.objects.filter(productId=3):
            LessonStatus(userId_id=2, productId_id=3, lessonId_id=lessons.lessonId.id).save()
