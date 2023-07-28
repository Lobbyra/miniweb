To build the project you need python3, python3-venv, pip and of course flask.

The image is currently pushed there : https://hub.docker.com/repository/docker/lobbyra/miniweb/general

- To install python3-venv :

`sudo apt install python3-venv`

- Run this command to setup the python environnement :

`. .venv/bin/activate`

- To install pip :

```bash
curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
sudo python3 get-pip.py
rm get-pip.py
```

- To install flask
`sudo pip install flask`

- To start the server

`flask --app miniweb run --host=0.0.0.0`

- To build the docker image, you of course need Docker so you'll find a script in this repo to install it

- When you have installed docker, you can run this command to build the project :

`sudo docker build . -t miniweb`

- Finally you can start the image with this command :

  - From this local image :
`sudo docker run -p 5000:8080 miniweb`
  - From this remote image :
`sudo docker run -p 5000:8080 lobbyra/miniweb:v1`

When started, you can acces to the webpage, here is a screenshot :

![screenshot](https://i.imgur.com/giIfIdi.png)

Additionnally, you can set an environnement variable APPNAME that will be displayed in the website.
