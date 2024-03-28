FROM python:3.11-slim 
WORKDIR maconduite_back/
COPY requirements.txt .
ADD maconduite_back/* .
RUN pip install --no-cache-dir -r requirements.txt
EXPOSE 5000
CMD ["gunicorn","app:create_app()","-b","0.0.0.0:5000"]