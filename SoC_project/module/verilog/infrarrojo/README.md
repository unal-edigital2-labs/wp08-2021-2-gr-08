# Infrarrojo

Esta seccion es la encargada de implementar el seguidor de linea del robot, ya que con este set de sensores infrarrojos se detecta la cinta negra que dicta el recorido del carro. En este caso se hace uso de 5 sensores infrarrojos que fueron adquiridos en el siguiente arreglo.

<p align="center">
  <img src="/Imagenes/ir.jpeg" align="center">
</p>

Como se puede ver en el código, la descripción es muy sencilla ya ue solo se igualan cinco pines declarados de la FPGA a cinco pines, correspondientes a cada sensor de tal forma que en el firmware, dependiendo se lo que se envíe se decide si el robot está siguiendo la cinta, recibiendo un 1 solo del sensor del medio, o si se desvió, recibiendo un 1 de algun otro sensor. Asimismo si se detecta que todos los sensores estan enviando un 1 el robot se detemdrá ya que esto le indica que se debe iniciar otro proceso con el radar.

```verilog
    `timescale 1ns / 1ps

      module infrarrojo(
      input [4:0] infras,
      output [4:0] infras2
    );

     assign infras2 = infras;

    endmodule
```

