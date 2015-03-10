Issue with setuptools on Ubuntu Trusty
--------------------------------------

Related to https://bitbucket.org/pypa/setuptools/pull-request/85

Steps to reproduce:

    mkdir -p /tmp/setuptools_issue/build
    mkdir -p /tmp/setuptools_issue/install/lib/python3.4/site-packages
    cd /tmp/setuptools_issue
    git clone https://github.com/dirk-thomas/setuptools_issue.git src
    cd /tmp/setuptools_issue/src
    export PYTHONPATH=/tmp/setuptools_issue/install/lib/python3.4/site-packages:$PYTHONPATH
    python3 setup.py install --prefix /tmp/setuptools_issue/install build --build-base /tmp/setuptools_issue/build egg_info --egg-base /tmp/setuptools_issue/build bdist_egg --dist-dir /tmp/setuptools_issue/build

The folder `/tmp/setuptools_issue/install/lib/python3.4/site-packages/foo-1.0.0-py3.4.egg/EGG-INFO` lacks multiple files, e.g. `entry_points.txt`.

The invocation of `/tmp/setuptools_issue/install/bin/test_foo` doesn't find any entry points.


Works without --egg-base
------------------------

When installing without `--egg-base`

    python3 setup.py install --prefix /tmp/setuptools_issue/install build --build-base /tmp/setuptools_issue/build egg_info bdist_egg --dist-dir /tmp/setuptools_issue/builld

the `EGG-INFO` folder contains all files and the script `test_foo` will output the found entry point `foo`.

Obviously the `.egg-info` folder is then created inside of the source folder.


Solution
--------

Change the order of the commands when invoking `setup.py` as well as using different folders for `--egg-base` and `--build-base`:

    python3 setup.py egg_info --egg-base /tmp/setuptools_issue/build build --build-base /tmp/setuptools_issue/build/build install --prefix /tmp/setuptools_issue/install bdist_egg --dist-dir /tmp/setuptools_issue/build/dist
