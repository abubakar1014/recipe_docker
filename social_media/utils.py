import re
from django.db import models
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework import status
from rest_framework.exceptions import APIException
from django.utils.translation import gettext_lazy as _

class TimeStamped(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True, null=True)

    class Meta:
        abstract = True
        

class LowercaseEmailField(models.EmailField):
    def to_python(self, value):
        value = super(LowercaseEmailField, self).to_python(value)
        if isinstance(value, str):
            return value.lower()
        return value


class CustomPagination(PageNumberPagination):
    page_size = 50
    page_size_query_param = 'limit'
    max_page_size = 250

    def get_paginated_response(self, data):
        response = Response(
            {
                'count': self.page.paginator.count,
                'next': self.get_next_link(),
                'previous': self.get_previous_link(),
                'num_pages': self.page.paginator.num_pages,
                'results': data
            }
        )
        return response
    
def validate_password(password):
    password_pattern = "^(?=.*?[A-Z])(?=.*?[a-z])(?=.*?[0-9])(?=.*?[#?!@$%^&*-]).{8,}$"
    return re.match(password_pattern, password)

def serializer_errors(serializer):
    try:
        fields = list(serializer.errors.keys())
        data = [x + ": " + serializer.errors[x][0] for x in fields]
        data = "\n".join(data)
        return data
    except:
        return serializer.errors
    



class InvalidException(APIException):
    status_code = status.HTTP_406_NOT_ACCEPTABLE
    default_detail = _('Error Occurs.')
    default_code = 'error'
