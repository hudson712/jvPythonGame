import pygame, os, sys


pygame.init() # inicia os modulos  Teclado, Video etc

window = pygame.display.set_mode((350,263))  # cria a janela
pygame.display.set_caption('Jogo Da velha!')  # titulo da janela


screen = pygame.display.get_surface()   #pega referencia da tela
posicao=[(20,0),(135,0),(240,0),(20,90),(135,90),(240,90),(20,177),(135,177),(240,177)]
vez = True
contador= 9
ganhou = True
fimDeJogo = False
#True para X , False para O
File = os.path.join(".","tabulero.png") #caminho onde esta imagen
fundo = pygame.image.load(File) #carrega imagen

screen.blit(fundo,(0,0)) #joga a imagem Image na tela
pygame.display.update() #atualiza a tela


File2 = os.path.join(".","alvo.png") #caminho onde esta imagen
alvo = pygame.image.load(File2) #carrega imagen

File3 = os.path.join(".","x.png") #caminho onde esta imagen
x = pygame.image.load(File3) #carrega imagen

File4 = os.path.join(".","o.png") #caminho onde esta imagen
o = pygame.image.load(File4) #carrega imagen

File5 = os.path.join(".","fimX.png") #caminho onde esta imagen
fimX = pygame.image.load(File5) #carrega imagen

File6 = os.path.join(".","fimO.png") #caminho onde esta imagen
fimO = pygame.image.load(File6) #carrega imagen

File7 = os.path.join(".","velha.png") #caminho onde esta imagen
velha = pygame.image.load(File7) #carrega imagen



P=1
screen.blit(alvo,posicao[P-1]) #joga a imagem Image na tela
pygame.display.update() #atualiza a tela


status=[0,0,0,0,0,0,0,0,0]





clock = pygame.time.Clock()
clock.tick(60)

running=True
while (running):
       for event in pygame.event.get(): #fila de eventos
	if event.type == pygame.QUIT:   #evento do X da janela
               running = False
	elif event.type == pygame.KEYDOWN: #se clical alguma tecla
		pygame.event.pump() #carrega o teclado
		key=pygame.key.get_pressed()#pega o teclado
		
		if (key[pygame.K_w]): #verifica se e para cima
			if(P<4):
				P=P+6
			else:
				P=P-3		
	
		elif (key[pygame.K_s]): #verifica se e para cima
			if(P>6):
				P=P-6
			else:
				P=P+3						

		elif (key[pygame.K_a]): #verifica se e para cima
			if((P-1)%3==0):
				P=P+2
			else:
				P=P-1
		elif (key[pygame.K_d]): #verifica se e para cima
			if(P%3==0):
				P=P-2
			else:
				P=P+1	
		elif (key[pygame.K_q]): #verifica se e para cima
			running = False
			

		elif (key[pygame.K_r]): #verifica se e para cima
			vez = True
			ganhou = True
			fimDeJogo = False
			P=1			
			status=[0,0,0,0,0,0,0,0,0]
			contador =9
			
			screen.blit(alvo,posicao[P-1]) #joga a imagem Image na tela
			pygame.display.update() #atualiza a tela

			
		elif (key[pygame.K_e]): #verifica se e para cima
			if (status[P-1]==0):
				contador -=1
				if(vez):
					status[P-1]=1						
					P=1
					vez= not vez
				else:
					status[P-1]=-1
					P=1
					vez= not vez
			

	if (status[0] == 1 and status[1] == 1 and status[2] == 1 or
status[3] == 1 and status[4] == 1 and status[5] == 1 or
status[6] == 1 and status[7] == 1 and status[8] == 1 or
status[0] == 1 and status[3] == 1 and status[6] == 1 or
status[1] == 1 and status[4] == 1 and status[7] == 1 or
status[2] == 1 and status[5] == 1 and status[8] == 1 or
status[0] == 1 and status[4] == 1 and status[8] == 1 or
status[2] == 1 and status[4] == 1 and status[6] == 1 ):
		fimDeJogo = True
		screen.blit(fimX,(0,0)) #joga a imagem Image na tela
		pygame.display.update() #atualiza a tela
	elif (status[0] == -1 and status[1] == -1 and status[2] == -1 or
status[3] == -1 and status[4] == -1 and status[5] == -1 or
status[6] == -1 and status[7] == -1 and status[8] == -1 or
status[0] == -1 and status[3] == -1 and status[6] == -1 or
status[1] == -1 and status[4] == -1 and status[7] == -1 or
status[2] == -1 and status[5] == -1 and status[8] == -1 or
status[0] == -1 and status[4] == -1 and status[8] == -1 or
status[2] == -1 and status[4] == -1 and status[6] == -1 ):
		fimDeJogo = True
		screen.blit(fimO,(0,0)) #joga a imagem Image na tela
		pygame.display.update() #atualiza a tela
	elif (contador==0):
		fimDeJogo = True
		screen.blit(velha,(0,0)) #joga a imagem Image na tela
		pygame.display.update() #atualiza a tela	
		
	
	screen.blit(fundo,(0,0)) #joga a imagem Image na tela
	if(fimDeJogo == False):
		for position, tiro in enumerate(status):
			if(tiro==1):
				screen.blit(x,posicao[position])
			elif (tiro==-1):
				screen.blit(o,posicao[position])

		screen.blit(alvo,posicao[P-1]) #joga a imagem Image na tela
		pygame.display.update() #atualiza a tela


