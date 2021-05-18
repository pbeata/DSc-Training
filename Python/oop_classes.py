import turtle

class Polygon:
	def __init__(self, num_sides, name, size=100, color="black", lw=2):
		self.num_sides = num_sides
		self.name = name
		self.size = size  # default size is 100
		self.color = color
		self.lw = lw
		self.interior_angles_sum = (self.num_sides - 2) * 180
		self.single_angle = self.interior_angles_sum / self.num_sides

	# print details about the attributes
	def print(self):
		print("\npolygon name:", self.name)
		print("number of sides:", self.num_sides)
		print("sum of interior angles:", self.interior_angles_sum)
		print("value for single angle:", self.single_angle)		

	# draw the polygon shape
	def draw(self):
		turtle.color(self.color)
		turtle.pensize(self.lw)
		for i in range(self.num_sides):
			turtle.forward(self.size)
			turtle.right(180 - self.single_angle)
		turtle.done()


# PART 1: The Basics
 
# plaza = Polygon(4, "Square", 200, color="blue", lw=5)
# plaza.print()
# plaza.draw()

# building = Polygon(5, "Pentagon")
# building.print()
# # building.draw()

# stop_sign = Polygon(6, "Hexagon", 150, color="red", lw=5)
# stop_sign.print()
# stop_sign.draw()


# PART 2: Inheritance and Subclassing

class Square(Polygon):
	def __init__(self, size=100, color="black", lw=2):
		# Polygon is the "super" class
		super().__init__(4, "Square", size, color, lw)

	# overriding the member function from Polygon
	def draw(self):
		turtle.begin_fill()
		super().draw()
		turtle.end_fill()

# square = Square(color="blue", size=200)
# print(square.num_sides)
# print(square.single_angle)
# square.draw()
# turtle.done()



# PART 3: Operator Overloading

import matplotlib.pyplot as plt

class Point:
	def __init__(self, x, y):
		self.x = x
		self.y = y

	def __add__(self, other):
		if isinstance(other, Point):
			x = self.x + other.x
			y = self.y + other.y
		else:
			x = self.x + other
			y = self.y + other
		return Point(x,y)

	def pplot(self):
		plt.plot(self.x, self.y, 'kx')
		plt.show()


point1 = Point(4, 5)
print(point1.x, point1.y)
# point1.pplot()

a = Point(1, 1)
b = Point(2, 2)
c = a + b
print(c.x, c.y)

d = a + 5
print(d.x, d.y)