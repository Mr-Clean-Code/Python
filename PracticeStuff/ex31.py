print "You enter a dark room with two doors. Do you go through door #1, #2 or #3?"

door = raw_input(">")

if door == "1":
	print "There's a giant bear here eating a cheese cake. What do you do?"
	print "1. Take the cake."
	print "2. Scream at the bear."
	
	bear = raw_input("> What is your choice? = ")
	
	if bear == "1":
		print "The bear eats your face off. Oh no!"
	elif bear == "2":
		print "The bear rips off your legs. Oh no!"
	else:
		print "Well, doing %s is probably better. Bear runs away." % bear
		
elif door == "2":
	print "You stare into the endless abyss of Cthulu's retina. What thought do you choose to think about?"
	print "1. Blueberries."
	print "2. Yellow jacket clothespins."
	print "3. Understanding revolvers yelling melodies."
	
	insanity = raw_input(">What is your choice of thought? = ")
	
	if insanity == "1" or insanity == "2":
		print "Your body survives powered by a mind of jello. Good job!"
	else:
		print "The insanity rots your eyes into a pool of mush dripping down your face. Nice!"

elif door == "3":
	print "There are two levers. Which one do you choose?"
	print "1. Red Lever"
	print "2. Blue Lever"
	
	lever = raw_input(">Pick a number...or don't = ")
	
	if lever == "1":
		print "A bag of gold falls from the ceiling. You get to live."
	elif lever == "2":
		print "A bag of fools gold falls from the ceiling. You get to live, but foolishly."
else:
	print "You stumble around and fall on a propped up knife and die. Oh no!"