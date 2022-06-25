locais = {
	1 : {
		'nome' : 'ENTRADA',
		'sul' : 4,
		'leste' : 2,
    'oeste' : 5
	},
	2 : {
		'nome' : 'LABORATÓRIO DE INFORMÁTICA',
		'norte' : 8,
    'oeste' : 1,
    'sul' : 3
	},
	3 : {
		'nome' : 'LANCHONETE',
		'norte' : 2,
    'oeste' : 4,
		'item'  : 'Pimenta'        
	},

	4 : {
		'nome' : 'PATIO',
		'norte' : 1,
    'leste' : 3,
    'oeste' : 6,
    'sul' : 10
	},

	5 : {
		'nome' : 'DIREÇÃO',
    'leste' : 1,
    'sul' : 6
	},

	6 : {
		'nome' : 'BIBLIOTECA',
		'norte' : 5,
    'leste' : 4,
    'oeste' : 7,
    'sul' : 11

	},

	7 : {
		'nome' : 'BANHEIRO',
    'leste' : 6,
    'sul' : 12,  
		'item'  : 'Rosca'

	},

	8 : {
		'nome' : 'SALA  DOS PROFESSORES',
    'leste' : 9,
    'sul' : 2

	},

	9 : {
		'nome' : 'GARAGEM',
    'oeste' : 8
    
	},
	10 : {
		'nome' : 'SALA DE AULA',
    'norte' : 4,
    'oeste' : 11,
    'sul' : 15

	},

	11 : {
		'nome' : 'SALA DA NUTRICIONISTA',
    'norte' : 6,
    'leste' : 10,
    'oeste' : 12,
    'sul' : 14,
		'item' : 'nutricionista'

	},

	12 : {
		'nome' : 'REFEITÓTIO',
    'norte' : 7,
    'leste' : 11,
    'sul' : 13

	},

	13 : {
		'nome' : 'SALA DE JOGOS',
    'norte' : 12,
    'leste' : 14

	},

	14 : {
		'nome' : 'MAMBEE',
    'norte' : 11,
    'leste' : 15,
    'oeste' : 13,
		'item' : 'gato'

	},
	15 : {
		'nome' : 'SALA 2',
    'norte' : 10,
    'oeste' : 14,

	},
}
print ("")
print('             ||||||||||||||||||||||||||||||||||||||||||||||||||||||')
print("             ||||     ESSE JOGO FOI BASEADO EM FATOS REAIS     ||||") 
print('             ||||||||||||||||||||||||||||||||||||||||||||||||||||||')
print('')
print('')
print('')
print('')
print('HISTÓRIA')
print('APÓS ANOS DE PESQUISA ARQUEÓLOGOS CONSEGUIRAM A FÓRMULA SECRETA PARA O ELIXIR DA VIDA ')
print("               QUE ESTAVA ESCONDIDA NAS ANTIGAS PIRÂMIDES DO EGITO")
print("")
print('\033[1m'+'A PIMENTA!'+'\033[1m')
print("")
print("")
print('MAS UM SER DE GRANDE MALDADE NO CORAÇÃO NÃO GOSTAVA DOS PODERES QUE A PIMENTA PROPORCIONAVA AOS MORTAIS')
print("ENTÃO ESSE MOSTRO CHAMADO DE *NUTRICIONISTA* ROUBOU A PIMENTA E À DEIXOU ESCONDIDA EM UM LABIRINTO SEM LUZ")
print("")
print("")
print("POREM EXISTE UMA PROFECIA DE QUE UM(A) BRAVO(A) GUERREIRO(A) IRÁ RECUPERAR A PIMENTA ")
print("        E TRAZER PAZ MAIS UMA VEZ PARA TODAS AS BARRIGAS DOS PIMENTEIROs")
print("")
print("")
print(     "SEJA ESSE HERÓI, RECUPERE A PIMENTA E SALVE A HUMANIDADE!")
print("MAS CUIDADO! VOCÊ NÃO PODE SER PEGO(A) PELA TEERIVÉL *NUTRICIONISTA*")
print("")
print("")
a = str(input(""))
if a == "":
  for n in range (100):
     print("")
else:
  for n in range (100):
     print("")


print('\033[31m'+'██████████ Jogo de RPG ██████████'+'\033[0;0m')
print( )
print('=' * 30)
print( )
print('\033[32m'+'ir [direcao]'+'\033[0;0m')
print('\033[32m'+'pegar [item]'+'\033[0;0m')
print( )
print('=' * 30)
#print('\033[42;1;33m'+''=' * 30 '+'\033[0;0m')
print( )
print('\033[31m'+'Direções: Norte, Sul, Leste, Oeste'+'\033[0;0m')
print()
print('=' * 30)
#print('\033[42;1;33m'+''=' * 30 '+'\033[0;0m')
print( )
print('\033[32m'+'Itens: Pimenta, Rosca e gato'+'\033[0;0m')
print( )
print('\033[32m'+'Sua missão é pegar a Pimenta na Lanchonete, a Rosca no banheiro e chegar ao refeitório sem passar pela nutricionista, mas cuidado ao se deparar com um gato na Mambee.'+'\033[0;0m')
print( )
print('=' * 30)
#print('\033[42m'+'\033[1m'+'\033[33m'+''=' * 30'+'\033[0;0m')
print( )
posicao_atual = locais[1]
inventario = []
while(True):
	print('-'*40)
	print('>>>>> Você está no(a) {}'.format(posicao_atual['nome']))
	print('Inventário',inventario)
	#print('Inventário',inventario)
	print('-'*40)
	entrada = input('> ').split(' ')
	comando = entrada[0]
	if comando == 'ir':
		direcao = entrada[1]
		if direcao in posicao_atual.keys():
			proximo_local = posicao_atual[direcao]			
			posicao_atual = locais[proximo_local]
		else:
			print('>>>>> Você não pode ir por esse caminho')
	elif comando == 'pegar':
		item = entrada[1]
		if item in posicao_atual.values():
			if item not in inventario:
				inventario.append(posicao_atual['item'])
		else:
			print('>>>>> Nesse local não existe itens!')
	else:
		print('>>>>> Comando inválido')
	if ('Pimenta' in inventario) and posicao_atual['nome'] == 'REFEITÓTIO':
		print('Você conseguiu chegar ao refeitório com o molho de pimenta...')
		print('Você comeu a Rosca de quem não gostou do jogo! ')
		print('''\033[31m'+'

	______0000000000000000
 ____0000000000000000000000
_000000000__00000__0000000000
0000000000__00000__00000000000
0000000000__00000__00000000000
000000000000000000000000000000
000000000000000000000000000000
000000__________________000000
000000__________________000000
_000000_________________00000
__0000000_____________000000
____0000000_________0000000
______ 00000000000000000
'+'\033[0;0m''')
		print('\033[34m'+'VOCÊ VENCEU!'+'\033[34m')
		break

	#Quando o jogador entrar em um cômodo com a nutriocionista, irá perder
	
	if 'item' in posicao_atual:
		if 'nutricionista' in posicao_atual['item']:
			print('A nutricionista pegou você...')
			print("Você queimou a Rosca.")
			print('''\033[31m'+'
 			▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄ 
			████▌▄▌▄▐▐▌█████ 
			████▌▄▌▄▐▐▌▀████ 
			▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀ 
			'+'\033[0;0m''')
			print('\033[34m'+'VOCÊ PERDEU!'+'\033[34m')
			break

	#Quando o jogador chegar a cantina com o molho de pimenta e sem passar pela nutricionista ele vence
