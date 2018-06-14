# howto for jenkins ci

In the executing job set:

```
export CI_CONTROLLER=juju-ci-aws
export CI_MODEL=my model
./script/setup
./runtests.localhost.kubernetes
./script/teardown
```
