import os

from django.shortcuts import render

# Create your views here.
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from accounts.decorators import user_required
from paintings.forms import CommentForm
from paintings.forms import PaintingForm
from paintings.models import Painting, Like, Comment

def clean_up_files(path):
    os.remove(path)

def list_painting(request):
    context = {
        'paintings': Painting.objects.all(),
    }

    return render(request, 'painting_list.html', context)


@login_required
def details_or_comment_painting(request, pk):
    painting = Painting.objects.get(pk=pk)
    if request.method == 'GET':
        context = {
            'painting': painting,
            'form': CommentForm(),
            'can_delete': request.user == painting.user.user,
            'can_edit': request.user == painting.user.user,
            'can_like': request.user != painting.user.user,
            'has_liked': painting.like_set.filter(id=request.user.userprofile.id).exists(),
            'can_comment': request.user != painting.user.user,
        }

        return render(request, 'painting_detail.html', context)
    else:
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = Comment(text=form.cleaned_data['text'])
            comment.painting = painting
            comment.user = request.user.userprofile
            comment.save()
            return redirect('painting details or comment', pk)
        context = {
            'painting': painting,
            'form': form,
        }

        return render(request, 'painting_detail.html', context)


def persist_painting(request, painting, template_name):
    if request.method == 'GET':
        form = PaintingForm(instance=painting)

        context = {
            'form': form,
            'painting': painting,
        }

        return render(request, f'{template_name}.html', context)
    else:
        old_image = painting.image
        form = PaintingForm(
            request.POST,
            request.FILES,
            instance=painting
        )
        if form.is_valid():
            if old_image:
                clean_up_files(old_image.path)
            form.save()
            Like.objects.filter(painting_id=painting.id) \
                .delete()
            return redirect('painting details or comment', painting.pk)

        context = {
            'form': form,
            'painting': painting,
        }

        return render(request, f'{template_name}.html', context)


@user_required(Painting)
def edit_painting(request, pk):
    painting = Painting.objects.get(pk=pk)
    return persist_painting(request, painting, 'painting_edit')


@login_required
def create_painting(request):
    painting = Painting()
    return persist_painting(request, painting, 'painting_create')


@login_required
def delete_painting(request, pk):
    painting = Painting.objects.get(pk=pk)
    if painting.user.user != request.user:
        # forbid
        pass
    if request.method == 'GET':
        context = {
            'painting': painting,
        }

        return render(request, 'painting_delete.html', context)
    else:
        painting.delete()
        return redirect('list paintings')


@login_required
def like_painting(request, pk):
    like = Like.objects.filter(user_id=request.user.userprofile.id, painting_id=pk).first()

    if like:
        like.delete()
    else:
        painting = Painting.objects.get(pk=pk)
        like = Like(test=str(pk), user=request.user.userprofile)
        like.painting = painting
        like.save()
    return redirect('painting details or comment', pk)
