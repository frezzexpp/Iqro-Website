import requests
from io import BytesIO
from PIL import Image, UnidentifiedImageError
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from drf_spectacular.utils import extend_schema, OpenApiParameter


class ImageProxyView(APIView):
    @extend_schema(
        parameters=[
            OpenApiParameter(name='url', description='URL of the image', required=True, type=str),
            OpenApiParameter(name='width', description='Desired width of the image', required=False, type=int),
            OpenApiParameter(name='height', description='Desired height of the image', required=False, type=int),
        ],
        responses={200: 'image/jpeg'}
    )
    def get(self, request, *args, **kwargs):
        image_url = request.query_params.get('url')
        width = request.query_params.get('width')
        height = request.query_params.get('height')

        if not image_url:
            return Response({"error": "URL parameter is required"}, status=status.HTTP_400_BAD_REQUEST)

        try:
            response = requests.get(image_url)
            response.raise_for_status()
        except requests.exceptions.RequestException as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

        try:
            image = Image.open(BytesIO(response.content))

            if width and height:
                width = int(width)
                height = int(height)
                image = image.resize((width, height), Image.Resampling.LANCZOS)
            elif width:
                width = int(width)
                ratio = width / image.width
                height = int(image.height * ratio)
                image = image.resize((width, height), Image.Resampling.LANCZOS)
            elif height:
                height = int(height)
                ratio = height / image.height
                width = int(image.width * ratio)
                image = image.resize((width, height), Image.Resampling.LANCZOS)

            buffer = BytesIO()
            format = image.format if image.format else 'JPEG'
            image.save(buffer, format='PNG')
            buffer.seek(0)

            return HttpResponse(buffer.getvalue(), content_type=response.headers.get('Content-Type', f'image/{format.lower()}'))

        except UnidentifiedImageError:
            return Response({"error": "Failed to identify image format"}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"error": "Failed to process the image: " + str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)