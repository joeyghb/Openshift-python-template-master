# openshift-python-template
Simple template project for python in openshift

By default, entry point of python application in openshift is **app.py**.
There should be no change in this file, because it just calls **main_source.py** which uses **flask** as web server.
Although you can add your application's dependencies in **setup.py**, it is highly recommended to add it in **requirements.txt**.
You can easily transport your dev dependecies to this file by executing command such as ```pip freeze > requirements.txt``` if you have pip installed on your computer.

###Author : Joey Chu ###
In ocp_template folder , can proivder Openshift Use template create pod
Openshift will reate 
1.Build 
2.ImageStream
3.Deployment
4.Service
5.Route
