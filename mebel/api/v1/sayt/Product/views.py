from rest_framework.exceptions import NotFound
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response

from api.v1.sayt.Product.serialazer import ProductSerializer
from api.v1.sayt.Product.services import format_pro, paginated_ctg
from sayt.models import Product


class ProductView(GenericAPIView):
    serializer_class = ProductSerializer

    def get_object(self, pk=None):
        try:
            root = Product.objects.get(pk=pk)
        except:
            raise NotFound(f"{pk} idsidagi product yo'q!")
        return root

    def get(self, requests, pk=None, *args, **kwargs):

        if pk:
            pro = Product.objects.filter(pk=pk).first()
            if not pro:
                result = {"Error": "Bunday product yo'q!"}
            else:
                result = format_pro(pro)
        else:
            # result = []
            # for x in Product.objects.all():
            #     result.append(format_pro(x))
            result = paginated_ctg(requests)
        return Response(result)

    def post(self, requests, *args, **kwargs):
        data = requests.data
        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        result = serializer.create(serializer.data)

        return Response(format_pro(result))

    def put(self, requests, pk, *args, **kwargs):
        data = requests.data
        root = self.get_object(pk)
        serializer = self.get_serializer(data=data, partial=True, instance=root)
        serializer.is_valid(raise_exception=True)
        result = serializer.save()

        return Response(format_pro(result))

    def delete(self, requests, pk, *args, **kwargs):
        pro = Product.objects.filter(pk=pk).first()
        if not pro:
            result = {"Error": "Bunday product yo'q!"}
        else:
            pro.delete()
            result = {"Success": f"{pro.content} o'chirib tashlandi!"}
        return Response(result)
