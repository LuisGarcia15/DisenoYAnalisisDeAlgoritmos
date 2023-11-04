JuegoDeLaVida juego;
//Objeto para evaluar las reglas
int matrizAux[][];
/*Arreglo que mostrara el tablero en la ventana*/
int filas,columnas,cuadro_ancho,cuadro_largo;
/*Variables para indicar el número de celdas en el tablero*/

void setup(){
  size(1200,800);
  /*Tamaño de la ventana*/
  background(255);
  /*Color de fondo de la ventana*/
  filas=60;
  /*Indica cuantas celdas tendra el tablero*/
  columnas=40;
  juego = new JuegoDeLaVida(filas,columnas);
  this.matrizAux = new int[filas][columnas];
  cuadro_ancho=width/filas;
  /*Divide el los tamaños de la ventana entre el número de filas
  y columnas que tiene el tablero. Esto obtendra el tamaño máximo
  de cada cuadrito dibujado en el tablero tanto en ancho como en alto*/
  cuadro_largo=height/columnas;
  for(int i=0;i<filas;i++){
    for(int j=0;j<columnas;j++){
      /*Recorre cada celda del tablero, y asigna un valor
      entre 0 y 1 a esa celda*/
      this.juego.getTablero()[i][j]=round(random(1));
    }
  }
}

void pintaTablero(){
  float x=0;
  /*Variables que tomarán el valor de cuadro_largo
  y cuadro_ancho para dibujar los cuadrados seguidos
  en la ventana*/
  float y=0;
  for(int i=0;i<columnas;i++){
    /*Recorre todo el tablero*/
    x=0;
    /*Cada que cambia de columna, x obtiene el valor
    de 0*/
    for(int j=0;j<filas;j++){
      /*Si la celda actual del tablero es igual a cero,
      se pinta de color blanco las formas que se utilicen
      a partir de está linea de código*/
      if(this.juego.getTablero()[j][i]==0){
        fill(0);
      }
      else{
        /*Sino, se pinta de color negro las formas que se utilicen
      a partir de está linea de código*/
        fill(255);
      }
      /*Crea un cuadrado con las coordenadas en las variables x e y, y de tamaño
      con las coordenadas cuadrado_ancho y cuadrado_largo. Tendrá el color del
      parámentro fill() que se allá llamado en ese momento*/
      rect(x,y,cuadro_ancho,cuadro_largo);
      x+=cuadro_ancho;
      /*Aumenta la variable x, el valor de la variable cuadro_ancho para pintar
      los siguientes cuadrados de forma consecutiva*/
    }
    y+=cuadro_largo;
    /*Aumenta la variable y, el valor de la variable cuadro_largo para pintar
      los siguientes cuadrados de forma la misma altura*/
  }
}

void ciclo(){
  /*Ciclo para hacer que se pinte la ventana en pausas y pueda
  observarse el cambio de celdas*/
  for(int i=0;i<1000000000;i++){
    for(int j=0;j<1000000000;j++){
    }
  }
  loop();
  //Permite llamar nuevamente a la función draw()
}
void draw(){
  noLoop();
  //Permite teminar el ciclo que geneere loop()
  pintaTablero();
  /*Llama a la función pintaTablero() para pintar la generación
  actual de celulas vivas*/
  verificarReglas();
  /*Llama a la función iniciarJuego() para evaluar las celular
  del tablero actual*/
  ciclo();
  /*Permite volver a llamar a la función draw() para
  ver el nacimiento/muerte de las celulas*/
}
/*################################*/

void verificarReglas() {//Método para verificar las reglas del juego
    int celda;
    //Guarda el resultado de evaluar la celda
    for(int numFilas = 0; numFilas < filas; numFilas++) {
      for(int numColumnas = 0; numColumnas < columnas; numColumnas++) {
        //Recorre cada celda del tablero de la instancia juego
        if(numFilas == 0| numFilas == (filas- 1) | numColumnas == 0 | numColumnas == (columnas- 1) ) {
          /*si las coordenadas son:
          x = 0 ó x = último indice de la matriz ó y = 0 ó y = último indice de la mátriz
          significa que se esta evaluando una celda exterior y debe llamarse al método para evaluar
          ese tipo de celdas*/
          celda = this.juego.recorrerCeldaExterior(numFilas, numColumnas); //<>//
          /*Cambia el estado que se obtuvo de la evaluación anterior en la celda que se esta evaluando
          al aplicar las reglas del juego*/
          this.matrizAux[numFilas][numColumnas] = celda;
        }else {
          /*Si las coordenadas no son ninguna de las mencionadas, entonces se trata
          de una celda que se encuentra en el interior, por lo que se llama al método
          para evaluar este tipo de celdas*/
          celda = this.juego.recorrerCeldaCentral(numFilas, numColumnas);
          /*Cambia el estado que se obtuvo de la evaluación anterior en la celda que se esta evaluando
          al aplicar las reglas del juego*/
          this.matrizAux[numFilas][numColumnas] = celda;
        }
      }  
    }
    this.copiarArrayADT();
    /*Copia la matriz de ayuda a la matriz del tablero de la instancia juego, para mostrar
    la nueva generación que se formo*/
  }
  
  void copiarArrayADT() {
    //Copia la matriz de la variable espejo a la matriz de la instancia objeto
    for(int numFilas = 0; numFilas < filas; numFilas++) {
      for(int numColumnas = 0; numColumnas < columnas; numColumnas++) {
        //Recorre cada celda de la matriz de la instancia juego
        this.juego.getTablero()[numFilas][numColumnas] = this.matrizAux[numFilas][numColumnas];
        /*toma el elemento de la celda actual de la matriz de ayuda y la copia en la celda
        correspondiente de la matriz de la instancia juego*/
        this.matrizAux[numFilas][numColumnas] = 0;
        /*Cambia el valor de la celda actual de la matriz de ayuda a 0, para cuando
        se necesite evaluar de nuevo otra generación, no afecte la anterior evaluacion*/
      }  
    }
  }
