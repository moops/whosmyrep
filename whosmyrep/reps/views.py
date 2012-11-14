from django.shortcuts import render_to_response, get_object_or_404
from django.http import Http404
from whosmyrep.reps.models import Rep

def index(request):
	reps = Rep.objects.all().order_by('last_name')[:20]
	return render_to_response('index.html', {'reps': reps})

def detail(request, rep_id):
	r = get_object_or_404(Rep, id=rep_id)
	return render_to_response('detail.html', {'rep': r})