import circle
import square
import triangle

figs = ['circle', 'square', 'triangle']
funcs = ['perimeter', 'area']
sizes = {
        'circle_perimeter': 1,
    'circle_area': 1,
    'square_perimeter': 1,
    'square_area': 1,
    'triangle_perimeter': 3,
    'triangle_area': 3
}

def sizesRight(fig,sizes):
        if any(size<=0 for size in sizes):
                raise ValueError("Wrong sizes/неправильные размеры фигур, они должны быть больше нуля")
        if fig=='triangle':
                a,b,c=sizes
                if not(a+b>c and b+c>a and a+c>b):
                        raise ValueError("wrong sizes for a triangle/введенные стороны не удовлетворяют правилу построения треугольника")
def calc(fig, func, size):
	assert fig in figs
	assert func in funcs
	sizesRight(fig,size)

	result = eval(f'{fig}.{func}(*{size})')
	return result

if __name__ == "__main__":
	func = ''
	fig = ''
	size = list()
    
	while fig not in figs:
		fig = input(f"Enter figure name, avaliable are {figs}:\n")
	
	while func not in funcs:
		func = input(f"Enter function name, avaliable are {funcs}:\n")
	
	while len(size) != sizes.get(f"{func}_{fig}", 1):
		size = list(map(int, input("Input figure sizes separated by space, 1 for circle and square\n").split(' ')))
	
	calc(fig, func, size)



