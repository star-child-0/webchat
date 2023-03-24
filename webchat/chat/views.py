from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from chat.models import Message
from django.http import JsonResponse

MEDIA_URL = '/media/'


@login_required
def rooms(request):
	return render(request, "chat/index.html")


@login_required
def room(request, room_name):
	context_dict = {}

	context_dict['room_name'] = room_name
	return render(request, "chat/room.html", context_dict)


@login_required
def chat(request):
	context_dict = {}

	messages = Message.objects.all()
	msgs = []
	for m in messages:
		msgs.append(m.as_dict())

	context_dict['messages'] = msgs
	context_dict['MEDIA_URL'] = MEDIA_URL
	return render(request, "chat/chat.html", context_dict)


@login_required
def ajax_send_message(request):
	data = {}
	if request.method == 'POST':
		postdata = request.POST
		text = postdata.get("message")
		has_file = int(postdata.get("has_file"))

		try:
			message = Message()

			message.text = text
			message.author = request.user
			if has_file:
				message.file = request.FILES["file"]

			message.save()
			data['filename'] = message.file.name
			data['result'] = 0
		except:
			data['result'] = -1
	return JsonResponse(data)
