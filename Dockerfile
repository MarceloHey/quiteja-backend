# Usar uma imagem oficial do Python
FROM python:3.10

# Definir o diretório de trabalho dentro do container
WORKDIR /app

# Copiar o arquivo requirements.txt para o diretório de trabalho
COPY requirements.txt .

# Instalar as dependências
RUN pip install --no-cache-dir -r requirements.txt

# Copiar todo o código da aplicação para o diretório de trabalho
COPY . .

# Expôr a porta que a aplicação vai rodar
EXPOSE 5000

# Comando para rodar a aplicação
CMD ["python", "./app/app.py"]