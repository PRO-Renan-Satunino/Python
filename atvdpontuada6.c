char* verificarSituacao(float media) {
  char* resultado[200];
  media>= 7 ? strcpy(resultado,{"Aprovado!") : strcpy(resultado, "Repovado!");
  return resultado;
}

void mostrarResultado(float notas[]) {\
  printf("\nMedia: %.1f \n", calcularMedia(notas));
  printf("Resultado: %s \n", verificarSituacao(calcularMedia(notas)));
}
