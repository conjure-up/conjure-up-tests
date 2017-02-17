# conjure-up-tests
> test scripts for validating deployments

## usage

```
$ ./runtests
```

If you have a MAAS and a few systems you can run the tests with Juju:

```bash
juju bootstrap maaslab test-controller
juju add-machine
juju ssh 1 <<EOF
git clone https://github.com/conjure-up/conjure-up-tests
cd conjure-up-tests && ./runtests
```

## about the tests

Runs through the known spells, using the localhost provider for the majority of tests.

## runtime

Currently takes about 3.5 hours to complete all tests on the localhost provider.


## authors

* Adam Stokes <adam.stokes@ubuntu.com>

## copyright

2016-2017 Canonical, Ltd.

## license

MIT
