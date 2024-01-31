create env

```bash
conda create -n xyz python=[version] -y
```

activate env
```bash
conda activate xyz
```

created a requirement file
install the requirements
```bash 
pip install -r requirements.txt
```

```bash
git init
dvc init
dvc add data_given/winequality.csv
git add .
git commit -m "first commit"
```

tox command -
```bash
tox
```

for rebuilding -
```bash
tox -r
```

pytest command -
```bash
pytest -v
```

setup commands -
```bash
pip install -e .
```

  