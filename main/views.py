from rest_framework.views import APIView
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST, HTTP_404_NOT_FOUND
from .models import Category, Product
from .serializers import ( CategorySerializer, AdminCategorySerializer,
    ProductSerializer, AdminProductSerializer )


class CategoriesApiView(APIView):
    def get(self, request: Request) -> Response:
        object_list = Category.objects.all()
        serializer = CategorySerializer(object_list, many=True)

        return Response({
            'status': 'ok',
            'code': 200,
            'results': serializer.data
        }, status=HTTP_200_OK)


class AdminCategoriesApiView(APIView):
    def get(self, request: Request, guid=None) -> Response:
        object_list = Category.objects.all()
        if guid:
            try:
                object_ = object_list.get(guid=guid)
                serializer = AdminCategorySerializer(object_)
            except:
                return Response({
                    'status': 'error',
                    'code': 404,
                    'errors': ["Not found"]
                }, status=HTTP_404_NOT_FOUND)
        else:
            serializer = AdminCategorySerializer(object_list, many=True)

        return Response({
            'status': 'ok',
            'code': 200,
            'results': serializer.data
        }, status=HTTP_200_OK)

    def post(self, request: Request) -> Response:
        serializer = AdminCategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()

            return Response({
                'status': 'ok',
                'code': 200,
                'results': serializer.data
            }, status=HTTP_200_OK)

        return Response({
            'status': 'error',
            'code': 400,
            'errors': serializer.errors
        }, status=HTTP_400_BAD_REQUEST)

    def put(self, request: Request, guid=None) -> Response:
        if guid:
            try:
                object_ = Category.objects.get(guid=guid)
                serializer = AdminCategorySerializer(data=request.data, instance=object_)

                if serializer.is_valid():
                    serializer.save()

                    return Response({
                        'status': 'ok',
                        'code': 200,
                        'results': serializer.data
                    })

                return Response({
                    'status': 'error',
                    'code': 400,
                    'errors': serializer.errors
                }, status=HTTP_400_BAD_REQUEST)
            except:
                return Response({
                    'status': 'error',
                    'code': 404,
                    'errors': ["Not found"]
                }, status=HTTP_404_NOT_FOUND)

        return Response({
            'status': 'error',
            'code': 200,
            'errors': ["No object is shown"]
        }, status=HTTP_400_BAD_REQUEST)
