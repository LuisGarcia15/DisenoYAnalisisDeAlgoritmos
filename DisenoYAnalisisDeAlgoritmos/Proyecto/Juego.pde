class Juego{
  JuegoDeLaVida objeto = new JuegoDeLaVida(20,20);
  String[][] espejo = new String[this.objeto.filasTablero][this.objeto.columnasTablero];
  
  public Juego() {
    int numeroDeCelulas = 1;
    System.out.printf("%22s %n","JUEGO DE LA VIDA");
    System.out.println("\n");
    for(int i = 0; i < this.objeto.filasTablero; i++) {
      for(int j = 0; j < this.objeto.columnasTablero; j++) {
        this.objeto.getCeldas()[i][j] = "-";
      }  
    }

    this.objeto.getCeldas()[4][2] = "D";
    this.objeto.getCeldas()[4][3] = "D";
    this.objeto.getCeldas()[4][4] = "D";
    this.objeto.getCeldas()[4][5] = "D";
    numeroDeCelulas += 4;
    System.out.println("\n");
  }
  
  public void iniziarJuego() {
    String celda;
    boolean entrada = true;
    int numeroGeneraciones = 6;
    int contadorGeneraciones = 1;
    
    do{
      System.out.printf("%40s %n","******** " + contadorGeneraciones + "° Generación ********* \n");
      System.out.println(this.imprimirMatriz(this.objeto.getCeldas()));
    for(int filas = 0; filas < this.objeto.filasTablero; filas++) {
      for(int columnas = 0; columnas < this.objeto.columnasTablero; columnas++) {
        if(filas == 0| filas == (this.objeto.filasTablero- 1) | columnas == 0 | columnas == (this.objeto.columnasTablero- 1) ) {
          celda = this.objeto.recorrerCeldaExterior(filas, columnas);
          this.espejo[filas][columnas] = celda;
        }else {
          celda = this.objeto.recorrerCeldaCentral(filas, columnas);
          this.espejo[filas][columnas] = celda;
        }
      }  
    }
    contadorGeneraciones++;
    this.copiarArrayADT();
    entrada = this.evaluarArrayADT();
    if(!entrada) {
      System.out.printf("%40s %n","******** " + contadorGeneraciones + "° Generación ********* \n");
      System.out.println(this.imprimirMatriz(this.objeto.getCeldas()));
      System.out.printf("%60s %n","La población murió en su totalidad en la " + contadorGeneraciones + "° generación");
    }
    if(contadorGeneraciones == (numeroGeneraciones + 1)) {
      entrada = !entrada;
    }
    }while(entrada);
  }
  
  private void copiarArrayADT() {
    for(int filas = 0; filas < this.objeto.filasTablero; filas++) {
      for(int columnas = 0; columnas < this.objeto.columnasTablero; columnas++) {
        this.objeto.getCeldas()[filas][columnas] = this.espejo[filas][columnas];
        this.espejo[filas][columnas] = null;
      }  
    }
  }
  
  private boolean evaluarArrayADT() {
    for(int filas = 0; filas < this.objeto.filasTablero; filas++) {
      for(int columnas = 0; columnas < this.objeto.columnasTablero; columnas++) {
        if(this.objeto.getCeldas()[filas][columnas].equals("D")) {
          return true;
        }
      }  
    }
    return false;
  }
  
  private String imprimirMatriz(String[][] objeto) {
    String array = "";
    for (int i = 0; i < 20; i++) {
      for (int j = 0; j < 20; j++) {
        array += objeto[i][j] + "       ";
      }
      array += "\n";
    }
    return array;
  }
  
}
