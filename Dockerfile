FROM python:3.12
WORKDIR /app
COPY . .
RUN pip install pandas
CMD ["python", "Telemetry Data.py"]
