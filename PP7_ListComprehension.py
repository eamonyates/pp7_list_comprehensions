a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]


def even_list(list1):
	b = [number for number in list1 if number % 2 == 0]
	print (b)


if __name__ == "__main__":
	even_list(a)
