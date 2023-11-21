import math as m

def binomial(espacio,exitos,pexito):
#Se usa cuando es un experimento de dos posibles resultados con experimentos CON reposicion.
#espacio = N, exitos = K, pexito = P(k)
    numerador = m.factorial(espacio)
    denominador = (m.factorial(exitos)*m.factorial(espacio-exitos))
    independiente = (pexito**exitos)*((1-pexito)**(espacio-exitos))
    proba = numerador/denominador*independiente
    return proba

def poisson(lamda,exitos):
#Se usa cuando necesitas contabilizar cantidad de exitos en un periodo continuo (tiempo u otro) - Usualmente cuando las probabilidades de exito son chicas.
#lamda = lambda, exitos = k
    '''
    tiempo
    ratio
    lamda = tiempo * ratio
    '''
    numerador = (lamda**exitos)
    denominador = m.factorial(exitos)
    independiente = m.e**(-lamda)
    proba = numerador/denominador*independiente
    return proba

def hiper(poblacion,exitos,muestra,valor):
#Se usa cuando es un experimento SIN reposicion.
#poblacion = N, exitos en la poblacion = k, muestra = n, valor (de la proba buscada) = v
    numerador1 = m.factorial(exitos)/(m.factorial(valor)*m.factorial(exitos-valor))
    numerador2 = m.factorial(poblacion-exitos)/(m.factorial(muestra-valor)*m.factorial((poblacion-exitos)-(muestra-valor)))
    denominador = m.factorial(poblacion)/(m.factorial(muestra)*m.factorial(poblacion-muestra))
    proba = numerador1*numerador2/denominador
    return proba

def normalizar(valor,media,desvio):
#Se suele usar cuando dan una media y desvio standar.
#valor = x (valor de variable no estandarizada), media = media, desvio = desvio (ojo no es varianza!!)
    resultado = (valor - media)/desvio
    return resultado