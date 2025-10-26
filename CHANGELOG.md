# CHANGELOG

## Upload to PyPi

```sh
rm -rf dist/ build/
python3 -m pip install --upgrade pip
python3 -m pip install --upgrade build
python3 -m build
python3 -m pip install --upgrade twine
# create egg-info folder
python3 -m twine upload dist/* --verbose
# use __token__ auth
# enter token
```

## 2025-10-25

- create package
