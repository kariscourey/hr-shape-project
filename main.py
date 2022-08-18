# import rectangle # must use dot operator if importing entire module # .py not needed ... import rectangle creates an object, and everything in that object can be accessed with dot operator

# from shapes.rectangle import area # use dot operator (?) for shapes
# from shapes.triangle import area # two .areas!!

# from shapes import rectangle
# from shapes import triangle

from shapes import triangle, rectangle # optimized, bart's way

# dot operator = accessing an object (module) within an object (dir)

# from shapes.rectangle import area as rect_area # imports area function but renames it
# from shapes.triangle import area as tri_area # another option for optimzation

# Initialize variables
rect1_height = 10
rect1_width = 10
rect2_height = 200
rect2_width = 100
tri1_height = 10
tri1_width = 10
tri2_height = 200
tri2_width = 100

# Invoke area()
# rect1_area = rectangle.area(rect1_height, rect1_width) # if only import rectangle
# rect2_area = rectangle.area(rect2_height, rect2_width)

rect1_area = rectangle.area(rect1_height, rect1_width)
rect2_area = rectangle.area(rect2_height, rect2_width)
tri1_area = triangle.area(rect1_height, rect1_width)
tri2_area = triangle.area(rect2_height, rect2_width)

# Print result
print(f"Area of rect with a height of {rect1_height} and width of {rect1_width} is {rect1_area}")
print(f"Area of rect with a height of {rect2_height} and width of {rect2_width} is {rect2_area}")
print(f"Area of tri with a height of {tri1_height} and width of {tri1_width} is {tri1_area}")
print(f"Area of tri with a height of {tri2_height} and width of {tri2_width} is {tri2_area}")
