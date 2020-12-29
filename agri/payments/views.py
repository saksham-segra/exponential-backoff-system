import uuid
from django.http import JsonResponse
from rest_framework.views import APIView
from .tasks import update_payment_status


class PaymentView(APIView):

    def post(self, request, *args, **kwargs):
        # do some business logic
        payment_uuid = uuid.uuid4()
        update_payment_status.delay(payment_uuid)

        return JsonResponse({"status": "SUCCESS"})
