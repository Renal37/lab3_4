import random
from django.views.decorators.csrf import csrf_exempt
from django.http import  JsonResponse
from django.shortcuts import render
from .models import CatImage

def cats_view(request):
    images = CatImage.objects.all()
    return render(request, 'cats/index.html', {'images': images})

@csrf_exempt
def random_cat_image(request):
    cat_images = CatImage.objects.all()
    if cat_images.exists():
        random_image = random.choice(cat_images)
        return JsonResponse({'source': random_image.image.url})
    else:
        return JsonResponse({'error': 'Не найдено ошибок'}, status=404)

def random_cat_images(request, num):
    cat_images = CatImage.objects.all()
    if cat_images.exists():
        random_images = random.sample(list(cat_images), min(num, len(cat_images)))
        sources = [image.image.url for image in random_images]
        return JsonResponse({'source': sources}, safe=False)
    else:
        return JsonResponse({'error': 'Не найдено ошибок'}, status=404)