import turtle

def apply_rules(curr_char):
	# Define axioms just in terms of if-else statements
	new_str = ''
	if curr_char == 'A':
		new_str = '+A+A+A+A'
		# If you want larger alphabets, just add additional branches
	else:
		# The default production rule, that the character is replaced with itself
		new_str = curr_char

	return new_str

def process_string(curr_str):
	new_str = ''
	for c in curr_str:
		new_str = new_str + apply_rules(c)
	return new_str

def L_system(iterations, axiom):
	omega = axiom
	final_state = ''
	for i in range(iterations):
		final_state = process_string(omega)
		omega = final_state
	return final_state

def draw_system(turtle_instance, instruction_state, delta, line_size, change_line_cycle = False):
	# Rules for processing a given L system as turtle commands
	# To make more diverse curves, can do interesting things like modify the line size through each iteration
	curr_cycle = 0
	cycle_change = 4
	size_change = 5
	for symb in instruction_state:
		if symb == 'A':
			turtle_instance.forward(line_size)
			curr_cycle += 1
		elif symb == 'B':
			turtle_instance.backward(line_size)
			curr_cycle += 1
		elif symb == '+':
			turtle_instance.right(delta)
		elif symb == '-':
			turtle_instance.left(delta)

		if change_line_cycle and curr_cycle % cycle_change == 0:
			line_size += 1

def main():
	# Initial setting for Lindenmayer System
	# Be careful with the number of iterations, as the final state size can grow to be quite large
	axiom = 'A+A+A+A'
	curr_state = axiom
	delta = 90
	num_iterations = 10

	# Setting up turtle functionality, loading the window and instantiating the turtle.
	loadWindow = turtle.Screen()
	t = turtle.Turtle()
	turtle.colormode(255)

	# set turtle to one step below fastest speed (0 is quickest)
	t.speed(0)

	# Get the final Lindenmayer state
	final_state = L_system(num_iterations, axiom)
	draw_system(t, final_state, delta, 1, change_line_cycle=True)

	turtle.exitonclick()

main()