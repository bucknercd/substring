import argparse;


def get_shortest_substring(string, substring):
	shortest_substr = ''
	start = 0
	for end in range(1, len(string)+1):
		tmp = string[start:end]
		if is_valid(tmp, substring):
			shortest_substr = tmp
			while True:
				start +=1 
				tmp = string[start:end]
				if is_valid(tmp, substring):
					if len(tmp) < len(shortest_substr):
						shortest_substr = tmp
				else:
					break
	return shortest_substr

def is_valid(tmp, substr):
	for char in substr:
		if char not in tmp:
			return False
	return True

def main():
	parser = argparse.ArgumentParser()
	parser.add_argument('string', type=str, help='String to be parsed.')
	parser.add_argument('substr', type=str, help='String to be parsed.')
	args = parser.parse_args()
	shortest_substr = get_shortest_substring(args.string, args.substr)
	print('String: {}\nSubstring: {}\nThe shortest substring is: {}'.format(args.string, args.substr, shortest_substr))	


if __name__ == '__main__':
	main()
