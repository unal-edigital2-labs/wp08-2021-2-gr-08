# Radar 
El periferico consta de dos partes, el sensor ultrasonico HC-SR04 y el servomotor. Lo que se busca es que el servomotor gire de tal manera que el sensor ultrasonico a punte en tres direcciones, adelante, izquierda y derecha y al momento en que el servo motor este apuntando en alguna de las direcciones mencionadas el sensor ultrasonico tome una muestra dodnde se mida la distancia de la pared que el robo tienen en esa dirección, con el objeivo que con esa informacion el robot sea capaz de de moverse sin chocar.

<p align="center">
  <img src="/Imagenes/ultras.jpeg" align="center">
</p>

## Ultrasonido

Tomando como guía el trabajo realizado por el grupo 4 del 2021-I se tienen dos modulos principales para el funcionamiento del sensor de ultrasonido "controlador.v" y "genpulsos.v" con los cuales se va a poder realizar el envio de pulsos y el calculo de la distancia del obstaculo.

### Para [contador.v](https://github.com/unal-edigital2-labs/wp08-2021-2-gr-08/blob/main/SoC_project/module/verilog/ultrasonido/contador.v)

Este módulo tiene como propósito generar el pulso que le indica al ultrasonido el inicio de la operacion y asi comenzar el calculo de la distancia entre el sensor y el obstáculo, esto por medio de la medición del ancho de la señal y lo que demora en volver esta al sensor. Este proceso lo describe el siguiente código.


```verilog
module contador		(
				output wire	[7:0] count,
				output reg	pulse,
				output reg	calculate,
				input	ECHO,
				//input	sign,
				input	ENABLE,
				input	CLKOUT,
				input	reset
			);
	reg [7:0] count0;
	reg logico;
	//reg calculate;
	initial 
	begin
		count0=0;
		pulse=0;
		calculate=0;
	end
	
	always@(posedge CLKOUT)
	begin
		logico=(count0[7]||count0[6]||count0[5]||count0[4]||count0[3]||count0[2]||count0[1]||count0[0]);
		if(reset)
		begin
			count0=0;
			calculate=0;
			pulse=0;
		end
		//	Da la orden de mandar un pulso
		else
		begin
			if(ENABLE)
			begin
				pulse=1'b1;
			end
			//
			//	Cuenta el rango que tiene el pulso del ECHO del sensor
			//
			if(ECHO)
			begin
				count0=count0+1;
			end
			if(!ECHO && logico)
			begin
				calculate = 1;
			end
		end
	end
	assign count = count0;
endmodule
```

### Para [genpulsos.v](https://github.com/unal-edigital2-labs/wp08-2021-2-gr-08/blob/main/SoC_project/module/verilog/ultrasonido/genpulsos.v)

Este módulo tiene como propósito indicarle al sensor cuando genere una señal PWM, la cual será la señal trigg, emitiendo asi las ondas que rebotaran en los obstaculos próximos del robot, teniendo asi la informacion para medir la distancia.Este proceso lo describe el siguiente código.

El código utilizado para realizar este proceso es el siguiente:

```verilog
module	genpulsos	(
				input		pulse,
				input		CLKOUT1,
				input		reset,
				//input		ECHO,
				//output	sign,
				output		trigg
			);
	reg	Doit;
	reg	NoDoit;
	assign trigg=(Doit && ~NoDoit);
	
	initial
	begin
		Doit<=0;
		NoDoit<=0;
	end

	always@(posedge CLKOUT1)
	begin
		if(reset)
		begin
			Doit<=0;
			NoDoit<=0;
		end
		else
		begin
			if(pulse)
			begin
				Doit<=1'b1;
			end
			if(pulse && Doit)
			begin
				NoDoit<=1'b1;
			end
		end
	end
	//assign	sign=ECHO;
endmodule
```

 
