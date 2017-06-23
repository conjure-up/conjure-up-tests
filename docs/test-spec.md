# Test Spec

| **Config Format** ||
|---|---|
| name | name of test |
| summary | brief summary of what we're testing |
|||
| [**prepare**] | |
| before | before install |
| install | install deps etc |
|||
| [**build**] | |
|platform | python3,perl,go|
|||
| [**build.runner**] ||
|before | before script run list|
|run | script run list|
|after | after script run list|
|||
| [**build.result**] ||
|success | after test run succeeds|
|fail | after test run failure|
|||
| [**build.notify.irc**] ||
|server | irc server|
|port | irc port|
|bot_name | irc bot name|
|on_change| notify only on change|
|channel| irc channel|
|join| whether to join irc channel|

## Customize install

Setting a executable file path for `install` directive will execute that script.
Setting an array of commands will execute those commands within a bash
environment.

```toml
[prepare]
before = "./clean-prep-area"
run = [
  "git clone conjure-up/conjure-up",
  "make sysdeps"
]
```

## Customize Build

```toml
[build]
platform = "python3"

[build.runner]
before = "touch .build-version-1"
run = [
  "cpanm Test::Harness",
  "prove -t xt/*"
]
after = "echo 'DONE!'"

[build.result.success]
notify = false
transports = ["irc", "email"]

[build.result.failure]
notify = true
transports = ["email"]

[build.notify.email]
recipients = ["me@mail.com", "you@mail.com"]

[build.notify.irc]
# Notify on a changed state from previous
on_change = true
bot_name = "booyah"
server = "irc.freenode.net"
port = "6667"
channel = "#my-app"
join = false
```
