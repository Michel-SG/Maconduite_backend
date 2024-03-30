FROM python:3.11-slim 
WORKDIR /app
ENV PYTHONUNBUFFERED 1
ADD . .
RUN pip install --no-cache-dir -r requirements.txt
# CMD ["flask","run","--host=0.0.0.0"]
CMD ["gunicorn","maconduite_back.app:create_app()","--workers","1","-b","0.0.0.0:5000"]