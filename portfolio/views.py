from django.shortcuts import render
# from .models import ResumeFile, MyRemarkableWork
# from django.http import HttpResponse


def index(request):
    # works = MyRemarkableWork.objects.all().order_by('-id')
    # context = {
    #     'works': works
    #     'files': ResumeFile.objects.all()
    # }

    return render(request, 'index.html')


# def download(request, path):
#     file_path = os.path.join(settings.MEDIA_ROOT, path)
#     if os.path.exists(file_path):
#         with open(file_path, 'rb') as fh:
#             response=HttpResponse(fh.read(), content_type="application/pdfs")
#             response['Content-Disposition']='inline;filename='+os.path.basename(file_path)
#             return response

#     return Http404

