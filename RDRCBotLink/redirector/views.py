from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseBadRequest
from .models import utmBase, LinkBase # Импортируйте ваши модели
from urllib.parse import urlparse, parse_qs , urlencode
import uuid
def get_link(request, id):
    """
    View функция, которая считывает UTM-метки и редиректит по ссылке.
    """
    try:
        linkbase_instance = get_object_or_404(LinkBase, pk=id)
    except Exception as e:
        return HttpResponseBadRequest(f"Ошибка при получении ссылки: {e}")

    utm_str = urlencode(request.GET, doseq=True)
    if utm_str:

        utm_instance, created = utmBase.objects.get_or_create(unicKye=uuid.uuid4().hex[:8])  # Используем id ссылки как уникальный ключ
        utm_instance.utms = utm_str
        utm_instance.save()  # добавляем ссылку к utmBase
        utm_instance.linkbase.add(linkbase_instance)



    return redirect(f"{linkbase_instance.getlink}?start={utm_instance.unicKye}")


def get_urls(request):
    """
    Представление, перенаправляющее пользователя по unicKey.
    """
    try:
        utm_instance = utmBase.objects.get(unicKye=request.GET.get('key'))
        links = utm_instance.linkbase.all()
    except utmBase.DoesNotExist:
        return HttpResponseNotFound("Ссылка не найдена")
    return  redirect(f'{links.first().postLink}?{utm_instance.utms}')