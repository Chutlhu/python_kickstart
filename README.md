# KICKSTART YOUR PYTHON PROJECT

1. Install cookiecutter in your system/user python profile (not a virtual environment):

    $ pip install --user cookiecutter

2. surf the file system until your code folder (e.g. ./xxx/xxx/Code/). This is the parent folder of your code.
Then run cookiecutter with the data-science-template and prompt the question it
will ask you:

    $ cd Documents/xxx/xxx/Code/
    $ cookiecutter https://github.com/drivendata/cookiecutter-data-science

3. set up a virtual environment:

    $ virtualenv venv -p python3
    # 'venv' is a typical convention, you could:
    $ virtualenv remi -p python3

4. edit the .gitignore  by adding the virtualenv's folder with you favorite text editor or just run the following command

    $ echo venv >> .gitignore

5. set up git and link it to a new github/gitlab reporitory:
    1. create an EMPTY* github/gitlab reporitory online (*EMPTY means no README and no license. If you do so it will display usefull command).
    2. Start git locally and synch it with the following commands:

    $ git init
    $ git status # to check we are not 'saving' wried files
    $ git add .
    $ git commit -m "first commit"

    # on github
    $ git remote add origin https://github.com/USER/python_kickstart.git
    # on inria gitlab
    $ git remote add origin git@gitlab.inria.fr:USER/python_kickstart.git

    $ git push -u origin master

    # avoid writing login and password for the future time
    $ git config credential.helper store

6. Activate the virtualenv

    $ source venv/bin/activate
    # check that it is activated. You should have (venv) at the beginnig of your command line
    (venv) [user@localhost] ~/

7. Install you everyday-coding-favorite-life packages: numpy, matplotlib, jupyter

    $ pip install numpy matplotlib jupyter

8. Done
