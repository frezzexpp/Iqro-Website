from rest_framework import mixins, status
from drf_spectacular.utils import extend_schema_view, extend_schema
from rest_framework.filters import SearchFilter
from rest_framework.pagination import PageNumberPagination
from rest_framework.viewsets import GenericViewSet
from .serializers import *
import telebot
from config import settings


def send_telegram_message(message):
    bot = telebot.TeleBot(settings.TELEGRAM_BOT_TOKEN)
    try:
        bot.send_message(
            chat_id=settings.TELEGRAM_CHANNEL_ID,
            text=message,
            parse_mode=None  # Yoki 'Markdown'/'HTML' bo'lishi mumkin
        )
    except telebot.apihelper.ApiTelegramException as e:
        print(f"Telegram Error: {e}")

# Contact Pagination:
class ContactPagination(PageNumberPagination):
    page_size = 100
    page_size_query_param = 'page_size'
    max_page_size = 10000



# Contact CRUD:
@extend_schema_view(
    list=extend_schema(summary='list contact project', tags=['Contact']),
    retrieve=extend_schema(summary='retrieve contact project', tags=['Contact']),
    create=extend_schema(summary='create contact project', tags=['Contact']),
    destroy=extend_schema(summary='destroy contact project', tags=['Contact']
))
class CRUDContact(mixins.CreateModelMixin,
                   mixins.RetrieveModelMixin,
                   mixins.DestroyModelMixin,
                   mixins.ListModelMixin,
                   GenericViewSet):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializers
    pagination_class = ContactPagination
    filter_backends = [SearchFilter]
    search_fields = ['first_name', 'phone']

    def perform_create(self, serializer):
        instance = serializer.save()
        data = instance.create_at
        date = str(data)[0:10]
        time = str(data)[11:19]
        message = (
            f"Contact ({date}/{time}): \n"
            f"Name: {getattr(instance, 'name', 'N/A')}\n"
            f"Phone: {getattr(instance, 'phone', 'N/A')}\n"
            f"Email: {getattr(instance, 'email', 'N/A')}\n"
            f"Message: {getattr(instance, 'message', 'N/A')}"
        )
        send_telegram_message(message)