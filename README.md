#  Automatizando el hogar con Python Raspberry PI y Reconocimiento de voz

Amazon Echo marcó un hito gigante en la percepción de la tecnología. Si bien el 
reconocimiento de voz es algo presente en la investigación por mas de 60 años, 
la brecha entre el lenguaje natural hablado y el entendido por un ordenador se 
cerró abruptamente en la última década. Las búsquedas por voz de Google ya eran 
posibles desde hace algún tiempo, pero un dispositivo listo para usuario final 
con características de personalización e integración con dispositivos en el 
mercado causó gran impacto en la población estado unidense tanto que tan solo en
2017 se vendieron mas de 20 millones de dispositivos. Otras alternativas como 
Google Home, Apple HomePod, Sonos o Mycroft cerran la brecha mas y mas haciendo 
que el control domótico del hogar sea una labor trivial.

Pero no podemos creer que debemos usar una alternativa privada para realizar el 
control de nuestro hogar, pues alternativas de hardware libre y software libre 
combinadas nos permiten lograr los mismos resultados con un poco de esfuerzo y 
mucha mas satisfacción.

Con un Raspberry PI y un micrófono USB podremos lograr lo mismo e incluso más 
que las alternativas del mercado (aunque podremos lograr los mismos resultados 
con un BeagleBoard, un BananaPi o cualquier otra plataforma de bajo costo que 
nos permita ejecutar linux y nos deje algo de memoria RAM disponible, aunque 
recomiendo 1GB de RAM, si eres un auténtico ninja podrás reducir los servicios 
del sistema operativo y tener todo funcionando en configuraciones inpensables) 
claro, si aún no tienes tu dispositivo puedes hacerlo todo en tu computador 
personal sin ningún problema.

En este corto taller exploraremos un poco la teoría detrás de la magia del 
reconocimiento automático de la voz (Automatic Speech Recognition ASR), 
las metodologías tradicionales basadas en Modelos de Markov Ocultas y Modelos 
de Mixturas Gausianas (Hidden Markov Models - Gaussian Mixture Models HMM-GMM), 
aproximaciones hibridas utilizando Modelos de Markov Ocultos en Redes Neuronales 
Profundas Dependientes de Contexto (Context Dependent Deep Neural Networks Hidden 
Markov Models  CD-DNN-HMM) y por qué no un poco de Redes Neuronales Profundas 
(Deep Neural Networks DNN).


Pero tranquilo, si aún no eres un ninja en aprendizaje profundo existen 
herramientas listas para usar que nos darán las funcionalidades necesarias a 
un `apt` de distancia.

Dejando la teoría y permitiendo que nuestro cerebro respire un poco, trabajaremos 
con pocketsphinx, rasaNLU y GPIO usando scripts para enviar señales a nuestros 
dispositivos físicos y hacer magia.


## Descripción de la charla

El taller propuesto es un taller divulgativo para el uso de python y sus aplicaciones 
prácticas. 

Soy estudiante de Maestría en Ingeniería con énfasis en Ingeniería de Sistemas y 
Computación.  En mi tesis de pregrado trabajé con CMU Sphinx y actualmente me 
encuentro implementando una suite de funciones útiles para usar algoritmos 
tradicionales reescritos en python y potenciados por GPU para el alineamiento 
forzoso de la voz.

Idealmente se requiere que el asistente tenga un Raspberry, un micrófono USB, 
una protoboard, un led y una resistencia de 330 ohm para realizar todo el 
proceso, pero la práctica se puede llevar a cabo con un  computador portatil.

El espacio teórico es agotador y denso, no suele pasar de 20 minutos, pero lo 
prefiero pues regularmente entre la audiencia siempre hay personas con 
conocimientos técnicos avanzados los cuales están interesados en el porqué de 
las cosas.

La parte práctica para una persona con conocimientos en hardware y software es 
de cerca de 15 minutos, pero la configuración de paquetes tiende a ser lenta 
en personas sin conocimientos técnicos, por lo que para este espacio se destina 
una hora.

Finalizando muestro un ejemplo un poco mas aplicado usando SonOFF basic, un 
switch inteligente de bajo costo basado en el módulo ESP8266, donde se escribe 
un servidor en python que controla el dispositivo sin cables, esto tarda 5 
minutos, dejando el taller de 1 hora y 30 minutos aproximadamente.


## Algunos enlaces útiles

### Aproximaciones usando Modelos Ocultos de Markov
- Suite de [CMU Sphinx](https://cmusphinx.github.io/)
  - [Sphinx base](https://github.com/cmusphinx/sphinxbase)
  - [Pocket Sphinx](https://github.com/cmusphinx/pocketsphinx)
  - [Pocket Sphinx JS](https://syl22-00.github.io/pocketsphinx.js/)
### Aproximaciones usando red es neuronales
- [Deep Speech](https://arxiv.org/abs/1412.5567) con su [implementación en tensorflow](https://github.com/mozilla/DeepSpeech)


### Wrappers
- [Speech recognition](https://github.com/Uberi/speech_recognition)


### Un poco de electrónica
- [Raspberry Pi: Control Relay switch via GPIO](https://tutorials-raspberrypi.com/raspberry-pi-control-relay-switch-via-gpio/)
- [Sonoff switch complete hack without firmware upgrade](https://blog.ipsumdomus.com/sonoff-switch-complete-hack-without-firmware-upgrade-1b2d6632c01)
- [Controlling AC Devices with Raspberry PI](https://electronicshobbyists.com/controlling-ac-devices-with-raspberry-pi-raspberry-pi-relay-control/)
- [GPIO Docs](https://www.raspberrypi.org/documentation/usage/gpio/)
- [Configuring Son Off for custom images](https://www.youtube.com/watch?v=BHzsWwd351I)
- [Installing sonoff Tamsota](https://www.youtube.com/watch?v=IcOFeIcLFFo)
- [ESPTool](https://github.com/espressif/esptool)
- [Sonoff-Tasmota](https://github.com/arendst/Sonoff-Tasmota)