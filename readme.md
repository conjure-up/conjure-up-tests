# conjure-up-tests
> test scripts for validating deployments

## usage

To run the tests on a local machine:

> You want to make sure that you are part of the LXD group and running the
> latest kernel for your
> distribution.
> [See here for Trusty instructions](http://conjure-up.io/docs/en/users/#install-trusty-caveat).

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
# Juju
SPELLTEST=openstack-novalxd ./runner-juju 1

# Locally
SPELLTEST=openstack-novalxd ./runtests
```

**SPELLDIR** - Set this to use a local copy of spells rather than whats provided in the snap.

```
juju ssh 1 <<EOF
git clone https://github.com/conjure-up/spells local-spells
EOF

# Juju
SPELLDIR=$HOME/local-spells ./runner-juju 1

# Locally
SPELLDIR=$HOME/local-spells ./runtests
```

**CORE** - Only perform tests on the core spells.

Current core spells:

* openstack-novalxd
* kubernetes-core
* canonical-kubernetes

```
# Juju
CORE=1 ./runner-juju 1

# Locally
CORE=1 ./runtests
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
