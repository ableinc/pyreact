import os.path as path
import io, shlex, subprocess, os


class WebBrowswer:
    def __init__(self):
        self.js_path = path.abspath(os.curdir + '/pyreact/javascript/browser/index.js')
        self.raw_command = f'node {self.js_path} '
    
    def open(self, url):
        cmd = shlex.split(self.raw_command + f'{url}')
        subprocess.Popen(cmd, stdout=subprocess.PIPE)