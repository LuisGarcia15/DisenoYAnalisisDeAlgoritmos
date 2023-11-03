class Juego{
  JuegoDeLaVida objeto = new JuegoDeLaVida(20,20);
  /*Objeto que se encargará de ejecutar las reglas del juego*/
  String[][] espejo = new String[this.objeto.filasTablero][this.objeto.columnasTablero];
  /*Matriz para copiar el tablero de la instancia objeto e imprimir el resultado*/
  
Juego() {//Constructor de la clase Juego
    println("JUEGO DE LA VIDA");
    println("\n");
    for(int i = 0; i < this.objeto.filasTablero; i++) {
      for(int j = 0; j < this.objeto.columnasTablero; j++) {
        this.objeto.getCeldas()[i][j] = "-";
        /*For para llenar el tablero de la instancia objeto con simbolos -*/
      }  
    }
    /*Coloca ciertas celdas como células "vivas"*/
    this.objeto.getCeldas()[4][2] = "D";
    this.objeto.getCeldas()[4][3] = "D";
    this.objeto.getCeldas()[4][4] = "D";
    this.objeto.getCeldas()[4][5] = "D";
    System.out.println("\n");
  }
  
  void iniziarJuego() {//Método para iniciar el juego
    String celda;
    //Guarda el resultado de evaluar la celda
    boolean entrada = true;
    //Permite iterar otra vez o terminar el juego
    int numeroGeneraciones = 6;
    //Indica el número de generaciones que imprime
    int contadorGeneraciones = 1;
    //Lleva el contador de generaciones que se han impreso
    
    do{//Ejecuta al menos una vez el juego
      println("******** " + contadorGeneraciones + "° Generación ********* \n");
      println(this.imprimirMatriz(this.objeto.getCeldas()));
      //Imprime el estado del objeto actualmente
    for(int filas = 0; filas < this.objeto.filasTablero; filas++) {
      for(int columnas = 0; columnas < this.objeto.columnasTablero; columnas++) {
        //Recorre cada celda del tablero de la instancia objeto
        if(filas == 0| filas == (this.objeto.filasTablero- 1) | columnas == 0 | columnas == (this.objeto.columnasTablero- 1) ) {
          /*si las coordenadas son:
          x = 0 ó x = último indice de la matriz ó y = 0 ó y = último indice de la mátriz
          significa que se esta evaluando una celda exterior y debe llamarse al método para evaluar
          ese tipo de celdas*/
          celda = this.objeto.recorrerCeldaExterior(filas, columnas);
          //Cambia el estado que se obtuvo de la evaluación anterior en la celda que se esta evaluando
          this.espejo[filas][columnas] = celda;
        }else {
          /*Si las coordenadas no son ninguna de las mencionadas, entonces se trata
          de una celda que se encuentra en el interior, por lo que se llama al método
          para evaluar este tipo de celdas*/
          celda = this.objeto.recorrerCeldaCentral(filas, columnas);
          //Cambia el estado que se obtuvo de la evaluación anterior en la celda que se esta evaluando
          this.espejo[filas][columnas] = celda;
        }
      }  
    }
    contadorGeneraciones++;
    //Aumenta en una unidad las generaciones
    this.copiarArrayADT();
    /*copia la matriz espejo a la matriz de la instancia tablero, para poder seguir evaluando las
    siguientes generaciones*/
    entrada = this.evaluarArrayADT();
    /*Evalua si aún hay células vias en la matriz de la instancia objeto*/
    if(!entrada) {
      /*Si ya no quedan celulas vivas, se imprime la última matriz y se informa que termino el juego*/
      println("******** " + contadorGeneraciones + "° Generación ********* \n");
      println(this.imprimirMatriz(this.objeto.getCeldas()));
      println("La población murió en su totalidad en la " + contadorGeneraciones + "° generación");
    }
    if(contadorGeneraciones == (numeroGeneraciones + 1)) {
      /*Verifica si se llego al número de generaciónes disponibles para ejecutar el juego, si lo hizo
      cambia la variable entrada a False*/
      entrada = !entrada;
    }
    }while(entrada);//Itera o no de nuevi el juego dependiendo del valor de la variable entrada
  }
  
  void copiarArrayADT() {
    //Copia la matriz de la variable espejo a la matriz de la instancia objeto
    for(int filas = 0; filas < this.objeto.filasTablero; filas++) {
      for(int columnas = 0; columnas < this.objeto.columnasTablero; columnas++) {
        //Recorre cada celda de la matriz de la instancia objeto
        this.objeto.getCeldas()[filas][columnas] = this.espejo[filas][columnas];
        /*toma el elemento de la celda actual de la matriz espejo y la copia en la celda
        correspondiente de la matriz de la instancia objeto*/
        this.espejo[filas][columnas] = null;
        /*Cambia el valor de la celda actual de la matriz espejo a nulo, para cuando
        se necesite evaluar de nuevo otra generación, no afecte la anterior evaluacion*/
      }  
    }
  }
  
  boolean evaluarArrayADT() {
    for(int filas = 0; filas < this.objeto.filasTablero; filas++) {
      for(int columnas = 0; columnas < this.objeto.columnasTablero; columnas++) {
        //Recorre cada celda de la matriz de la instancia objeto para saber si aún hay celdas vivas
        if(this.objeto.getCeldas()[filas][columnas].equals("D")) {
          /*Si la celda actual es igual a "D", entonces aún hay celdas vivas y retorna true*/
          return true;
        }
      }  
    }
    return false;
  }
  
  String imprimirMatriz(String[][] objeto) {
    /*Almacena con cierto formato, en una variable la matriz que se pasa como parámetro
    para que se pueda imprimir*/
    String array = "";
    for (int i = 0; i < 20; i++) {
      for (int j = 0; j < 20; j++) {
        //Recorre cada celda de la matriz que se pasa como parámetro
        array += objeto[i][j] + "       ";
        //Cada elemento de la celda que se evalua, se guarda en una variable con un espacio
      }
      array += "\n";
      //Agrega un salto de línea a la variable que almacenará la matriz
    }
    return array;
  }
  
}
