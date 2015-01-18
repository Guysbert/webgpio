# webgpio
A web service that allows you to set raspberry gpio ports by using rest calls

Requisites:
You may need to install python and virtualenv.

To install:

You need root rights to run the program, because otherwise you can't access the gpio ports. The program uses GPIO port 3 at the moment. You can change it in the code.

create virtualenv:
  virtualenv env

change to su
	sudo su
	
activate virtualenv:
	source env/bin/activate
	
install flask
	pip install flask
	
install RPi.GPIO
	pip install RPi.GPIO
	
run the program
	python webgpio.py
