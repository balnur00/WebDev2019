from django_filters import rest_framework as filters
from api.models import Task


class TaskFilter(filters.FilterSet):
    name = filters.CharFilter(lookup_expr='contains')
    # price = filters.NumberFilter(lookup_expr='exact')
    # min_price = filters.NumberFilter(field_name='price', lookup_expr='gte')
    # max_price = filters.NumberFilter(field_name='price', lookup_expr='lte')

    class Meta:
        model = Task
        fields = ('name')


# from api.serializers import CategorySerializer2, UserSerializer, ProductSerializer
# from rest_framework import generics
# from rest_framework.permissions import IsAuthenticated
# from django.http import Http404
# from django.shortcuts import get_object_or_404
# from django_filters.rest_framework import DjangoFilterBackend
# from rest_framework.filters import SearchFilter, OrderingFilter
# from api.filters import ProductFilter
# from rest_framework.pagination import PageNumberPagination, LimitOffsetPagination
#
#
# class CategoryProductsAPIView(generics.ListCreateAPIView):
#     serializer_class = ProductSerializer
#     pagination_class = LimitOffsetPagination
#     filter_backends = (DjangoFilterBackend, SearchFilter, OrderingFilter)
#     # TODO DjangoFilterBackend
#     # filterset_fields = ('name', 'price',)
#     filter_class = ProductFilter
#
#     # TODO SearchFilter
#     search_fields = ('name', 'price', 'count')
#
#     # TODO OrderingFilter
#     ordering_fields = ('name', 'price')
#     ordering = ('price', )
#
#     def get_queryset(self):
#         # category = get_object_or_404(Category, id=self.kwargs['pk'])
#         try:
#             category = Category.objects.get(id=self.kwargs['pk'])
#         except Category.DoesNotExist:
#             raise Http404
#
#         queryset = category.products.all()
#         # name = self.request.query_params.get('name', None)
#         # if name is not None:
#         #     queryset = queryset.filter(name=name)
#         return queryset

