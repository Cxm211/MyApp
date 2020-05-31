from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from .models import articleInfo
from article.serializers import articleSerializer, contentSerializer, commentSerializer


# Create your views here.
@csrf_exempt
def article_list(request):
    if request.method == 'GET':
        articleLs = articleInfo.objects.all()
        serializer = articleSerializer(articleLs, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = articleSerializer(data=data)

        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


@csrf_exempt
def article_content(request, id):
    try:
        article = articleInfo.objects.get(pk=id)
    except articleInfo.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = contentSerializer(article)
        return JsonResponse(serializer.data, safe=False)
    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = contentSerializer(article, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)


def article_comment(request, id):
    try:
        article = articleInfo.objects.get(pk=id)
    except articleInfo.DoesNotExist:
        return HttpResponse(status=404)
    if request.method == 'GET':
        serializer = commentSerializer(article)
        return JsonResponse(serializer.data, safe=False)
    pass
