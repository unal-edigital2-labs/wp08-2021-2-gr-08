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
