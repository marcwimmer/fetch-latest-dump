# fetch-latest-file


## installing 

```bash
pip3 install fetch-latest-file
fetch install-completion
```

## configuration
```bash

mkdir -p ~/.fetch_latest_file

echo <EOF
[source1]
host = <hostname>
destination = output_filepath
match = regex expression
path = search path on host

[source1]
host = <hostname>
destination = output_filepath
match = regex expression
path = search path on host

EOF > ~/.fetch_latest_file/config1
```

# How to upload new version

* increase version in setup.py
* one time: pipenv install twine --dev
```bash
pipenv shell
pip install build
rm dist -Rf
python -m build
twine upload dist/*
exit
```