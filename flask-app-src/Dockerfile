# buid imafge starting from python image
FROM python:3.6.3

# add the current directory into the path `code/flask-app` in the image
ADD . code/flask-app/

# set `code/flask-app/` as workdir in the image
WORKDIR code/flask-app/

# install python dependencies
RUN pip install -r requirements.txt

# set the default command for container to `python app.py`
CMD ["python", "app.py"]