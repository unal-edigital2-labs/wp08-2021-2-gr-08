# Entrega final robot cartógrafo
## Electrónica digital II - Grupo 8

- Andres Felipe Rodriguez Florez 
- Nicolas Esteban Gomez Tellez
- Eddy Santiago Delgado Caro
	
A continuación se mostrará el proyecto de un robot diseñado en base a una arquitectura de System on a chip, en el que por medio de los datos que proporcionan una serie de periféricos al procesador,le permitirán al robot moverse por medio de un laberinto, mapear su recorrido, detenerse en puntos específicos e identificar algunos aspectos de su entorno.

------------imagen-------------

## Periféricos

A continuación se presenta una lista de los periféricos que fueron empleados en el desarrollo de este proyecto. Para más información acerca de cada periférico y de su implementación dar click sobre el periférico.

- [Radar](https://github.com/unal-edigital2-labs/wp08-2021-2-gr-08/tree/main/SoC_project/module/verilog/ultrasonido)
- [Infrarrojo](https://github.com/unal-edigital2-labs/wp08-2021-2-gr-08/tree/main/SoC_project/module/verilog/infrarrojo)

En el siguiente diagrama se puede ver como se conectan los perifereicos y sus correspondientes modulos con el puente Wishbone y a su vez como se hace la conexión del mismo con el procesador y la memoria.

<p align="center">
  <img src="/Imagenes/esquema1.png" align="center">
</p>


## SoC    

Esta sección tiene como objetivo describir los procesos realizados en Litex de tal manera que los módulos de los periféricos usados se pudieran integrar de manera correcta con el procesador y el bus Wishbone. De los archivos proporcionados en clase se obtiene un procesador picoRV32 y un bus Wishbone y por haciendo uso de Litex se crea el hardware del procesador en la FPGA. [Detalles del SoC](https://github.com/unal-edigital2-labs/wp08-2021-2-gr-08/tree/main/SoC_project).



## Firmware

En esta sección se explica el código principal main.c con la descripción de las funciones empleadas para el desarrollo del proyecto que permiten el funcionamiento del robot. Para ver información ma detallada aiga el siguiente [enlace](https://github.com/unal-edigital2-labs/wp08-2021-2-gr-08/tree/main/SoC_project/firmware)

## Alimentación

Para alimentar el robot se hace uso de una powerbank a la que la FPGA siempre debe estar conectada a una fuente para que el hardware y el firmware cargado en esta no se pierda. Los motores se alimentan por separado y para ello se utilizan 8 pilas AAA.

<p align="center">
  <img src="/Imagenes/powerbank.jpeg" align="center">
</p>


## Problemas presentados 



