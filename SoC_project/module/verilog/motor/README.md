# Motores

Se utilizaron dos motores y un puente H (L298N) para el movimiento del robot cartógrafo,donde este se alimenta con un arreglo de 8 pilas AA con el fin de suministrar a los motores 12V.
<p align="center">
  <img src="/Imagenes/DC.jpeg" align="center" width="400px" >
</p>

El puente H, según los valores de sus entradas, permite que el robot avance, gire o se detenga, en la siguiente tabla se resumen las acciones que puede realizar dependiendo del valor de sus entradas.

 | Acción | S1 | S2 | S3 | S4 |
| ------------- | ------------- | ------------- |------------- |------------- |
| Avance | 0 | 1 | 1 | 0 |
| Retroceso | 1 | 0 | 0 | 1 |
| Giro Derecha | 1 | 0 | 1 | 0 |
| Giro Izquierda | 0 | 1 | 0 | 1 |
| Pausa | 0 | 0 | 0 | 0 | 



Teniendo en cuenta la anterior tabla se desarrollo el módulo [Motor.v](/Soc_project/module/verilog/Motor.v) que cumple la función de driver para los motores. El código utilizado para la realización del módulo es el siguiente:

```verilog
    parameter AVANCE=2, RETROCESO=1, PAUSA=0, GIROD=3, GIROI=4;

    always @(posedge clk) 
    begin

          case(estado)
            AVANCE: pin = 4'b0110;
            RETROCESO: pin = 4'b1001;
            PAUSA: pin = 4'b0000;
            GIROD: pin = 4'b0101;
            GIROI: pin = 4'b1010;
          default:
            pin = 4'b0000;
          endcase
      end
  ```
      
El funcionamiento del módulo se basa en que según el valor de la señal de entrada **estado** se establecen los valores de los 4 pines de salida siguiendo la tabla descrita anteriormente para que los motores realicen la acción deseada. 
