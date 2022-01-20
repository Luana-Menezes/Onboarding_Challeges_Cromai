## Uso

1. Dentro da pasta com o arquivo `Dockerfile`, execute o comando build para construir a imagem.
  ```sh
  docker build -t <nome imagem> . 
  ```

2. Rode a imagem com o comando `docker run`.
  ```sh
  docker run -it --privileged <container> /bin/sh 
  ```
  
3. Execute os códigos python dentro do container.
  ```sh
  python LED.py 
  ```
  ```sh
  python sensors_to_csv.py
  ```
