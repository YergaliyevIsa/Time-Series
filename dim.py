from math import sin, cos, sqrt, log


def x_y(a, b, t):
	return a * cos(t), b * sin(t)

def heaviside(x):
	return 1 if x >= 0 else 0

def p_o(a, b):
	return sqrt((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2)

def p_k(w, n, n0, k):
	return sqrt(sum([(p_o(w[n - k +  i], w[n0 - k + i])) ** 2 for i in range(k)]))
		

def lam_cor(k, N, time_ser):
	l = 0.5	
	ans = []	
	while l > 0.001:	
		ckl = sum([heaviside(l - p_k(time_ser, i, j, k)) for i in range(N) for j in range(N)]) / (N * N)
		tmp = log(ckl) / log(l)		
		ans.append(tmp)		
		l /= 2
	return ans

a, b = 3, 2
k = 10
points = []	
delta_t = [1, 0.1, 0.01, 0.001]
N = 1000
for time in delta_t:      
	points.append([x_y(a, b, i * time)  for i in range(N)])

for time_ser in points:
	ans = lam_cor(k, N, time_ser)
	print(ans)
	


		
