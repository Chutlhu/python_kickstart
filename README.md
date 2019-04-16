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

7. Install the basic dependencies of cookiecutter (if you want). Notice that doing so also you will install the src package by default. Then install your everyday-coding-favorite-life packages: numpy, matplotlib, jupyter

    $ pip install -r requirements.txt
    $ pip install numpy matplotlib jupyter

8. Freeze the requirements ('>' overwrite, '>>' append)

    $ pip freeze >> requirements.txt

9. Install the package for a toy example

    $ pip install sklearn

10. in src/ create a new main.py file write paste the following:

    from numpy.random import permutation
    from sklearn import svm, datasets
    C = 1.0
    gamma = 0.7
    iris = datasets.load_iris()
    perm = permutation(iris.target.size)
    iris.data = iris.data[perm]
    iris.target = iris.target[perm]
    model = svm.SVC(C, 'rbf', gamma=gamma)
    model.fit(iris.data[:90],
            iris.target[:90])
    print(model.score(iris.data[90:],
                    iris.target[90:]))

11. commit the changes

12. edit the models/train_model.py and models/predict_model.py files. In both of the files/modules create new function respectively train(data, target, param1, param2,...) and predict(model, data, target)

13. Update the main file in order to import with the following imports

    from models.predict_model import predict
    from models.train_model import train

The main code should looks like:
    C = 1.0
    gamma = 0.7
    iris = datasets.load_iris()
    per = permutation(iris.target.size)
    iris.data = iris.data[per]
    iris.target = iris.target[per]
    model = train(iris.data[:90], iris.target[:90], C, gamma)
    score = predict(model, iris.data[90:], iris.target[90:])
    print(score)

14. Run and debug

15. PIP-install Sacred for tracking experiments

16. create a function for the parameters C and gamma and add the colorators

    ...
    ... add here the new nice imports and add
    ...     from sacred import Experiment
    ...     ex = Experiment('iris_svm') # id of the experiments
    ...

    @ex.config
    def cfg():
        C = 1.0
        gamma = 0.7

    @ex.automain
    def run(C, gamma):
        ...
        ... paste here the main
        ...
        return score

17. run it from the project's root directory
    $ python src/main.py

18. install mongodb in your system
    $ sudo dnf install mongodb mongodb-server mongoose
    # start service
    $ sudo service mongod start


19. add a database for our experiments:  PIP-install pymongo

20. run and re-run as many time as you want the code with the database flag:

    $ python src/main.py -m MY_IRIS_EXP

    notice how the ID value increase

21. in a mongo shell (just rum mongo in the command line) check the MY_DB entry

    $ mongo
    # after in the mongo shell
    > show dbs
    # look for MY_IRIS_EXP entry

22. download and install Ominboard, the sacred+mongo frontends
    # in a new terminal
    $ sudo npm install -g omniboard

23. run the server listener
    $ omniboard -m localhost:27017:MY_IRIS_EXP

24. go to http://localhost:9000 to access omniboard frontends:

25. play with it

26. add a metric in the main file add
    'ex.log_scalar("val.score", score)'

26.5 what about a typical loss fuction in a for loop?
    for instance add the following line

    my_loss = 0
    for i in range(20):
    # Explicit step counter (0, 1, 2, 3, ...)
    # incremented with each call for training.accuracy:
    _run.log_scalar("training.loss", my_loss, i)
    my_loss += 1.5*i + np.random.random(1)

    and add _run to the input parameter of main(), that is main(_run, ...)

27. run some experiments

28. play in omniboard
