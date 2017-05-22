from rest_framework.viewsets import GenericViewSet
from django.contrib.auth.models import User
from custom_user.serializers import UserProfileSerializer
from rest_framework import mixins, status
from django.http import HttpResponse
import csv
from rest_framework.response import Response



class UserViewSet(mixins.CreateModelMixin,
                   mixins.ListModelMixin,
                   mixins.RetrieveModelMixin,
                   mixins.UpdateModelMixin,
                   mixins.DestroyModelMixin,
                   GenericViewSet):

    queryset = User.objects.all()
    serializer_class = UserProfileSerializer


    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())

        if self.request.query_params.get('xls'):
            response = HttpResponse(content_type='text/csv')
            response['Content-Disposition'] = 'attachment; filename="report.csv"'

            writer = csv.writer(response)
            writer.writerow(["Username", "Birthday", "Eligible", "Random Number", "BizzFuzz"])
            for r in queryset.all():
                writer.writerow([r['username'],
                                 r['birthday'],
                                 r['eligible'],
                                 r['random'],
                                 r['bizzfuzz']])

            return response

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

