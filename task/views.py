from rest_framework import viewsets
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import action
from .models import *
from .serializers import *

# Create your views here.

class UsersViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = UserSerializer

    def get_queryset(self):
        pk = self.kwargs.get("pk")

        if not pk:
            return Users.objects.all()

        return Users.objects.filter(pk=pk)

    def getLesson(self, productId, lessonId, userId):
        info = LessonStatus.objects.get(userId=userId, productId=productId, lessonId=lessonId)

        return {'duration': info.durationViewed, 'status': info.status}

    @action(methods=['get'], detail=True)
    def stats(self, request, pk=None):
        product = ProductUserAccess.objects.filter(userId=pk)

        return Response({"product": {
                pr.productId.id: {
                        ls.lessonId.id: self.getLesson(pr.productId.id, ls.lessonId.id, pk)
                        for ls in LessonInProduct.objects.filter(productId=pr.productId.id)
                } for pr in product
        }})

class UserProductViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Users.objects.all()
    serializer_class = UserSerializer
    lookup_field = 'pk'

    def get_lessons_for_product(self, request, user_id, product_id):
        try:
            user = Users.objects.get(pk=user_id)
            product = Products.objects.get(pk=product_id)
        except Users.DoesNotExist or Products.DoesNotExist:
            return Response({'error': 'User or Product does not exist'}, status=status.HTTP_404_NOT_FOUND)

        lessons = LessonStatus.objects.filter(userId=user_id, productId=product_id)
        serializer = LessonSerializer(lessons, many=True)
        return Response(serializer.data)

class ProductdStatisticsViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Products.objects.all()
    serializer_class = ProductStatisticsSerializer

    def list(self, request):
        productStatistics = []
        usersCount = Users.objects.count()

        for product in self.queryset:
            productId = product.id
            totalLessonsViewed = LessonStatus.objects.filter(productId=productId).count()
            totalDurationViewed = LessonStatus.objects.filter(productId=productId).aggregate(total_duration=models.Sum("durationViewed"))["total_duration"]
            studentsCount = ProductUserAccess.objects.filter(productId=productId).count()
            perByProduct = (studentsCount / usersCount) * 100 if usersCount > 0 else 0

            data = {
                "product_id" : productId,
                "total_lesson_viewed" : totalLessonsViewed,
                "total_duration_viewed" : totalDurationViewed,
                "students_count" : studentsCount,
                'percent_buy_product' : perByProduct
            }

            productStatistics.append(data)

        return Response(productStatistics)
