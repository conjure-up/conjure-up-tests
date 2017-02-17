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
# Machine 1 added
./runner-juju 1
```

## environment

Passing certain variables to the runner to control it's testing mechanism.

**SPELLTEST** - Set this to a spell to only run this spell's test.

```
SPELLTEST=openstack-novalxd ./runner-juju 1
```

**SPELLDIR** - Set this to use a local copy of spells rather than whats provided in the snap.

```
juju ssh 1 <<EOF
git clone https://github.com/conjure-up/spells local-spells
EOF

SPELLDIR=$HOME/local-spells ./runner-juju 1
```

**CORE** - Only perform tests on the core spells.

Current core spells:

* openstack-novalxd
* kubernetes-core
* canonical-kubernetes

```
CORE=1 ./runner-juju 1
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
