from django.shortcuts import render
# from .models import ResumeFile, MyRemarkableWork
# from django.http import HttpResponse
from django.core.mail import send_mail

def index(request):
    # works = MyRemarkableWork.objects.all().order_by('-id')
    # context = {
    #     'works': works
    #     'files': ResumeFile.objects.all()
    # }

    return render(request, 'index.html')

def contact(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        subject = request.POST.get('subject')
        message = request.POST.get("message")

        data = {
            'name': name,
            'email': email,
            'subject': subject,
            'message': message
        }
        message = """
        New message: {}

        From: {}
        """.format(data["message"], data["email"])
        send_mail(data["subject"], message, '', ["iabdurahmonov1604@gmail.com"])

        return render(request, 'success.html')

    else:
        return render(request, 'index.html')

# def download(request, path):
#     file_path = os.path.join(settings.MEDIA_ROOT, path)
#     if os.path.exists(file_path):
#         with open(file_path, 'rb') as fh:
#             response=HttpResponse(fh.read(), content_type="application/pdfs")
#             response['Content-Disposition']='inline;filename='+os.path.basename(file_path)
#             return response

#     return Http404

