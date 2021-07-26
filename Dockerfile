FROM python:3.8-slim

# Copy local directory to /app in container
# Dont use COPY * /app/ , * will lead to lose of folder structure in /app
COPY . /app/

# Change WORKDIR
WORKDIR /app

# Install dependencies
# use --proxy http://<proxy host>:port if you have proxy
RUN pip install -r requirements.txt

# In Docker, the containers themselves can have applications running on ports. To access these applications, we need to expose the containers internal port and bind the exposed port to a specified port on the host.
# Expose port and run the application when the container is started
EXPOSE 5000:5000
ENTRYPOINT python app.py




# FROM python:3.7
#
#
# # Copy local directory to /app in container
# # Dont use COPY * /app/ , * will lead to lose of folder structure in /app
# COPY ./ /app/
#
# # Change WORKDIR
# WORKDIR /app
#
# # Install dependencies
# # use --proxy http://<proxy host>:port if you have proxy
# RUN pip install -r requirements.txt
#
# EXPOSE 9999:9999
#
# CMD python app.py

# RUN pip install pipenv
#
# ADD . /flask-deploy
#
# WORKDIR /flask-deploy
#
# RUN pipenv install --system --skip-lock
#
# RUN pip install gunicorn[gevent]
#
# EXPOSE 5000

# CMD gunicorn --worker-class gevent --workers 8 --bind 0.0.0.0:5000 wsgi:app --max-requests 10000 --timeout 5 --keep-alive 5 --log-level info