from django.shortcuts import render, get_object_or_404, redirect
from .forms import ImageForm, ToggleFavoriteForm
from .models import Image
from django.urls import reverse

def home(request):
    if request.method == "POST":
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    form = ImageForm()
    img = Image.objects.all()
    return render(request, 'app/home.html', {'img': img, 'form': form})

def toggle_favorite(request, pk):
    obj = get_object_or_404(Image, pk=pk)

    if request.method == 'POST':
        form = ToggleFavoriteForm(request.POST)
        if form.is_valid():
            obj.is_favorite = not obj.is_favorite
            obj.save()
            referer = request.META.get('HTTP_REFERER')

            return redirect(referer) if referer else redirect('home')
    else:
        form = ToggleFavoriteForm()

    return render(request, 'toggle_favorite.html', {'form': form})

def favorites(request):
    favorite_images = Image.objects.filter(is_favorite=True)
    print("Favorite Images:", favorite_images)
    return render(request, 'favorites.html', {'favImg': favorite_images})