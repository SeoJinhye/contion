print("type three number")
a1 = int(raw_input(">"))
a2 = int(raw_input(">"))
a3 = int(raw_input(">"))

if(a1 < a2< a3):
	print("Up and risying(?)")

if(a3 < a2 < a1):
	print("Falling Down")

if(a3 < a2 & a1 < a2):
	print("Over the mountain")

if(a2 < a3 & a2< a1):
	print("in the dog house")