from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from .game import *
import json
# Create your views here.


def home(request):
	return render(request, 'game.html')

@csrf_exempt
def first_random_step(request):
	print('first_random_step.....')

	# Start playing

	# play with human
	p1 = Player("computer", exp_rate=0)
	p1.loadPolicy("policy_p1")

	p2 = HumanPlayer("human")

	st = State(p1, p2)
	action = st.first_random_step()
	print(23333333333, str(action))

	action = convert_postion(str(action))

	return HttpResponse(json.dumps({'action':action}), content_type='application/json')


def convert_postion(position):
	position_dict = {'(1, 1)':4}
	return position_dict[position]
