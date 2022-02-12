# Entrega final robot cartógrafo

## Electrónica digital II - Grupo 8

- Andres Felipe Rodriguez Florez
- Nicolas Esteban Gomez Tellez
- Eddy Santiago Delgado Caro

A continuación se mostrará el proyecto de un robot diseñado en base a una arquitectura de System on a chip, en el que por medio de los datos que proporcionan una serie de periféricos al procesador,le permitirán al robot moverse por medio de un laberinto, mapear su recorrido, detenerse en puntos específicos e identificar algunos aspectos de su entorno.

<p align="center">
  <img src="/Imagenes/carro.jpeg" align="center">
</p>


## Periféricos

A continuación se presenta una lista de los periféricos que fueron empleados en el desarrollo de este proyecto. Para más información acerca de cada periférico y de su implementación dar click sobre el periférico.

- [Ultrasonido](https://github.com/unal-edigital2-labs/wp08-2021-2-gr-08/tree/main/SoC_project/module/verilog/ultrasonido)
- [PWM](https://github.com/unal-edigital2-labs/wp08-2021-2-gr-08/tree/main/SoC_project/module/verilog/pwm)
- [Infrarrojo](https://github.com/unal-edigital2-labs/wp08-2021-2-gr-08/tree/main/SoC_project/module/verilog/infrarrojo)
- [Motores](https://github.com/unal-edigital2-labs/wp08-2021-2-gr-08/tree/main/SoC_project/module/verilog/motor)

En el siguiente diagrama se puede ver como se conectan los perifereicos y sus correspondientes modulos con el puente Wishbone y a su vez como se hace la conexión del mismo con el procesador y la memoria.

<p align="center">
  <img src="/Imagenes/esquema1.png" align="center">
</p>

Para este diagrama, realizamos la asignación de memoria, la cual se encuentra detallado en Soc_MemoryMap.csv, y en la siguiente imagen se encuentra la base de memoria para cada periferico.

<p align="center">
  <img src="/Imagenes/base_memoria.png" align="center">
</p>

## SoC

Esta sección tiene como objetivo describir los procesos realizados en Litex de tal manera que los módulos de los periféricos usados se pudieran integrar de manera correcta con el procesador y el bus Wishbone. De los archivos proporcionados en clase se obtiene un procesador picoRV32 y un bus Wishbone y por haciendo uso de Litex se crea el hardware del procesador en la FPGA. en este proyecto se hizo uso tanto de Verilog como de Python para la implementacion de algunos peifericos haciendo uso de Litex. 

## Firmware

En esta sección se explica el código principal main.c con la descripción de las funciones empleadas para el desarrollo del proyecto que permiten el funcionamiento del robot. Para ver información más detallada siga el siguiente [enlace](https://github.com/unal-edigital2-labs/wp08-2021-2-gr-08/tree/main/SoC_project/firmware)

## Alimentación

Para alimentar el robot se hace uso de una powerbank a la que la FPGA siempre debe estar conectada a una fuente para que el hardware y el firmware cargado en esta no se pierda. Los motores se alimentan por separado y para ello se utilizan 8 pilas AAA.

<p align="center">
  <img src="/Imagenes/powerbank.jpeg" align="center">
</p>

## Pruebas de funcionamiento

A continuación se encuentran los enlaces a los videos donde se registran las pruebas de funcionamiento de los perifericos.

- Prueba infrarrojo [video](https://drive.google.com/file/d/13kffaWp2K457gwzorsgMh6wR_2ZYaWx1/view?usp=sharing)
- Prueba ulstrasonido [video](https://drive.google.com/file/d/1ey0Xhe9qSGAbLr63CadsokZ75T6HUz1y/view?usp=sharing)
- Prueba PWM [video](https://drive.google.com/file/d/1RgBu7nsRi5nNKUc0nNvV_0Banl6OJJ0C/view?usp=sharing)
- Prueba motores: derecha[video](https://drive.google.com/file/d/1FrcGwzUQM6VyivukLtw224ZwAYWwkP5J/view?usp=sharing), izquierda[video](https://drive.google.com/file/d/19j1_dJPY0KJHh1XSxGWpkLAYdVuREpwc/view?usp=sharing)
- Prueba uart [video](https://drive.google.com/file/d/1DEueL7_CSkYnbC1ym5uAAPBR0cGD2tzz/view?usp=sharing)

## Problemas presentados

Durante la realización del proyecto se presentaron diversos problemas, los más significativos fueron los siguientes:
- **Módulo de la cámara** Después de realizar distintas pruebas al módulo de la cámara fue imposible hacer que funcionara, este dañaba el resto de modulos y no permitia correr el top. Se realizaron pruebas incluso en vivado pero el error persistia, lo que nos atraso en el tiempo de desarrollo.
- **Tiempo de desarrollo**: Debido al problema expuesto anteriormente el tiempo de desarrollo se alargó para las primeras etapas de la implementación, esto sumado a los inconvenientes de la virtualidad hizo que no se pudiera culminar con exito el proyecto.
- **Modulo de temperatura**:Debido a que nos quedamos estancados en las primeras etapas del proyecto las pocas pruebas que se realizaron con el modulo de temperatura o fueron suficientes para su implementacion en el proyecto.
