int tablero[][];
/*Arreglo que mostrara el tablero en la ventana*/
int filas,columnas,cuadro_ancho,cuadro_largo;

void setup(){
  //size(1200,800);
  /*Tamaño de la ventana*/
  //background(255);
  /*Color de fondo de la ventana*/
  filas=60;
  /*Indica cuantas celdas tendra el tablero*/
  columnas=40;
  tablero = new int[filas][columnas];
  cuadro_ancho=width/filas;
  /*Divide el los tamaños de la ventana entre el número de filas
  y columnas que tiene el tablero. Esto obtendra el tamaño máximo
  de cada cuadrito dibujado en el tablero tanto en ancho como en alto*/
  cuadro_largo=height/columnas;
  for(int i=0;i<filas;i++){
    for(int j=0;j<columnas;j++){
      /*Recorre cada celda del tablero, y asigna un valor
      entre 0 y 1 a esa celda*/
      tablero[i][j]=round(random(1));
    }
  }
  Juego juego = new Juego();
  juego.iniziarJuego();
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
      if(tablero[j][i]==0){
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

void suAlgoritmo(){
  
}


void draw(){
}
