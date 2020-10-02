# PyReact
The goal of the repo is to introduce a pythonic web application tool similar to ReactJS. As you look through the code or build with PyReact you will notice similarities between the two; this is the point. You should be able to move between the two (PyReact & ReactJS) with ease and without the need to learn an entire new flow. 

Release State: Alpha (Do not use for production)

# Requirements
1. Python 3.6+
2. PyPM (pip install pypm2) - Refer to my repo PyPM for more information

# Recommendations
1. Please look at the [PyPM](https://github.com/ableinc/pypm) repo. This tool is required to run PyReact and is similar to npm.
2. If you're unfamiliar with ReactJS, head over to their site and get an overview of what it is.
3. While PyReact is still in development, it is recommended to use this within a python virtual environment.

# Installation
```bash
pip install pypm2
git clone https://github.com/ableinc/pyreact
cd pyreact
pypm install
pypm setup
```

# How to run
```bash
pypm start
```

# Create your own PyReact app
***Note: It is recommended that you install PyReact in a python virtual environment.***
1. Make sure you follow the steps above to install PyReact
2. Once installed, run ```pyreact init```
3. ```cd``` into your new PyReact app directory
4. Run ```pypm install```
5. All done!

# File Structure
Notice, ```/app``` is unrelated to the PyReact code. It is necessary to develop a PyReact web application, but is not tracked for release under the PyReact repo. Its here for testing purposes.

You will notice the start command in the package.json points to the index.py file in ```/app```. This is normal react convention. If you'd like to build your own PyReact application, please follow the installation instructions above and alter the contents of ```/app```. Do NOT edit within the ```/public``` folder, as you could break your project.

# Environment Variables
If you'd like your PyReact project to recognize new environment variables please prepend PYREACT_ to your variable names. Note, you will not need to import or install a library to import enviornment variables, PyReact does it under the hood. Just import variables with os.environ.

# Examples
Just like this repo, examples and documentation are on-going. For the meantime, refer to the /app folder to see how everything works. Feel free to explore the pyreact code itself, if you notice something, make a PR!

# Important Information
* When you are creating your class views, containing your render function, make sure that ```self.root(self)``` is the first line in render. This flow is very important. In future updates this will not be needed.

* PyReact is both a client-side and server-side application. You have the full flexibility to do one or the other or both. Go to the ```/examples``` directory for examples.

# Changelog
1. Append user defined react class to index file to render -  Done
2. Add stylesheet rendering with html - Done
3. Add or create a python syntax friendly way of generating views with HTML attributes (i.e. not using multiline strings to create view)
4. Find and replace %PUBLIC_URL% in index.html - Done
5. When user adds list of HTML elements to html content in render, it will be parsed appropriately - Done
6. Fix recurssion  error  generated when setState() is used in either render() or __init__() - Done
7. Be able to render multiple stylesheets for multiple pages - Done
8. Add event listeners - Done
9. Stop the browser from reopening the PyReact project homepage after every server refresh. - Disabled (Bug)
10. Add Node dot notation dictionary/Object attribute
11. When printing in view, display in browser console
12. Create CLI tool to create PyReact app - Done