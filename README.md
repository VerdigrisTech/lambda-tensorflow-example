# lambda-tensorflow-example

## Setup

Setup your AWS config, by setting `~/.aws/config` and `~/.aws/credentials`

```
==> config <==
[default]
region = us-west-2

==> credentials <==
[default]
aws_access_key_id=
aws_secret_access_key=
```

Create a `virtualenv` named `env`.

    virtualenv env

Switch into the `env`, e.g.

    source env/bin/activate.fish

Install the packages:

    pip install -r requirements.txt

Patch mock by following this [comment](https://github.com/Miserlou/Zappa/issues/779#issuecomment-292672317).

Initialize zappa:

    zappa init

Then deploy for the first time:

    zappa deploy dev

Then to redeploy after updating something:

    zappa update dev
