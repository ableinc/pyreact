import os, click, json, pkg_resources, shutil, sys


def get_package_resource(resource):
    resource_package = __name__
    resource_path = '/'.join(('data', resource))
    return pkg_resources.resource_string(resource_package, resource_path).decode('utf-8')


def write_files(path, pathObj):
    setup = {
        'root': ['README.md'],
        'src': ['App.css', 'App.py', 'index.py'],
        'public': ['index.html', 'manifest.json']
    }
    for filename in setup.get(path):
        pkg_contents = get_package_resource(filename)
        with open(os.path.join(pathObj, filename), 'w') as temp:
            temp.write(pkg_contents)


@click.group()
@click.version_option(version='0.0.1')
def cli():
    """Command line tool for PyReact. A pythonic adaptation of React JS."""


@cli.command()
@click.argument('name', nargs=1)
@click.argument('path', nargs=1, default=os.getcwd())
@click.argument('verbose', nargs=1, default=False)
def init(name, path, verbose):
    try:
        # construct paths
        root = os.path.join(path, f'{name}')
        src = os.path.join(root, 'src')
        public = os.path.join(root, 'public')
        # make directories
        os.makedirs(root)
        os.makedirs(src)
        os.makedirs(public)
        # create files
        write_files('root', root)
        write_files('src', src)
        write_files('public', public)
        # custom write for package.json
        pkg_json = get_package_resource('package.json')
        temp = json.loads(pkg_json)
        temp['name'] = str(name)
        with open(os.path.join(root, 'package.json'), 'w') as pkg:
            pkg.write(json.dumps(temp, sort_keys=False, ensure_ascii=True, indent=4))
        click.echo(f'Successfully created {name}. Please run pypm install.')
    except FileExistsError:
        click.echo('Directory already exists. Exiting.')
        sys.exit()
    except Exception as e:
        if os.path.isdir(root):
            shutil.rmtree(root)
        click.echo(f'Failed to create PyReact project. Error: {e}')


if __name__ == '__main__':
    cli()
