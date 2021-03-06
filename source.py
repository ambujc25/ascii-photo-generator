from PIL import Image
import math

while True:
	name = input("Enter file name: ")
	siz = int(input("Ente size: "))
	try:
		im = Image.open(name)
	except:
		continue;
		
	print(im.size)

	#im = im.resize((int(0.02*im.size[0]),int(0.02*im.size[1])))
	im = im.resize((siz,siz))
	#im.thumbnail((40, 40))

	rows,cols = (im.size[0],im.size[1])
	print(rows,cols)
	arr = [[0]*cols for i in range(rows)]

	arr = list(im.getdata())
	arr = [arr[i*cols: (i+1)*cols] for i in range(rows)]

	brightness_matrix = [[0]*cols for i in range(rows)]

	i = 0;
	#for col in range(cols):
		#brightness_matrix[i][col] = int((arr[i*cols+col][0] + arr[i*cols + col][1] + arr[i*cols + col][2])/3);

	for row in range(rows):
		for col in range(cols):
			brightness_matrix[row][col] = math.floor((arr[row][col][0] + arr[row][col][1] + arr[row][col][2])/3)
			#brightness_matrix[row][col] = 0.21*arr[row][col][0] + 0.72*arr[row][col][1] + 0.07*arr[row][col][2]
			#brightness_matrix[row][col] = int((max(arr[row][col][0],arr[row][col][1],arr[row][col][2]) + min(arr[row][col][0],arr[row][col][1],arr[row][col][2]))/2)
			#print(int((arr[row][col][0]+arr[row][col][1]+arr[row][col][2])/3),end = " ")

	ascii_chars = "`^,:;Il!i~+_-?][}{1)(|/tfjrxnuvczXYUJCLQ0OZmwqpdbkhao*#MW&8@$"

	divider = 255/(len(ascii_chars)-1)

	ascii_matrix = [[0]*cols for i in range(rows)]
	for row in range(rows):
		for col in range(cols):
			ascii_matrix[row][col] = ascii_chars[math.floor(brightness_matrix[row][col]/divider)]

	width = int(input("Enter width(1.Narrow, 2.Medium, 3.Wide)"))

	for row in range(rows):
		for col in range(cols):
			for p in range(width):
				print(ascii_matrix[row][col],end = "")
		print()

	cont = input("Do you want to exit? (Y or N)")
	if cont=='Y' or cont=='y':
		break;
