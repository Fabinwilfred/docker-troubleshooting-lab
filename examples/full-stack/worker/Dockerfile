FROM python:3.11-slim
WORKDIR /app
COPY worker.sh .
RUN chmod +x worker.sh
CMD ["./worker.sh"]
