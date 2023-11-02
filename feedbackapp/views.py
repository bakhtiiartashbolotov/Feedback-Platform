import string
from django.http import HttpRequest, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import get_object_or_404, redirect, render
from .forms import CommentForm, FeedbackForm
from .models import Comment, Feedback

def all_feedbacks(request: HttpRequest):
    context = {
        'feedbacks': Feedback.objects.all()
    }
    return render(request, 'main.html', context=context)

def feedback_by_id(request, id):
    feedback = Feedback.objects.get(id=id)
    comments = Comment.objects.filter(feedback=feedback)
    
    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.feedback = feedback
            comment.save()
            comment_form = CommentForm()
    else:
        comment_form = CommentForm()

    context = {
        'id': id,
        'feedback': feedback,
        'comments': comments,
        'comment_form': comment_form,
    }
    return render(request, 'feedbacks.html', context=context)

@csrf_exempt
def create_feedback(request: HttpRequest):
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('main')
    else:
        form = FeedbackForm()

    context = {'form': form}
    return render(request, 'feedback_form.html', context)

@csrf_exempt
def delete_feedback(request, id):
    feedback = Feedback.objects.get(id=id)
    if(request.method == 'POST'):
        feedback.delete()
        return redirect('main')
    context = {'feedback':feedback}
    return render(request, 'delete_feedback.html')

@csrf_exempt
def update_feedback(request:HttpRequest, id:string):
    feedback = Feedback.objects.get(id=id)
    print(feedback)
    form = FeedbackForm(instance=feedback)
    if(request.method == 'POST'):
        form = FeedbackForm(data=request.POST, instance=feedback)
        form.save()
        return redirect('main')
    
    context = {'form':form,}
    return render(request, "feedback_form.html", context)

def delete_comment(request, comment_id):
    comment = Comment.objects.get(id=comment_id)

    if request.method == 'POST':
        comment.delete()
        return redirect('feedback_by_id', id=comment.feedback.id)

    context = {
        'comment': comment
    }
    return render(request, 'delete_comment.html', context)