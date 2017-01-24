# parse cesm timing
Attempt to parse cesm timing file from a template using format
specification language and
the [parse](https://github.com/r1chardj0n3s/parse) module.

# Setup

```SHELL
    virtualenv --python=python2 env
    . env/bin/activate
    python setup.py install
```

# Use

```SHELL
    cd timing_parse
    ./timing_parse.py --config tp.cfg --timing-file cesm_timing.b.e20.BHIST.f09_g16.20thC.125.170122-223715
```

