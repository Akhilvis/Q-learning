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
	winner = None
	# Start playing

	# play with human
	p1 = Player("computer", exp_rate=0)
	p1.loadPolicy("policy_p1")

	p2 = HumanPlayer("human")

	st = State(p1, p2)
	action = st.policy_move()

	action = convert_postion_int(str(action))

	return HttpResponse(json.dumps({'action':action}), content_type='application/json')


@csrf_exempt
def take_policy_step(request):

	data = json.loads(request.body)
	position = data['position']
	if not data['source']:
		source = 1
	else:
		source = -1


	p1 = Player("computer", exp_rate=0)
	p1.loadPolicy("policy_p1")

	p2 = HumanPlayer("human")


	st = State(p1, p2)
	st.board = load_board()
	print('board>>>>>>>>>>>>>>>>>>>>>>>>.', st.board)
	# st.update_board_from_request(int(position),source)
	st.update_board_from_request(convert_postion_tuple(position), source)

	action = st.policy_move()
	if st.winner() is None:
		is_end =  False
	else:
		is_end = True
		winner =st.winner()

	action = convert_postion_int(str(action))

	return HttpResponse(json.dumps({'action':action, 'is_end':is_end,'winner':winner}), content_type='application/json')



def convert_postion_int(position):
	position_dict = {'(0, 0)':0,'(0, 1)':1,'(0, 2)':2,'(1, 0)':3,'(1, 1)':4,'(1, 2)':5,
						'(2, 0)':6,'(2, 1)':7,'(2, 2)':8}
	return position_dict[position]

def convert_postion_tuple(position):
	position_dict = {'0':(0,0),'1':(0,1),'2':(0,2),'3':(1,0),'4':(1,1),'5':(1,2),
						'6':(2,0),'7':(2,1),'8':(2,2)}
	return position_dict[str(position)]

def load_board():
	current_board = np.loadtxt('board.txt', dtype=int)
	return current_board
    