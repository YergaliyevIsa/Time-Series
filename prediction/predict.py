

def make_ellipse(x1, y1, x2, y2, x3, y3):
	a_sqr = ((y1 * x2) ** 2 - (y2 * x1) ** 2) / (y1 * y1 - y2 * y2)
	b_sqr = y1 * y1 * a_sqr / (a_sqr - x1 * x1)
	
def make_hyberbola(x1, y1, x2, y2, x3, y3):
	b_sqr = ((x2 * y1) ** 2 - (y2 * x1) ** 2) / (x1 * x1 - x2 * x2)
	a_sqr = x1 * x1 * b_sqr / (y1 * y1 + b_sqr)

def make_parabola(x1, y1, x2, y2, x3, y3):
	p = y1 * y1 / (2 * x1)



*points, curve_type = list(map(int, input().split(', ')))

if curve_type == 1:
	make_ellipse(*points)
elif curve_type == 2:
	make_hyberbola(*points)
elif curve_type == 3:
	make_parabola(*points)

