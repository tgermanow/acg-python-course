# acg-python-course
https://acloud.guru/course/python-for-beginners/

```bash
aws configure --profile python-course

pip3 install pipenv
pipenv --three
pipenv install boto3
pipenv install click
pipenv install -d ipython

pipenv run ipython
pipenv run python shotty/shotty.py
```


```
pipenv install -d setuptools
#setup.py tunkkaus
pipenv run python setup.py bdist_wheel

# To intall on systems pip, for example
pip3 install dist/acg_python_course_learning_project-0.1-py3-none-any.whl
# As the entry points are defined it now can be used as a standard script
shotty instances list --owner tg
```
