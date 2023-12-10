# app/Dockerfile

FROM python:3.8

WORKDIR /app

# RUN apt-get update && apt-get install -y \
#     build-essential \
#     curl \
#     software-properties-common \
#     git \
#     && rm -rf /var/lib/apt/lists/*

COPY . .

RUN pip3 install -r requirements.txt

EXPOSE 8000

# ENV PORT=80

CMD ["python", "service/app.py"]
# ENTRYPOINT ["streamlit", "run", "service/langchain_PDF.py", "--server.port=8501", "--server.address=0.0.0.0"]