from django.shortcuts import render

# Create your views here.

posts = [
            {'id':1, 'title': 'First post', 'content': " First content.Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. "},
            {'id':2, 'title': 'Second post', 'content': "Second content. simply dummy text established fact that a reader will be distracted by the readable content of a page when looking at its layout. The point of using Lorem Ipsum is that it has a more-or-less normal distribution of letters, as opposed to using 'Content here, content here', making it look like readable English. "},
            {'id':3, 'title': 'Third post', 'content': "Third content. Contrary to popular belief, Lorem Ipsum is not simply random text. It has roots in a piece of classical Latin literature from 45 BC, making it over 2000 years old. Richard McClintock, a Latin professor at Hampden-Sydney College in Virginia, looked up one of the more obscure Latin words, consectetur, from a Lorem Ipsum passage, and going through the cites of the word in classical literature, discovered the undoubtable source."}
        ]


def home_view(request):

    return render(request, 'home.html')


def posts_view(request):


    context = {
        'posts': posts
    }

    return render(request,'posts.html',context)

def post_detail_view(request, id):
    post_filter = filter(lambda x: x['id']==id, posts)
    post = list(post_filter)[0]

    context = {
        'post': post
    }

    return render(request,'post_detail.html', context)
