from django.shortcuts import render,get_object_or_404,redirect,reverse,HttpResponseRedirect
from .models import *
from django.views.generic import DetailView,CreateView
from rest_framework import viewsets,status
from users.models import *
from .serializers import *
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.renderers import TemplateHTMLRenderer
from .forms import *
import random
from django.contrib.auth.decorators import login_required

# Create your views here.

def index(request):
    post = Post.objects.all()
    posts = post[::-1]
    landing = random.randint(0,len(post)-1)
    random_post = posts[landing]

    # print(post[0].country[0].country)

    return render(request, 'post/index.html',{'post':post,'random_post':random_post})



# class PostListView(ListView):
#     model = Post

#     template_name = 'post/index.html'
#     context_object_name = 'posts'


class PostDetailView(DetailView):
    model = Post
    



class PostCreateView(CreateView):
    model = Post
    fields = ('__all__')

    def form_valid(self, form):
        form.instance.account_user= self.request.user
        form.instance.profile_user= Profile.objects.get(id=self.request.user.profile.id)
        

        form.save()


        return redirect('home')


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    authentication_classes = (TokenAuthentication,)

    permission_classes = (IsAuthenticated,)

    
    
    # @action(detail = True,methods=['POST'])
    # def rate_post(self,request,pk=None):
      
    #     user = request.user
    #     post = Post.objects.get(id=pk)
        
    #     rating = Review.objects.get(user=user.id,post=post.id)





class ProfileViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all()

    serializer_class = ProfileSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)


   

 
class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)





def rate(request,pk):
    current_user = request.user
    post = Post.objects.get(pk=pk)
    review = Review.get_reviews(post.id)
    form = ReviewForm(request.POST)
 
    if request.method == 'POST':
        if form.is_valid:
            review = form.save(commit=False)
            review.user = current_user
            review.post = post
            review.post_id = post.id
            review.save()
            return redirect('home')

        else:
            form = ReviewForm()

    return render(request, 'post/review_form.html',{'form':form, 'post':post, 'comments':review})            



@login_required
def search_results(request):
    if 'title' in request.GET and request.GET['title']:
        title = request.GET.get("title")
        searched_user = Post.get_post(title) 
        message = f'No project found for the search term: {title}'
        return render (request,'post/search.html',{"message":message,"post":searched_user})

    else:
        message = "You haven't searched for any name"

    return render(request,'post/search.html',{'message':message})
