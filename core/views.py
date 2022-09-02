from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from accounts.models import User


def home(request):
	if 'username' in request.session:
		usuario = request.session['username']
	else:
                #current_user=request.user.iduser
		usuario = ''
	return render (request, 'core/home.html', { 'usuario': usuario })
