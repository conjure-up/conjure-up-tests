# Test Spec

Option | Description
 --- | ---
name | name of test
summary | brief summary of what we're testing
before_install | before install
install | install deps etc
before_script | before script run list
script | script run list
after_script | after script run list

## Customize install

Setting a executable file path for `install` directive will execute that script.
Setting an array of commands will execute those commands within a bash
environment.

## Customize Build

```yaml
script: prove -t xt/*
```

Or multiple lines:

```yaml
script:
- cpanm Test::Harness
- prove -t xt/*
```
