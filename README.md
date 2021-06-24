# Predictive_Maintenance_NSIN_MarineCorps



### Project Description:
This is a joint collaboration between NSIN and Marine Corps to build an end to end predictive maintenance solution. When we say we are going to deploy the model in production or productionalize the model, we are referring to integrating the machine learning model into an existing business application. In simple terms, we expose the ML model as REST API endpoints to serve the requests within the application platform or to direct user requests. 



### NSIN Team:
1. Mahmoud Hamsho
2. Grant Wilson
3. Farid Nemri

### Marine Corps Team:
1. Howard Ting
2. Dana Lain


### Dependencies:
* Flask: An open source lightweight web framework built in Python to deploy web applications
* Docker: A computer program that performs operating-system-level virtualization, also known as containerization
* Jinja2: HTML framwor


## Solution Architecture:

![Alt text](/images/NSIN_Solution_Architecture.png?raw=true "Solution Architecture")

**Flask** is a very lightweight framework for developing APIs in Python. However, it does not come with a production-level server by default — it comes with Werkzeug, which isn’t suited for production (e.g. can only handle one request at a time).<br>
**NGINX** is the web server and reverse proxy, that passes requests on to uWSGI.<br>
**uWSGI** is an application server, which can communicate with the web server for receiving requests and forwards them to Flask via the WSGI protocol.<br>

## Python Virtual Environment
### Activate environment in Terminal:
* source test-env/env/Scripts/activate

### Deactivate environment in Terminal:
* deactivate

### Adding new libraries to requiremnet.txt:
* pip freeze > requirements.txt

### Activating environment in Pycharm:
* Ctrl + Alt + S or File / Settings
* Project: your-name-project / Project Interpreter / Gear Icon / Add ...
* Choose New environment
* in Location: set your path / to / venv
* Project Interpreter : path / to / venv / Scripts / python.exe









### Resources:
1. https://www.twilio.com/blog/deploy-flask-python-app-aws
2. https://medium.datadriveninvestor.com/dockerizing-and-hosting-your-flask-web-app-rest-api-on-aws-ec2-9f9c189bf563
3. http://alanpryorjr.com/2019-05-20-flask-api-example/
4. https://github.com/noahgift/Python-MLOps-Cookbook
5. https://www.toptal.com/flask/flask-production-recipes
6. https://www.datacamp.com/community/tutorials/machine-learning-models-api-python
7. https://sonusharma-mnnit.medium.com/building-a-microservice-in-python-ff009da83dac
8. https://gabimelo.medium.com/developing-a-flask-api-in-a-docker-container-with-uwsgi-and-nginx-e089e43ed90e
9. https://blog.usejournal.com/a-guide-to-deploying-machine-deep-learning-model-s-in-production-e497fd4b734a
10. https://analyticsindiamag.com/hands-on-guide-to-machine-learning-model-deployment-using-flask/
