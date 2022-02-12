## Servomotor 

Para el funcionamiendo del servomotor requiere de un ciclo util de una señal PWM de 20 ms, con lo cual solo se requiere del siguiente código, donde solo se compara el valor del contador con la señal de entrada dutty y si es mayor la salida PWM es 1, de lo contrario 0.

```verilog
	`timescale 1ns / 1ps



	module pwm(
	    input enable,
	    input [31:0] period,
	    input [31:0] dutty,
	    input clk,
	    output reg pwm
	    );

	reg[27:0] counter=28'd0;
	reg[15:0] limite;
	reg[15:0] activo;

	always @(posedge clk) begin

	counter <= counter + 28'd1;

	     if(counter>=(period-1))
		counter <= 28'd0;

	     if(counter <= dutty)
		pwm <= 1;
		else
		pwm <=0;

	end

	endmodule
```
 
