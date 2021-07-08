name = 'Josue A. Solares'
age = 31 # not a lie
height = (68 * 25.54)# inches to cm
weight = (170 * 0.45359237) # kg
eyes = 'Brown'
teeth = 'in need of repair'
hair = 'Shades of brown'

print "Let's talk about %r." % name
print "He's %r cm tall." % height
print "He's %r kilos heavy." % weight
print "Actually that's not too heavy."
print "He's got %s eyes and %s hair." % (eyes, hair)
print "His teeth are usually %s depending on the coffee." % teeth

#this line is tricky, try to get it exactly right
print "If I add %d, %d, and %d I get %d." % (age, height, weight, age + height + weight)
