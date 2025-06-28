# Etapa 1: imagem base com Python
FROM python:3.12-slim

# Etapa 2: define diretório de trabalho
WORKDIR /app

# Copia apenas o backend pro container
COPY ./backend /app

# Instala dependências
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Expõe a porta do container
EXPOSE 8000

# Comando para iniciar o servidor
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
