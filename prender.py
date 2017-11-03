#!/usr/bin/env python

import RPi.GPIO as gpio
import time
#Metodo que inicializa los GPIO y los estados de los LED's
def inicializar():
	gpio.setmode(gpio.BCM)
	gpio.setwarnings(False)
	#GPIO 17, 27 y 22 seran las luces roja, amarilla y verde de la primera interseccion (sur-norte/norte-sur) respectivamente
	gpio.setup(17,gpio.OUT)
	gpio.setup(27,gpio.OUT)
	gpio.setup(22,gpio.OUT)
	#GPIO 23, 24, y 25 seran las luces verde, amarilla y roja de la primera interseccion (oriente-occidente/occidente-oriente)
	gpio.setup(23,gpio.OUT)
	gpio.setup(24,gpio.OUT)
	gpio.setup(25,gpio.OUT)

	#GPIO 18 representara la interrupcion de un ciclo normal
	gpio.setup(18,gpio.IN)
	#Al iniciar la ejecucion unicamente se prendera el LED verde norte-sun y el rojo oriente-occidente
	gpio.output(22,gpio.HIGH)
	gpio.output(17,gpio.LOW)
	gpio.output(27,gpio.LOW)

	gpio.output(23,gpio.LOW)
	gpio.output(24,gpio.LOW)
	gpio.output(25,gpio.HIGH)

	print 'PINES CORRECTAMENTE CONFIGURADOS'
	print 'INICIANDO CICLO...'

#Metodo que representa el comportamiento normal de un semanforo
def ciclo_normal():
	print 'Ciclo Normal'
	while True:
		#Si se detecta una interrupcion, se llama al metodo ciclo_interrupcion()
		if(gpio.input(18)):
			print 'Inicia interrupcion'
			ciclo_interrupcion()

		print 'Luz verde'
		gpio.output(22,gpio.HIGH)
		gpio.output(25,gpio.HIGH)
		time.sleep(3)
		if(gpio.input(18)):
                        print 'Inicia interrupcion'
                        ciclo_interrupcion()

		print 'Luz amarilla'
		gpio.output(22,gpio.LOW)
		gpio.output(25,gpio.LOW)
		gpio.output(27,gpio.HIGH)
		gpio.output(24,gpio.HIGH)
		time.sleep(1)
		gpio.output(27,gpio.LOW)
		gpio.output(24,gpio.LOW)
		if(gpio.input(18)):
                        print 'Inicia interrupcion'
                        ciclo_interrupcion()

		print 'Luz roja'
		gpio.output(17,gpio.HIGH)
		gpio.output(23,gpio.HIGH)
		time.sleep(3)
		gpio.output(17,gpio.LOW)
		gpio.output(23,gpio.LOW)
		if(gpio.input(18)):
                        print 'Inicia interrupcion'
                        ciclo_interrupcion()
		print 'Luz amarilla'
		gpio.output(27,gpio.HIGH)
		gpio.output(24,gpio.HIGH)
		time.sleep(1)
		gpio.output(27,gpio.LOW)
		gpio.output(24,gpio.LOW)
		if(gpio.input(18)):
                        print 'Inicia interrupcion'
                        ciclo_interrupcion()


def ciclo_interrupcion():
	#Se inicia el ciclo de interrupcio que inicia en verde, y hace una vuelta completa
	print 'Luz verde'
        gpio.output(22,gpio.HIGH)
	gpio.output(25,gpio.HIGH)
        time.sleep(3)
        print 'Luz amarilla'
        gpio.output(22,gpio.LOW)
	gpio.output(25,gpio.LOW)
        gpio.output(27,gpio.HIGH)
	gpio.output(24,gpio.HIGH)
        time.sleep(1)
        print 'Luz roja'
        gpio.output(27,gpio.LOW)
	gpio.output(24,gpio.LOW)
        gpio.output(17,gpio.HIGH)
	gpio.output(23,gpio.HIGH)
        time.sleep(3)
        gpio.output(17,gpio.LOW)
	gpio.output(23,gpio.LOW)
        print 'Luz amarilla'
        gpio.output(27,gpio.HIGH)
	gpio.output(24,gpio.HIGH)
        time.sleep(1)
	gpio.output(24,gpio.LOW)
        gpio.output(27,gpio.LOW)
	#Una vez termina el ciclo de interrupcion, se retorna al ciclo normal
	print
	print 'Termina interrupcion'
	print
	print 'Volviendo al cliclo noraml'
	print
	ciclo_normal()


inicializar()
ciclo_normal()
