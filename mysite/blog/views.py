from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Publicacion

def post_list(request):
    posts = Publicacion.objects.filter(fecha_publicacion__lte=timezone.now()).order_by('fecha_publicacion')
    return render(request, 'blog/post_list.html', {'posts': posts})


def detalle_pub(request,pk):
    post = get_object_or_404(Publicacion, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})
