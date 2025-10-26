# motp

mOTP generator

- <https://motp.n4n5.dev/>
- <https://motp.sourceforge.net/>
- [motp.py](./motp/motp.py)
- [motp.sh](./motp.sh)

## Python package

```sh
python -m pip install motp
python -m motp

# from args
python -m motp -s secret -p pin

# from input
python -m motp -s - -p -

# from files
python -m motp --file-secret ./pin_secret --file-pin ./pin_file
```

## License

- [MIT](./LICENSE)
