import numpy as np
import matplotlib.pyplot as plt
import csv


def estimativa(x, y): 
	TamAmostra = np.size(x) 

	xy = (np.sum(x)*np.sum(y)) - (TamAmostra * np.sum(y*x)) 
	xx = (np.sum(x) ** 2) - (TamAmostra *np.sum(x**2))  
	b1 = xy / xx 
	b0 = (np.sum(y) - b1*np.sum(x)) / TamAmostra 

	return(b0, b1) 

with open('AnaliseEstudo.csv') as txt_file:
    separador = ';'
    mediap= []
    idade = []
    falta = []
    TempoEst = []
    cont = 0
    for line_number, content in enumerate(txt_file):
        if line_number:  # pula cabeçalho
            colunas = content.strip().split(separador)
            idade.append(colunas[0])
            TempoEst.append(colunas[1])
            falta.append(colunas[2])
            media = (int(colunas[3]) + int(colunas[4]) + int(colunas[5])) / 3
            mediap.append(media)
            cont+=1
            
    x = np.array(idade).astype(np.int)
    x1 = np.array(tempo).astype(np.int)
    x2 = np.array(falta).astype(np.int)
    y = np.array(mediap).astype(np.float)
    
    a = estimativa(x, y)
    b = estimativa(x1,y)
    c = estimativa(x2,y)
    
    difineidade = 0
    difinetempo = 0
    difinefaltas = 0

    
    for i in range (cont):
        j = a[0] + (int(idade[i]) * a[1])
        k = b[0] + (int(tempo[i]) * b[1])
        l = c[0] + (int(falta[i]) * c[1])
        
        #Media de todas as idades
        #print("idade: "+ idade[i]+"- faltas: "+ falta[i]+ "- tempo: "+ tempo[i] + "- média: "+ str(media_prova[i]))
        
        difineidade += (mediap[i] - j)**2
        difinetempo += (k - mediap[i])**2
        difinefaltas += (l - mediap[i])**2
    

    desvioidade = math.sqrt(difineidade/cont)
    desviotempo = math.sqrt(difinetempo/cont)
    desviofaltas = math.sqrt(difinefaltas/cont)
    
    print("MÉDIA DAS PROVAS POR IDADE".format(a[0], a[1]))
    print("DESVIO PADRÃO: ", desvioidade)
    plot_regression_line(x, y, a)
    
    print("MÉDIA DAS PROVAS POR TEMPO DE ESTUDO".format(b[0], b[1]))
    print("DESVIO PADRÃO: ", desviotempo)
    plot_regression_line(x1, y, b)
    
    print("MÉDIA DAS PROVAS POR FALTAS".format(c[0], c[1]))
    print("DESVIO PADRÃO: ", desviofaltas)
    plot_regression_line(x2, y, c)
#Print da media das provas
#print (media_prova)


    
    
def grafico(x, y, b):  
	plt.scatter(x, y, color = "y", 
			marker = "o", s = 30)  
	y_pred = b[0] + b[1]*x 
	plt.plot(x, y_pred, color = "b") 
	plt.xlabel('x') 
	plt.ylabel('y') 
	plt.show()
