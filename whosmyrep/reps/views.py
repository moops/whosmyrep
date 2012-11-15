from django.shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.template import RequestContext
from whosmyrep.reps.models import Rep, Rank

def index(request):
	reps = Rep.objects.all().order_by('last_name')[:20]
	return render_to_response('index.html', {'reps': reps})

def detail(request, rep_id):
	r = get_object_or_404(Rep, id=rep_id)
	return render_to_response('detail.html', {'rep': r}, context_instance=RequestContext(request))

def rank(request, rep_id):
	print('rep_id: ' + rep_id)
	r = get_object_or_404(Rep, id=rep_id)
	print('rep_id: ' + str(r.id))
	if request.user.is_authenticated():
		rank = Rank(rep=r, rank=request.POST['rank'], user=request.user)
	rank.save()
	r.avg_rank = request.POST['rank']
	r.save()
	return HttpResponseRedirect(reverse('whosmyrep.reps.views.index'))