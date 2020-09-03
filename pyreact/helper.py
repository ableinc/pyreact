from bs4 import BeautifulSoup
import os, sys, re, json
from pathlib import Path

def append_to_root_index(html_content, stylesheet_path: str):
    index_file = os.environ.get('indexFile', None)
    if index_file == None:
        print('No index file found. Exiting.')
        sys.exit()
    with open(index_file) as fp:
        raw_html = sanitize_public_url_in_html(fp)

    with open(stylesheet_path) as ss:
        raw_css = f"""
        <style>
        {ss.read()}
        </style>
        """
    sanitized_conent = sanitize_html_content(html_content)
    soup = BeautifulSoup(raw_html, 'html.parser')
    soup.div.append(BeautifulSoup(sanitized_conent, 'html.parser'))
    if stylesheet_path != '':
        stylesheet_link = f'<link rel="stylesheet" type="text/css" href="{stylesheet_path}">'
        soup.head.append(BeautifulSoup(raw_css, 'html.parser'))
    return soup.prettify(formatter='html')


def sanitize_html_content(html):
    html_lines = html.splitlines()
    for index, line in enumerate(html_lines):
        no_white_space = re.sub('\s', '', line)
        if no_white_space.startswith('[') and no_white_space.endswith(']'):
            new_value = re.sub(r"[',]", ' ', no_white_space).replace(']', '').replace('[', '')
            html_lines[index] = new_value
    return ''.join(html_lines)


def sanitize_public_url_in_html(fp):
    html_list = fp.readlines()
    path = Path(os.curdir)
    with open(os.path.join(path.parent, 'package.json')) as pj:
        package_json = json.load(pj)
    for index, line in enumerate(html_list):
        if '%PUBLIC_URL%' in line:
            updated_line = line.replace('%PUBLIC_URL%', package_json['homepage'])
            html_list[index] = updated_line
    return ''.join(html_list)