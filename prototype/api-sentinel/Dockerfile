FROM python:3.14
WORKDIR /api-sentinel-app
COPY requirements.txt /api-sentinel-app/
RUN pip install -r /api-sentinel-app/requirements.txt
COPY app /api-sentinel-app/
CMD uvicorn main:app --host 0.0.0.0 --port 8081