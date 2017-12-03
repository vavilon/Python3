from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from myapp.models import UserProfile

def UserList(request):
    users = UserProfile.objects.all()
    paginator = Paginator(user_data, 10) # Shows only 10 records per page

    page = request.GET.get('page')
    try:
        users = paginator.page(page)
    except PageNotAnInteger:
    # If page is not an integer, deliver first page.
        users = paginator.page(1)
    except EmptyPage:
    # If page is out of range (e.g. 7777), deliver last page of results.
        users = paginator.page(paginator.num_pages)

    return render_to_response('user_list.html', {"users": users})
