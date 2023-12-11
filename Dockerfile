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

EXPOSE 5000
EXPOSE 8501

# ENV PORT=80

# "--host=0.0.0.0"
# ENTRYPOINT ["streamlit", "run", "service/langchain_PDF.py", "--server.port=5000", "--server.address=0.0.0.0"]

# CMD ["python", "service/app.py"]
RUN echo 'python service/app.py &' >> /entrypoint.sh && \
    echo 'streamlit run service/langchain_PDF.py --server.port=5000 --server.address=0.0.0.0' >> /entrypoint.sh && \
    chmod +x /entrypoint.sh

# 设置 ENTRYPOINT 执行脚本文件
ENTRYPOINT ["/bin/bash", "/entrypoint.sh"]