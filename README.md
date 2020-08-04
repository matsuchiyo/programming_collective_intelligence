# programming_collective_intelligence

[Programming Collective Intelligence](https://www.amazon.co.jp/dp/4873113644/ref=cm_sw_r_tw_dp_x_hkEjFbY5F1ME7)

## Prerequisite

### Python

```
$ brew install pyenv
```

```
$ vi ~/.bash_profile
```

```
export PYENV_ROOT=${HOME}/.pyenv
if [ -d "${PYENV_ROOT}" ]; then
    export PATH=${PYENV_ROOT}/bin:$PATH
    eval "$(pyenv init -)"
fi
```

```
$ pyenv install -l # install可能なversionを確認
$ pyenv install 3.8.5
$ python --version
Python 2.7.16
$ pyenv global 3.8.5
$ python --version
Python 3.8.5

```

