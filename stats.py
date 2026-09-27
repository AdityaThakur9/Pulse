def average(x):
	total=sum(x)
	length= len(x)
	if length == 0:
		return 0
	avr=total/length
	return avr
if __name__ == "__main__":
    print(average([10, 20]))
    print(average([4, 5, 6]))
    print(average([]))