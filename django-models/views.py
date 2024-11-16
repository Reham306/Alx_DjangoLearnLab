from django.http import HttpResponse
from django.contrib.auth.decorators import user_passes_test

def role_required(role):
    def decorator(user):
        return user.is_authenticated and hasattr(user, 'userprofile') and user.userprofile.role == role
    return user_passes_test(decorator)

# Admin view
@role_required('Admin')
def admin_view(request):
    return HttpResponse("Welcome to the Admin View!")

# Librarian view
@role_required('Librarian')
def librarian_view(request):
    return HttpResponse("Welcome to the Librarian View!")

# Member view
@role_required('Member')
def member_view(request):
    return HttpResponse("Welcome to the Member View!")
