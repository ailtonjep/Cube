def cube_generator():
	#Gera o cubo
	#Não recebe argumentos, retorna uma lista correspondente as posições do cubo
	#"\033[x;ym" é a formatação da cor da peça correspondente
	#O cubo é dividido em faces, as faces divididas em linhas, e as linhas em peças

	#Gera a face verde do cubo
	green_cube1  = ["\033[32;42m""vd1""\033[m","\033[32;42m""vd2""\033[m","\033[32;42m""vd3""\033[m"]
	green_cube2  = ["\033[32;42m""vd4""\033[m","\033[32;42m""vd5""\033[m","\033[32;42m""vd6""\033[m"]
	green_cube3  = ["\033[32;42m""vd7""\033[m","\033[32;42m""vd8""\033[m","\033[32;42m""vd9""\033[m"]
	green_cube   = [green_cube1,green_cube2,green_cube3]

	#Gera a face azul do cubo
	blue_cube1   = ["\033[34;44m""az1""\033[m","\033[34;44m""az2""\033[m","\033[34;44m""az3""\033[m"]
	blue_cube2   = ["\033[34;44m""az4""\033[m","\033[34;44m""az5""\033[m","\033[34;44m""az6""\033[m"]
	blue_cube3   = ["\033[34;44m""az7""\033[m","\033[34;44m""az8""\033[m","\033[34;44m""az9""\033[m"]
	blue_cube    = [blue_cube1, blue_cube2, blue_cube3]

	#Gera a face amarelo do cubo
	yelow_cube1  = ["\033[33;43m""am1""\033[m","\033[33;43m""am2""\033[m","\033[33;43m""am3""\033[m"]
	yelow_cube2  = ["\033[33;43m""am4""\033[m","\033[33;43m""am5""\033[m","\033[33;43m""am6""\033[m"]
	yelow_cube3  = ["\033[33;43m""am7""\033[m","\033[33;43m""am8""\033[m","\033[33;43m""am9""\033[m"]
	yelow_cube   = [yelow_cube1,yelow_cube2,yelow_cube3]

	#Gera a face branco do cubo
	white_cube1  = ["\033[37;47m""br1""\033[m","\033[37;47m""br2""\033[m","\033[37;47m""br3""\033[m"]
	white_cube2  = ["\033[37;47m""br4""\033[m","\033[37;47m""br5""\033[m","\033[37;47m""br6""\033[m"]
	white_cube3  = ["\033[37;47m""br7""\033[m","\033[37;47m""br8""\033[m","\033[37;47m""br9""\033[m"]
	white_cube   = [white_cube1,white_cube2,white_cube3]

	#Gera a face vermelho do cubo
	red_cube1    = ["\033[31;41m""vm1""\033[m","\033[31;41m""vm2""\033[m","\033[31;41m""vm3""\033[m"]
	red_cube2    = ["\033[31;41m""vm4""\033[m","\033[31;41m""vm5""\033[m","\033[31;41m""vm6""\033[m"]
	red_cube3    = ["\033[31;41m""vm7""\033[m","\033[31;41m""vm8""\033[m","\033[31;41m""vm9""\033[m"]
	red_cube     = [red_cube1,red_cube2,red_cube3]

	#Gera a face laraja do cubo
	orange_cube1 = ["\033[35;45m""lr1""\033[m","\033[35;45m""lr2""\033[m","\033[35;45m""lr3""\033[m"]
	orange_cube2 = ["\033[35;45m""lr4""\033[m","\033[35;45m""lr5""\033[m","\033[35;45m""lr6""\033[m"]
	orange_cube3 = ["\033[35;45m""lr7""\033[m","\033[35;45m""lr8""\033[m","\033[35;45m""lr9""\033[m"]
	orange_cube  = [orange_cube1,orange_cube2,orange_cube3]

	#Concatena as listas gerando o cubo
	cube = [green_cube,blue_cube,white_cube,yelow_cube,orange_cube,red_cube]
	
	return cube
def print_cube (cube):
	#Gera uma representação 2D do cubo
	#Usa unicode pra desenhar as linhas
	#http://www.unicode.org/charts/PDF/U2500.pdf
	#Cada linha de código desse bloco corresponde a uma limha impressa

	graphic_cube = "\n"
	graphic_cube = graphic_cube + "\t"+10*" "+u"\u2554"+3*u"\u2550"+u"\u2566"+3*u"\u2550"+u"\u2566"+3*u"\u2550"+u"\u2557"+"\n"
	graphic_cube = graphic_cube + "\t"+10*" "+u"\u2551"+cube[3][0][0]+u"\u2551"+cube[3][0][1]+u"\u2551"+cube[3][0][2]+u"\u2551"+"\n"
	graphic_cube = graphic_cube + "\t"+10*" "+u"\u2560"+3*u"\u2550"+u"\u256C"+3*u"\u2550"+u"\u256C"+3*u"\u2550"+u"\u2563"+"\n"
	graphic_cube = graphic_cube + "\t"+10*" "+u"\u2551"+cube[3][1][0]+u"\u2551"+cube[3][1][1]+u"\u2551"+cube[3][1][2]+u"\u2551"+"\n"
	graphic_cube = graphic_cube + "\t"+10*" "+u"\u2560"+3*u"\u2550"+u"\u256C"+3*u"\u2550"+u"\u256C"+3*u"\u2550"+u"\u2563"+"\n"
	graphic_cube = graphic_cube + "\t"+10*" "+u"\u2551"+cube[3][2][0]+u"\u2551"+cube[3][2][1]+u"\u2551"+cube[3][2][2]+u"\u2551"+"\n"
	graphic_cube = graphic_cube + "\t"+10*" "+u"\u255A"+3*u"\u2550"+u"\u2569"+3*u"\u2550"+u"\u2569"+3*u"\u2550"+u"\u255D"+"\n"

	graphic_cube = graphic_cube + 4*" "+u"\u2554"+3*u"\u2550"+u"\u2566"+3*u"\u2550"+u"\u2566"+3*u"\u2550"+u"\u2557"+" "+u"\u2554"+3*u"\u2550"+u"\u2566"+3*u"\u2550"+u"\u2566"+3*u"\u2550"+u"\u2557"+" "+u"\u2554"+3*u"\u2550"+u"\u2566"+3*u"\u2550"+u"\u2566"+3*u"\u2550"+u"\u2557"+" "+u"\u2554"+3*u"\u2550"+u"\u2566"+3*u"\u2550"+u"\u2566"+3*u"\u2550"+u"\u2557"+" "+"\n"
	graphic_cube = graphic_cube + 4*" "+u"\u2551"+cube[5][0][0]+u"\u2551"+cube[5][0][1]+u"\u2551"+cube[5][0][2]+u"\u2551"+" "+u"\u2551"+cube[0][0][0]+u"\u2551"+cube[0][0][1]+u"\u2551"+cube[0][0][2]+u"\u2551"+" "+u"\u2551"+cube[4][0][0]+u"\u2551"+cube[4][0][1]+u"\u2551"+cube[4][0][2]+u"\u2551"+" "+u"\u2551"+cube[1][0][0]+u"\u2551"+cube[1][0][1]+u"\u2551"+cube[1][0][2]+u"\u2551"+"\n"
	graphic_cube = graphic_cube + 4*" "+u"\u2560"+3*u"\u2550"+u"\u256C"+3*u"\u2550"+u"\u256C"+3*u"\u2550"+u"\u2563"+" "+u"\u2560"+3*u"\u2550"+u"\u256C"+3*u"\u2550"+u"\u256C"+3*u"\u2550"+u"\u2563"+" "+u"\u2560"+3*u"\u2550"+u"\u256C"+3*u"\u2550"+u"\u256C"+3*u"\u2550"+u"\u2563"+" "+u"\u2560"+3*u"\u2550"+u"\u256C"+3*u"\u2550"+u"\u256C"+3*u"\u2550"+u"\u2563"+"\n"
	graphic_cube = graphic_cube + 4*" "+u"\u2551"+cube[5][1][0]+u"\u2551"+cube[5][1][1]+u"\u2551"+cube[5][1][2]+u"\u2551"+" "+u"\u2551"+cube[0][1][0]+u"\u2551"+cube[0][1][1]+u"\u2551"+cube[0][1][2]+u"\u2551"+" "+u"\u2551"+cube[4][1][0]+u"\u2551"+cube[4][1][1]+u"\u2551"+cube[4][1][2]+u"\u2551"+" "+u"\u2551"+cube[1][1][0]+u"\u2551"+cube[1][1][1]+u"\u2551"+cube[1][1][2]+u"\u2551"+"\n"
	graphic_cube = graphic_cube + 4*" "+u"\u2560"+3*u"\u2550"+u"\u256C"+3*u"\u2550"+u"\u256C"+3*u"\u2550"+u"\u2563"+" "+u"\u2560"+3*u"\u2550"+u"\u256C"+3*u"\u2550"+u"\u256C"+3*u"\u2550"+u"\u2563"+" "+u"\u2560"+3*u"\u2550"+u"\u256C"+3*u"\u2550"+u"\u256C"+3*u"\u2550"+u"\u2563"+" "+u"\u2560"+3*u"\u2550"+u"\u256C"+3*u"\u2550"+u"\u256C"+3*u"\u2550"+u"\u2563"+"\n"
	graphic_cube = graphic_cube + 4*" "+u"\u2551"+cube[5][2][0]+u"\u2551"+cube[5][2][1]+u"\u2551"+cube[5][2][2]+u"\u2551"+" "+u"\u2551"+cube[0][2][0]+u"\u2551"+cube[0][2][1]+u"\u2551"+cube[0][2][2]+u"\u2551"+" "+u"\u2551"+cube[4][2][0]+u"\u2551"+cube[4][2][1]+u"\u2551"+cube[4][2][2]+u"\u2551"+" "+u"\u2551"+cube[1][2][0]+u"\u2551"+cube[1][2][1]+u"\u2551"+cube[1][2][2]+u"\u2551"+"\n"
	graphic_cube = graphic_cube + 4*" "+u"\u255A"+3*u"\u2550"+u"\u2569"+3*u"\u2550"+u"\u2569"+3*u"\u2550"+u"\u255D"+" "+u"\u255A"+3*u"\u2550"+u"\u2569"+3*u"\u2550"+u"\u2569"+3*u"\u2550"+u"\u255D"+" "+u"\u255A"+3*u"\u2550"+u"\u2569"+3*u"\u2550"+u"\u2569"+3*u"\u2550"+u"\u255D"+" "+u"\u255A"+3*u"\u2550"+u"\u2569"+3*u"\u2550"+u"\u2569"+3*u"\u2550"+u"\u255D"+"\n"
	
	graphic_cube = graphic_cube + "\t"+10*" "+u"\u2554"+3*u"\u2550"+u"\u2566"+3*u"\u2550"+u"\u2566"+3*u"\u2550"+u"\u2557"+"\n"
	graphic_cube = graphic_cube + "\t"+10*" "+u"\u2551"+cube[2][0][0]+u"\u2551"+cube[2][0][1]+u"\u2551"+cube[2][0][2]+u"\u2551"+"\n"
	graphic_cube = graphic_cube + "\t"+10*" "+u"\u2560"+3*u"\u2550"+u"\u256C"+3*u"\u2550"+u"\u256C"+3*u"\u2550"+u"\u2563"+"\n"
	graphic_cube = graphic_cube + "\t"+10*" "+u"\u2551"+cube[2][1][0]+u"\u2551"+cube[2][1][1]+u"\u2551"+cube[2][1][2]+u"\u2551"+"\n"
	graphic_cube = graphic_cube + "\t"+10*" "+u"\u2560"+3*u"\u2550"+u"\u256C"+3*u"\u2550"+u"\u256C"+3*u"\u2550"+u"\u2563"+"\n"
	graphic_cube = graphic_cube + "\t"+10*" "+u"\u2551"+cube[2][2][0]+u"\u2551"+cube[2][2][1]+u"\u2551"+cube[2][2][2]+u"\u2551"+"\n"
	graphic_cube = graphic_cube + "\t"+10*" "+u"\u255A"+3*u"\u2550"+u"\u2569"+3*u"\u2550"+u"\u2569"+3*u"\u2550"+u"\u255D"+"\n"
	
	print (graphic_cube)

#Movimentos do cubo
def motion_face1 (cube, color):
	#Deslocamento das peças em uma mesma face de forma horária
	#Passa cube[3][2] como tupla pq seu conteúdo será alterado
	#'color' recebe a cor da face que será girada
	# Verde => 0; Azul= 1; Branco= 2; Amarelo= 3; Laranha= 4; Vermelho= 5

	provisional_cube 	 = list(cube[color][2])
	cube[color][2][0]    = cube[color][2][2]
	cube[color][2][1]    = cube[color][1][2]
	cube[color][2][2]    = cube[color][0][2]
	cube[color][1][2]    = cube[color][0][1]
	cube[color][0][2]    = cube[color][0][0]
	cube[color][0][1]    = cube[color][1][0]
	cube[color][0][0]    = provisional_cube[0]
	cube[color][1][0]    = provisional_cube[1]
	
	return cube
def motion_face2 (cube, color):
	#Deslocamento das peças em uma mesma face de forma anti horária
	#Passa cube[3][2] como tupla pq seu conteúdo será alterado
	#'color' recebe a cor da face que será girada
	# Verde => 0; Azul= 1; Branco= 2; Amarelo= 3; Laranha= 4; Vermelho= 5

	provisional_cube = list(cube[color][2])
	cube[color][2][2]    = cube[color][2][0]
	cube[color][2][0]    = cube[color][0][0]
	cube[color][2][1]    = cube[color][1][0]
	cube[color][0][0]    = cube[color][0][2]
	cube[color][1][0]    = cube[color][0][1]
	cube[color][0][1]    = cube[color][1][2]
	cube[color][0][2]    = provisional_cube[2]
	cube[color][1][2]    = provisional_cube[1]

	return cube
def motion_u  (cube):
	#Movimento U do cubo
	provisional_cube = list(cube[0][0])
	cube[0][0]		 = cube[4][0]
	cube[4][0]		 = cube[1][0]
	cube[1][0]		 = cube[5][0]
	cube[5][0]		 = provisional_cube

	motion_face1 (cube, 3)
	
	return cube
def motion_ul (cube):
	#Movimento U' do cubo
	provisional_cube = list(cube[5][0])
	cube[5][0]		 = cube[1][0]
	cube[1][0]		 = cube[4][0]
	cube[4][0]		 = cube[0][0]
	cube[0][0]		 = provisional_cube
	
	motion_face2 (cube, 3)
	
	return cube
def motion_d  (cube):
	#Movimento D do cubo
	provisional_cube = list(cube[5][2])
	cube[5][2]		 = cube[1][2]
	cube[1][2]		 = cube[4][2]
	cube[4][2]		 = cube[0][2]
	cube[0][2]		 = provisional_cube
	
	motion_face1 (cube, 2)
	
	return cube
def motion_dl (cube):
	#Movimento D' do cubo
	provisional_cube = list(cube[0][2])
	cube[0][2]		 = cube[4][2]
	cube[4][2]		 = cube[1][2]
	cube[1][2]		 = cube[5][2]
	cube[5][2]		 = provisional_cube

	motion_face2 (cube,2)
	
	return cube
def motion_l  (cube):
	#Movimento L do cubo
	provisional_cube = list(cube[3][0])
	cube[3][0][0]    = cube[4][0][2]
	cube[3][0][1]    = cube[4][1][2]
	cube[3][0][2]    = cube[4][2][2]
	
	cube[4][0][2]    = cube[2][2][2]
	cube[4][1][2]    = cube[2][2][1]
	cube[4][2][2]    = cube[2][2][0]
	
	cube[2][2][0]    = cube[5][0][0]
	cube[2][2][1]    = cube[5][1][0]
	cube[2][2][2]    = cube[5][2][0]
	
	cube[5][0][0]    = provisional_cube[2]
	cube[5][1][0]    = provisional_cube[1]
	cube[5][2][0]    = provisional_cube[0]
		
	motion_face1 (cube, 1)

	return cube
def motion_ll (cube):
	#Movimento L' do cubo
	cube1			 =	cube[5][2][0]
	cube2			 =	cube[5][1][0]
	cube3			 =	cube[5][0][0]

	provisional_cube =	cube1,cube2,cube3

	cube[5][2][0] 	 =	cube[2][2][2]
	cube[5][1][0] 	 =	cube[2][2][1]
	cube[5][0][0]	 =	cube[2][2][0]

	cube[2][2][0]	 =	cube[4][2][2]
	cube[2][2][1]	 =	cube[4][1][2]
	cube[2][2][2]	 =	cube[4][0][2]

	cube[4][2][2]	 =	cube[3][0][2]
	cube[4][1][2]	 =	cube[3][0][1]
	cube[4][0][2]	 =	cube[3][0][0]

	cube[3][0]		 =	list(provisional_cube)
	
	motion_face2 (cube, 1)

	return cube
def motion_r  (cube):
	#Movimento R do cubo
	cube1			 =	cube[5][2][2]
	cube2			 =	cube[5][1][2]
	cube3			 =	cube[5][0][2]

	provisional_cube =	cube1,cube2,cube3

	cube[5][2][2] 	 =	cube[2][0][2]
	cube[5][1][2] 	 =	cube[2][0][1]
	cube[5][0][2]	 =	cube[2][0][0]

	cube[2][0][0]	 =	cube[4][2][0]
	cube[2][0][1]	 =	cube[4][1][0]
	cube[2][0][2]	 =	cube[4][0][0]

	cube[4][2][0]	 =	cube[3][2][2]
	cube[4][1][0]	 =	cube[3][2][1]
	cube[4][0][0]	 =	cube[3][2][0]

	cube[3][2]		 =	list(provisional_cube)
	
	motion_face1 (cube, 0)

	return cube
def motion_rl (cube):
	#Movimento R' do cubo
	provisional_cube = list(cube[3][2])
	cube[3][2][0]    = cube[4][0][0]
	cube[3][2][1]    = cube[4][1][0]
	cube[3][2][2]    = cube[4][2][0]
	
	cube[4][0][0]    = cube[2][0][2]
	cube[4][1][0]    = cube[2][0][1]
	cube[4][2][0]    = cube[2][0][0]
	
	cube[2][0][0]    = cube[5][0][2]
	cube[2][0][1]    = cube[5][1][2]
	cube[2][0][2]    = cube[5][2][2]
	
	cube[5][0][2]    = provisional_cube[2]
	cube[5][1][2]    = provisional_cube[1]
	cube[5][2][2]    = provisional_cube[0]
		
	motion_face2 (cube, 0)

	return cube
def motion_f  (cube):
	#Movimento F do cubo
	cube1			 =	cube[3][0][0]
	cube2			 =	cube[3][1][0]
	cube3			 =	cube[3][2][0]

	cube[3][0][0] 	 =	cube[1][2][2]
	cube[3][1][0] 	 =	cube[1][1][2]
	cube[3][2][0]	 =	cube[1][0][2]

	cube[1][2][2]	 =	cube[2][0][0]
	cube[1][1][2]	 =	cube[2][1][0]
	cube[1][0][2]	 =	cube[2][2][0]

	cube[2][0][0]	 =	cube[0][0][0]
	cube[2][1][0]	 =	cube[0][1][0]
	cube[2][2][0]	 =	cube[0][2][0]

	cube[0][0][0]	=	cube1
	cube[0][1][0]	=	cube2
	cube[0][2][0]	=	cube3
		
	motion_face1 (cube, 5)

	return cube
def motion_fl (cube):
	#Movimento F' do cubo
	cube3 			=	cube[0][2][0]
	cube2 			=	cube[0][1][0]
	cube1 			=	cube[0][0][0]

	cube[0][2][0]	=	cube[2][2][0]
	cube[0][1][0]	=	cube[2][1][0]
	cube[0][0][0]	=	cube[2][0][0]

	cube[2][2][0]	=	cube[1][0][2]
	cube[2][1][0]	=	cube[1][1][2]
	cube[2][0][0]	=	cube[1][2][2]

	cube[1][0][2]	=	cube[3][2][0]
	cube[1][1][2]	=	cube[3][1][0]
	cube[1][2][2]	=	cube[3][0][0]

	cube[3][2][0]	=	cube3
	cube[3][1][0]	=	cube2
	cube[3][0][0]	=	cube1

	motion_face2 (cube, 5)

	return cube
def motion_b  (cube):
	#Movimento B do cubo
	cube3 			=	cube[0][2][2]
	cube2 			=	cube[0][1][2]
	cube1 			=	cube[0][0][2]

	cube[0][2][2]	=	cube[2][2][2]
	cube[0][1][2]	=	cube[2][1][2]
	cube[0][0][2]	=	cube[2][0][2]

	cube[2][2][2]	=	cube[1][0][0]
	cube[2][1][2]	=	cube[1][1][0]
	cube[2][0][2]	=	cube[1][2][0]

	cube[1][0][0]	=	cube[3][2][2]
	cube[1][1][0]	=	cube[3][1][2]
	cube[1][2][0]	=	cube[3][0][2]

	cube[3][2][2]	=	cube3
	cube[3][1][2]	=	cube2
	cube[3][0][2]	=	cube1

	motion_face1 (cube, 4)

	return cube
def motion_bl (cube):
	#Movimento B' do cubo
	cube1			 =	cube[3][0][2]
	cube2			 =	cube[3][1][2]
	cube3			 =	cube[3][2][2]

	cube[3][0][2] 	 =	cube[1][2][0]
	cube[3][1][2] 	 =	cube[1][1][0]
	cube[3][2][2]	 =	cube[1][0][0]

	cube[1][2][0]	 =	cube[2][0][2]
	cube[1][1][0]	 =	cube[2][1][2]
	cube[1][0][0]	 =	cube[2][2][2]

	cube[2][0][2]	 =	cube[0][0][2]
	cube[2][1][2]	 =	cube[0][1][2]
	cube[2][2][2]	 =	cube[0][2][2]

	cube[0][0][2]	=	cube1
	cube[0][1][2]	=	cube2
	cube[0][2][2]	=	cube3
		
	motion_face2 (cube, 4)

	return cube

def scramble  (cube,functions=locals()):
	import random
	motion    = ["u","ul","d","dl","l","ll","r","rl","f","fl","b","bl"]
	
	for i in range(random.randint(12,22)):
		sort = random.choice(motion)
		#print (sort)
		select = "motion_" + sort
		functions [select] (cube)
	
	return cube

#Programa principal

cube=cube_generator()
scramble(cube)
print_cube(cube)
'''
cube = cube_generator()
for x in range(255000):
	print(x)
	scramble(cube)

print_cube(cube)
'''