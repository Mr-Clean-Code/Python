from sys import exit
from random import randint


class Scene(object):

	def enter(self):
		print "This scene is not yet configured. Subclass it and implement enter"
		exit(1)

class Engine(object):

	def __init__(self, scene_map):
		self.scene_map = scene_map

	def play(self):
		current_scene = self.scene_map.opening_scene()

		while True:
			print "\n---------"
			next_scene_name = current_scene.enter()
			current_scene = self.scene_map.next_scene(next_scene_name)

class Finished(Scene):
	end = ["Adventure awaits! "
			"Roll Credits and Music"]

	def enter(self):
		print Finished.end
		exit(1)

class Death(Scene):

	quips = [
		"Oh no! You fell overboard!",
		"You are not a pirate. You're a wannabe.",
		"You have been captured by the enemy.",
		"You angered your crewmates and one of them took revenge while you slept."
	]

	def enter(self):
		print Death.quips[randint (0, len(self.quips) - 1)]
		exit(1)

class PuertoMuelleDock(Scene):

	def enter(self):
		print "Tierrani, a world from another solar system, yet, much like your own planet Earth."
		print "Prepare yourself as you are about to experience a story unlike any other."
		print "A Captain leading the last dying breed of a free-spirited crew where the world around them is ever-changing."
		print "Pursued by the very opposite ideology, a force to be wreckoned with, an empire attempting to control what can never be tamed."
		print "Sentience."

		action = raw_input ("What is your choice, continue, turn back or something else?> ")

		if action == "continue":
			print "You have chosen wisely."
			print "Your mind will now be expanded, intrigued and perplexed at every turn."
			print "Your on the largest ship you've ever been on. Everyone is busy doing something."
			print "Orders are being barked by First and Second mates."
			return 'ship'

		elif action == "turn back":
			print "You turn back to the town and return to your life of being a bakerboy."
			return 'death'
		elif action == "something else":
			print "You missed out on an opportunity."
			return 'death'

class Ship(Scene):

	def enter(self):
		print "You are now on the ship and will become part of the crew, but there is no time to dillydally."
		print "You there with the funny face, tie this wench to the net!"
		print "Quickly now, how many knots would you say this needs?"
		knot = "%d" % (int(2))
		guess = raw_input("[keypad]> ")
		guesses = 0

		while guess != knot and guesses < 3:
			print "That's not right. Try again!"
			guesses += 1
			guess = raw_input("[keypad]> ")

		if guess == '2':
			print "Looks like you've got a knack for this."
			print "Now go onto the main deck and wait for me."
			print "I have further instruction for you, scrub."
			return 'main_deck'

		else:
			print "Looks like you don't even know what a rope is."
			print "I don't think you're cut out for this."
			return 'death'

class MainDeck(Scene):

	def enter(self):
		print "While waiting for the crewmember that asked you about knots, you look around."
		print "Taking in all the hustle and bustle of so much going on in such a confined space."
		print "You hear a voice behind you, 'ye be gawkin or ye be workin?'"

		action = raw_input("How do you respond? gawkin or workin> ")

		if action == 'gawkin':
			print "Ye be useless."
			return 'death'

		elif action == 'workin':
			print "Aye. Best be to be part o' this crew."
			print "You watch our backs. We'll watch your back and front."
			return 'open_sea'

class OpenSea(Scene):

	def enter(self):
		print "You're now in the open sea. Excited as ever and completing every order with fervor and without question."
		print "The lookout yells out 'Trouble ahead! False Colors!' "
		print "The time has come for battle. 'Fill the cannons scrub!' "

		gunpowder_cups = int(4)
		guess = raw_input("How many cups do you put?[cups 1-4]> ")

		if int(guess) != gunpowder_cups:
			print "You put too little"
			print "When they fire the cannons, the shot doesn't come out."
			return 'death'

		else:
			print "You put the right amount!"
			print "Holes are made on the enemy ship!"
			return 'end'

class Map(object):

	scenes = {
		'puerto_muelle_dock': PuertoMuelleDock(),
		'ship': Ship(),
		'main_deck': MainDeck(),
		'open_sea': OpenSea(),
		'death': Death(),
		'end': Finished()
	}

	def __init__(self, start_scene):
		self.start_scene = start_scene

	def next_scene(self, scene_name):
		return Map.scenes.get(scene_name)

	def opening_scene(self):
		return self.next_scene(self.start_scene)

a_map = Map('puerto_muelle_dock')
a_game = Engine(a_map)
a_game.play()