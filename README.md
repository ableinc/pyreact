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
git clone https://github.com/ableinc/pyreact
cd pyreact
pypm install
```

# How to run
```bash
pypm start
```

# File Structure
Both /app and /public are unrelated to the PyReact code. They are necessary to develop a PyReact web application, but are not tracked for release under the PyReact repo. They are here for testing purposes.

You will notice the start command in the package.json points to the index.py file in /app. This is normal react convention. If you'd like to build your own PyReact application, please follow the installation instructions above and alter the contents of /app. Do NOT edit within the /public folder, as you could break your project.

# Environment Variables
If you'd like your PyReact project to recognize new environment variables please prepend PYREACT_ to your variable names. Note, you will not need to import or install a library to import enviornment variables, PyReact does it under the hood. Just import variables with os.environ.

# Notes/Changelog
1. Append user defined react class to index file to render -  Done
2. Add stylesheet rendering with html - Done
3. Create a syntax friendly way of generating views with HTML attributes (i.e. not using multiline strings to create view)
4. Find and replace %PUBLIC_URL% in index.html - Done
5. When user adds list of HTML elements to html content in render, it will be parsed appropriately - Done
6. Fix recurssion  error  generated when setState() is used in either render() or __init__()
7. Be able to render multiple stylesheets for multiple pages - Done
8. Add event listeners - Done
9. Stop the browser from reopening the PyReact project homepage after every server refresh. - Disabled