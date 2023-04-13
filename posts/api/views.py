from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from posts.models import Post
import datetime
from posts.api.serializers import PostSerializer


class PostApiView(APIView):
    def get(self, request):
        posts = PostSerializer(Post.objects.all(), many=True)
        return Response(status=status.HTTP_200_OK, data=posts.data)
    

    def post(self, request):
        posts = PostSerializer(data=request.POST)
        posts.is_valid(raise_exception=True)
        posts.save()
        return Response(status=status.HTTP_200_OK, data=posts.data)





"""
#Esta es la opcion cruda sin serializador
#def get(self, request):
#posts = Post.objects.all()
#posts = [post.title for post in Post.objects.all()]
#return Response(status=status.HTTP_200_OK, data=posts)
    


#def post(self, request):
#Post.objects.create(title=request.POST['title'], 
#description=request.POST['description'], 
#order=request.POST['order'])
#return self.get(request)
"""



