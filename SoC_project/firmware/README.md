# Firmware

## Radar

Para esta sección se tienen en cuenta dos funciones pwm test() y ultra_test(). En la función del pwm se controla el movimiento del servo motor dandole diferentes valores a duty y en función de esto el servomotor apuntara en un ángulo diferente.

```c
static void pwm_test(void)
{
    unsigned int period = 2000000;
    unsigned int dutty = 0;
    unsigned int enable = 1;

    pwm_cntrl_enable_write(enable);
    printf("Test de pwm ... se interrumpe con el boton 1\n");

    delay_ms(10);


    dutty = 40000;
    pwm_cntrl_period_write(period);
    pwm_cntrl_dutty_write(dutty);
    delay_ms(1000);

    dutty = 60000;
    pwm_cntrl_period_write(period);
    pwm_cntrl_dutty_write(dutty);
    delay_ms(1000);

    dutty = 250000;
    pwm_cntrl_period_write(period);
    pwm_cntrl_dutty_write(dutty);
    delay_ms(1000);

}
```

Por otro lado en la funciónn ultra_test(), el valor de la variable orden es la que define si se mide una distancia, en la variable distancia se almacena el valor tomado por el sensor y finalmente done indica cuando termino el proceso.

```c

static void ultra_test(void)
{

    unsigned int orden = 0;
    unsigned int distancia = 0;
    unsigned int done = 0;

    ultra_cntrl_orden_write(orden);
    printf("Test de ultrasonido ... se interrumpe con el boton 1\n");

    delay_ms(10);


    while(!(buttons_in_read()&1)){


    orden = 0;
    ultra_cntrl_orden_write(orden);

    delay_ms(1000);
    orden = 1;
    ultra_cntrl_orden_write(orden);
    delay_ms(1000);

    distancia = ultra_cntrl_d_read();
    printf("distancia : %d \n",2*distancia);
    done = ultra_cntrl_DONE_read();
    printf("done : %d \n",done);

    delay_ms(1000);

    }

}
```

## Cámara

En esta función se declaran 3 variables en donde col puede tomar 4 valores 001, 010, 100 y 111 que corresponden a azul, verde, rojo y ninguno, dependiendo de la lectura que se haga con la cámara. Esta función retorna el valor de la variable col.

```c
int camara(void){

	unsigned int col = 0;
	unsigned int done = 0;
	unsigned int error = 0;

	printf("Test de camara ... se interrumpe con el boton 1\n");

		col = camara_cntrl_res_read();
		done = camara_cntrl_done_read();
		error = camara_cntrl_error_read();
		if(done){
			if(!error){
				switch (col){
	 				case 1: printf("Azul \n"); break;
	 				case 2: printf("Verde \n"); break;
	 				case 4: printf("Rojo \n"); break;
	 				case 7: printf("Ninguno \n"); break;
				}
			}
		}
	camara_cntrl_init_write(1);
	delay_ms(10);
	camara_cntrl_init_write(0);
	delay_ms(1000);

	return col;

}
```

## Sensor infrarrojo

En esta función se leen los valores entregados por el infrarrojo, el cual tiene 5 sensores, representados a través de un arreglo de 5 bits, los cuales se leen con la función infra_cntrl_infras2_read y luego se imprime para saber su valor.

```c
static void infra_test(void){
	printf("Test de infra ... se interrumpe con el boton 1\n");
	while(!(buttons_in_read()&1)) {
		printf("Infrarrojo: %lu \n",infra_cntrl_infras2_read());
		delay_ms(1000);
		}

}

```

## Motores

Para los motores hicimos uso de un puente H para poder controlar el encendido y apagado de cada motor, así como poder implementarle una potencia distinta. Para ello creamos 4 funciones para poder revisar las cuatro posibles estados, adelante, atras, giro izquierda y giro derechar, los cuales son interpretados por el puente H a través de un codigo binario, el cual enviamos por medio de la función motor_cntrl_estado_write.

```c
static void adelante(void)
{
    printf("Test del motor... se interrumpe con el botton 1\n");
        while(!(buttons_in_read()&1)) {
	motor_cntrl_estado_write(12); // 1 derecha adelante
	}
}

static void derecha(void)
{
    printf("Test del motor... se interrumpe con el botton 1\n");
        while(!(buttons_in_read()&1)) {
	motor_cntrl_estado_write(10); // 1 derecha adelante
	}
}

static void izquierda(void)
{
    printf("Test del motor... se interrumpe con el botton 1\n");
        while(!(buttons_in_read()&1)) {
	motor_cntrl_estado_write(9); // 1 derecha adelante
	}
}

static void atras(void)
{
    printf("Test del motor... se interrumpe con el botton 1\n");
        while(!(buttons_in_read()&1)) {
	motor_cntrl_estado_write(3); // 1 derecha adelante

	}
}


```

## UART

Se crearon 2 canales de comunicación UART para realizar la comunicación con el dispositivo bluethoot, el cual para poder probarlo usamos un test poniendo el tx y el rx en corto, así se escribe un dato y se espera que de salida sea el mismo dato.

```c
static void uart1_test(void){
	printf("Test de la uart 1, debe poner en corto el pon RX Tx de la la UART1.\n");

	printf("se envia el caracter A por la uart 1  y al estar en loopback se recibe el caracter  y se retrasmite por la uart 0\n");
	printf("se interrumpe con el botton 1\n");
	unsigned int matriz[2][2]={{1,2},{3,4}};
	unsigned int dato = 0;
	uart1_write(97);
	while(!(buttons_in_read()&1)) {

	dato = uart1_read();
	if(dato == 97)
	printf("listo\n");
	else printf("no listo\n");
	delay_ms(500);
	}
}

```
