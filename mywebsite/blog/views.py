from django.shortcuts import render

# Create your views here.
def index(req):
    context = {
        
    }
    
    return render(req, "index.html", context=context)

def about_me(request):
    award_image = AwardImageUpload.objects.all()
    
    return render(
        request,
        'single_pages/about_me.html',
        {
            award_image: award_image
        }
    )
    
    