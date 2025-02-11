from django.shortcuts import render

def handler404(request, exception):
    return render(request, 'error_page.html', {
        'status_code': 404,
        'message': "Page Not Found"
    }, status=404)
