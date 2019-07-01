from .models import interns, not_interns
from django.http import HttpResponse, Http404, JsonResponse
from .narnia import Magic
import requests

	
def meeting(request):

try:

	kirill_status = request.POST.get('status')
	kirill = not_interns.objects.get(name="kirill")
	interns = interns.objects.all()
	intern_data = []

	if kirill_status == True:

		for intern in interns:

			int_status = intern.getstatus(intern.id)

			if int_status == True:

				start_time = time.time()
				intern.talk(intern.name)
				question = kirill.genereate_question()
				intern_answer = intern.generate_answer(question)
				earned_points = kirill.validate_answer(question, intern_answer)
				presentation_time = time.time() - start_time

				if presentation_time > 300:
					earned_points = earned_points - 10
					kirill.give_angry_look_to(intern.name)

				if earned_points < 0:
					earned_points = 0

			else:
				earned_points = 0
				kirill.be_dissapointed()

			five_min  = {
			'InternName' : intern.name,
			'EarnedPoints' : earned_points,
			}

			intern_data.append(five_min)

	meeting_data = {
		'MeetingStatus' : 'Meeting did not happen!',
		'InternData' : intern_data,
	}

	else: 

		meeting_data = {'MeetingStatus' : 'Meeting was ruined!'}


	return JsonResponse(meeting_data)

except:

	raise Http404("Meeting error 404")