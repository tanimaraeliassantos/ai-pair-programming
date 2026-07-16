
import ast
import json

from django.http import QueryDict
from django.shortcuts import render
from rest_framework.parsers import BaseParser, FormParser, JSONParser, MultiPartParser
from rest_framework.viewsets import ModelViewSet

from .serializers import ExpenseSerializer
from .models import Expense


class OctetStreamParser(BaseParser):
    media_type = 'application/octet-stream'

    def parse(self, stream, media_type=None, parser_context=None):
        body = stream.read().decode('utf-8')
        if not body:
            return {}

        try:
            return json.loads(body)
        except json.JSONDecodeError:
            try:
                data = ast.literal_eval(body)
            except (ValueError, SyntaxError):
                return QueryDict(body, mutable=True)

            if isinstance(data, dict):
                return data
            return QueryDict(body, mutable=True)


def index(request):
    return render(request, 'index.html')


class ExpenseViewSet(ModelViewSet):
    queryset = Expense.objects.all()
    serializer_class = ExpenseSerializer
    parser_classes = (JSONParser, FormParser,
                      MultiPartParser, OctetStreamParser)
