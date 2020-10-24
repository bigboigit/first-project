ask = 0
ar = []
while ask < 5:
	ask_user = int(input('ENTER A NUMBER --> '))
	ar.append(ask_user)
	ask += 1
def print_max(num_list):
	max_value = max(num_list)
	return max_value

print(print_max(ar))