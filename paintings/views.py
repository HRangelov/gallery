import os

from django.shortcuts import render

# Create your views here.
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.views.generic import ListView

from accounts.decorators import user_required
from paintings.forms import CommentForm, FilterForm
from paintings.forms import PaintingForm
from paintings.models import Painting, Like, Comment

def clean_up_files(path):
    os.remove(path)

def extract_filter_values(params):
    order = params['order'] if 'order' in params else FilterForm.ORDER_ASC
    text = params['text'] if 'text' in params else ''

    return {
        'order': order,
        'text': text,
    }
# def list_painting(request):
#     context = {
#         'paintings': Painting.objects.all(),
#     }
#
#     return render(request, 'painting_list.html', context)

class PaintingsListView(ListView):
    model = Painting
    template_name = 'painting_list.html'
    context_object_name = 'paintings'
    order_by_asc = True
    order_by = 'name'
    contains_text = ''

    def dispatch(self, request, *args, **kwargs):
        params = extract_filter_values(request.GET)
        # self.order_by_asc = params['order'] == FilterForm.ORDER_ASC
        self.order_by = params['order']
        self.contains_text = params['text']
        return super().dispatch(request, *args, **kwargs)

    def get_queryset(self):
        order_by = 'name' if self.order_by == FilterForm.ORDER_ASC else '-name'
        result = self.model.objects.filter(name__icontains=self.contains_text).order_by(order_by)

        return result

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter_form'] = FilterForm(initial={
            'order': self.order_by,
            'text': self.contains_text
        })

        return context


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
            'has_liked': painting.like_set.filter(user_id=request.user.userprofile.id).exists(),
            'can_comment': request.user != painting.user.user,
        }

        return render(request, 'painting_detail3.html', context)
    else:
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = Comment(text=form.cleaned_data['text'], name=form.cleaned_data['name'])
            # comment = Comment(text=form.cleaned_data['text'])
            comment.painting = painting
            comment.user = request.user.userprofile
            comment.save()
            return redirect('painting details or comment', pk)
        context = {
            'painting': painting,
            'form': form,

        }

        return render(request, 'painting_detail3.html', context)


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
            # id_user
            painting = form.save(commit=False)
            painting.user = request.user.userprofile
            painting.save()
            # form.save()
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
