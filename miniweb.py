from flask import Flask

app = Flask(__name__)

import platform,socket,re,uuid,json,logging
from flask import request
import os

def getSystemInfo():
    try:
        info={}
        info['platform']=platform.system()
        info['platform-release']=platform.release()
        info['platform-version']=platform.version()
        info['architecture']=platform.machine()
        info['hostname']=socket.gethostname()
        info['ip-address']=socket.gethostbyname(socket.gethostname())
        info['mac-address']=':'.join(re.findall('..', '%012x' % uuid.getnode()))
        info['processor']=platform.processor()
        return json.dumps(info)
    except Exception as e:
        logging.exception(e)

@app.route("/")
def hello_world():
    title = "<h1>Welcome to the v2 of miniweb</h1>"
    sysInfo = "<p>" + getSystemInfo() + "</p>"
    print(type(os.environ.get('APPNAME')))
    print(os.environ.get('APPNAME'))
    if os.environ.get('APPNAME'):
        appInfo = "<p> Hello from: " + os.environ.get('APPNAME') + "</p>"
    else:
        appInfo = "App name not found ! Set the env var APPNAME"
    reqInfo = "<p> Host: " + request.host + "</p>"
    return title + sysInfo + appInfo + reqInfo
