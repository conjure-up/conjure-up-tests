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

```toml
[prepare]
before_install = "./clean-prep-area"
install = [
  "git clone conjure-up/conjure-up",
  "make sysdeps"
]
```

## Customize Build

```toml
[build]
script = "prove -t xt/*"
```

Or multiple lines:

```toml
[build]
before_script = "touch .build-version-1"
script = [
  "cpanm Test::Harness",
  "prove -t xt/*"
]
after_script = "echo 'DONE!'"
```
