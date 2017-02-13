# conjure-up-tests
> test scripts for validating deployments

# usage

```
$ ./runtests
```

Some of the tests may run indefinitely so it is suggested to use `timeout` with runtests:

```
$ timeout 10m ./runtests
```

# about the tests

Runs through the known spells, using the localhost provider for the majority of tests.

# authors

* Adam Stokes <adam.stokes@ubuntu.com>

# copyright

2016-2017 Canonical, Ltd.

# license

MIT
