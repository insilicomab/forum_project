from django.shortcuts import render, redirect, get_object_or_404
from django.shortcuts import render
from . import forms
from django.contrib import messages



'''
掲示板投稿
'''

def create_theme(request):
    create_theme_form = forms.CreateThemeForm(request.POST or None)
    if create_theme_form.is_valid():
        create_theme_form.instance.user = request.user # 現在、ログインしているユーザーを取得して、ForeignKeyのユーザーにわたす
        create_theme_form.save()
        messages.success(request, '掲示板を作成しました。')
        return redirect('accounts:home')
    return render(
        request, 'boards/create_theme.html', context={
            'create_theme_form': create_theme_form,
        }
    )

'''
投稿一覧表示
'''

def list_themes(request):
    themes = Themes.objects.fetch_all_themes()
    return render(
        request, 'boards/list_themes.html', context={
            'themes': themes
        }
    )