class JuegoDeLaVida{
  int[][] tablero;
  //Matriz para guardar las celdas vivas y muertas, se le aplican las reglas
  int filasTablero;
  //Guarda el número de filas de la matriz
  int columnasTablero;
  //Guarda el número de columnas de la matriz
  int celulasVivas = 0;
  //Guarda el número de celulas vivas que se vayan encontrando

  JuegoDeLaVida(int filas, int columnas) {//Constructor de la clase Juego de la vida 
    filasTablero = filas;
    //Almacena el número de filas y columnas en sus respectuvas variables
    columnasTablero = columnas;
    tablero = new int[filas][columnas];
    //Crea el tablero del número de filas y columnas que se pase
  }

  int[][] getTablero() {
    //Obtiene el tablero
    return tablero;
  }
  
   int recorrerCeldaCentral(int fila, int columna) {
    //Método que se encarga de recorrer las celdas centrales y retorna
    //el resultado de aplicar las reglas a la celda actual
    int filas = fila, columnas = columna;
    //Almacena las coordenadas en nuevas variables
    int celda;
    //Variable para almacenar el resultado de la evaluación
    for (int i = 0; i <= 8; i++) {
      //For para evaluar los 8 vecinos de la celda
      switch (i) {
        /*Se evalua de forma circular las celdas vecinas de la 
        actual celda. Iniciando por la celda vecina izquierda*/
      case 1:
      case 7:
        columnas++;
        //Evalua la celda derecha y superior a la celula vecina
        this.evaluarVecino(filas, columnas);
        break;
      case 2:
      //Evalua la celda inferior derecha a la celula vecina
        filas++;
        this.evaluarVecino(filas, columnas);
        break;
      case 3:
      case 4:
      //Evalua la celda inferior e inferior izquierda a la celula vecina
        columnas--;
        this.evaluarVecino(filas, columnas);
        break;
      case 5:
      case 6:
      //Evalua la celda izquierda y superior izquierda a la celula vecina
        filas--;
        this.evaluarVecino(filas, columnas);
        break;
      case 8:
      //Evalua la celda superior derecha a la celula vecina
        columnas++;
        this.evaluarVecino(filas, columnas);
        celda = this.aplicarReglas(fila, columna);
        //retorna el resultado e aplicar las reglas
        return celda;
      }
    }
    return 0;
  }

  int recorrerCeldaExterior(int fila, int columna) {
    //Método que se encarga de recorrer las celdas exteriores y retorna
    //el resultado de aplicar las reglas a la celda actual
    int filas = fila, columnas = columna;
    //Almacena las coordenadas en nuevas variables
    int celda;
    //Variable para almacenar el resultado de la evaluación
      for (int i = 0; i <= 8; i++) {
        //For para evaluar los 8 vecinos de la celda
        switch (i) {
        case 1:
        case 7:
          columnas++;
           //Evalua la celda derecha y superior a la celula vecina
          if (filas >= 0 && filas < filasTablero && columnas >= 0
              && columnas < columnasTablero) {
                /*Si el indice de la celula vecina a evaluar se encuentra 
                dentro de la longitud de la matriz, entonces es posible
                aplicar las reglas*/
            this.evaluarVecino(filas, columnas);
          }
          break;
        case 2:
          filas++;
          //Evalua la celda inferior derecha a la celula vecina
          if (filas >= 0 && filas < filasTablero && columnas >= 0
              && columnas < columnasTablero) {
                /*Si el indice de la celula vecina a evaluar se encuentra 
                dentro de la longitud de la matriz, entonces es posible
                aplicar las reglas*/
            this.evaluarVecino(filas, columnas);
          }
          break;
        case 3:
        case 4:
          columnas--;
           //Evalua la celda inferior e inferior izquierda a la celula vecina
          if (filas >= 0 && filas < filasTablero && columnas >= 0
              && columnas < columnasTablero) {
                /*Si el indice de la celula vecina a evaluar se encuentra 
                dentro de la longitud de la matriz, entonces es posible
                aplicar las reglas*/
            this.evaluarVecino(filas, columnas);
          }
          break;
        case 5:
        case 6:
          filas--;
          //Evalua la celda izquierda y superior izquierda a la celula vecina
          if (filas >= 0 && filas < filasTablero && columnas >= 0
              && columnas < columnasTablero) {
                /*Si el indice de la celula vecina a evaluar se encuentra 
                dentro de la longitud de la matriz, entonces es posible
                aplicar las reglas*/
            this.evaluarVecino(filas, columnas);
          }
          break;
        case 8:
          columnas++;
           //Evalua la celda superior derecha a la celula vecina
          if (filas >= 0 && filas < filasTablero && columnas >= 0
              && columnas < columnasTablero) {
                /*Si el indice de la celula vecina a evaluar se encuentra 
                dentro de la longitud de la matriz, entonces es posible
                aplicar las reglas*/
            this.evaluarVecino(filas, columnas);
          }
          celda = this.aplicarReglas(fila, columna);
          //retorna el resultado e aplicar las reglas
          return celda;
        }
      }
      return 0;
  }

  void evaluarVecino(int filas, int columnas) {
    //Método para evaluar las celulas vecinas
    int celda = this.tablero[filas][columnas];
    /*Obtiene el elemento de la matriz celda con las filas 
    y columnas pasadas como parámetro*/
    if (celda == 1) {
      /*Si la celda a evaluar es una 1, entonces aúmenta
      en una unidad la variable de celuas vivas*/
      this.celulasVivas++;
    }
  }

  int aplicarReglas(int filas, int columnas) {
    //Método para aplicar las reglas del juego a la celda evaluada (no es una vecina)
    int celula = this.tablero[filas][columnas];
    /*Obtiene el elemento de la matriz celda con las filas 
    y columnas pasadas como parámetro*/
    if (celula == 1) {
      //Si la celula evaluada es un 1 entonces:
      if (this.celulasVivas == 2 || this.celulasVivas == 3) {
        //Si se encontro dos o tres celulas vivas 
        this.celulasVivas = 0;
        //Vuelve a colocar en cero la variable celuasVivas
        //Retorna 1, pues la celula evaluada será una celula víva
        return 1;
      }
      
       if (this.celulasVivas == 0 || this.celulasVivas == 1) {
         //Si se encontro cero o una celulas vivas
        this.celulasVivas = 0;
        //Vuelve a colocar en cero la variable celuasVivas
        //Retorna 0, pues la celula evaluada será una celula muerta
        return 0;
      }
      
      if (this.celulasVivas >= 4) {
        //Si se encontro 4 o más celulas vivas
        this.celulasVivas = 0;
        //Vuelve a colocar en cero la variable celuasVivas
        //Retorna 0, pues la celula evaluada será una celula muerta
        return 0;
      }
    }else{
      //Sino, si la celula evaluada es una 0 entonces:
    if (celula == 0) {
      //Si se encontro 3 celulas vivas
      if (this.celulasVivas == 3) {
        this.celulasVivas = 0;
        //Vuelve a colocar en cero la variable celuasVivas
        //Retorna 1, pues la celula evaluada será una celula viva
        return 1;
      }
    }
    }
    this.celulasVivas = 0;
    //Vuelve a colocar en cero la variable celuasVivas
    /*Retorna 0, pues la celula evaluada será una celula muerta, en caso
    de que no se cumpla alguna condición anterior*/
    return 0;
  }

}
