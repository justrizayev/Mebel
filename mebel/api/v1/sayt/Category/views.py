from rest_framework.authtoken.models import Token
from rest_framework.exceptions import NotFound
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication

from rest_framework.permissions import AllowAny, IsAuthenticated
from api.v1.sayt.Category.services import format_ctg, paginated_ctg
from base.helper import BearerToken
from dashboard.models import User
from sayt.models import Category

from .serialazer import CategorySerializer, UserSerializer


class CategoryView(GenericAPIView):
    serializer_class = CategorySerializer
    permission_classes = (IsAuthenticated, )
    authentication_classes = (BearerToken, )

    def get_object(self, pk=None):
        try:
            root = Category.objects.get(pk=pk)
        except:
            raise NotFound(f"{pk} idsidagi kategoriya yo'q!")
        return root

    def get(self, requests, pk=None, *args, **kwargs):
        if pk:
            ctg = Category.objects.filter(pk=pk).first()
            if not ctg:
                result = {"Error": "Bunday categoriya yo'q!"}
            else:
                result = format_ctg(ctg)
        else:
            # result = []
            # for x in Category.objects.all():
            #     result.append(format_ctg(x))
            result = paginated_ctg(requests)

        return Response(result)

    def post(self, requests, *args, **kwargs):
        data = requests.data
        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        result = serializer.create(serializer.data)

        return Response(format_ctg(result))


