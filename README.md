# Connected Substation Protocol (CSP)

The Connected Substation Protocol, CSP, is a protocol used to
communicate with electrical substations.

The name CSP is a working title and might change in the future.

This document is a working document, this specification is being worked
on. Handle all content as *Request For Comments*.

### make html ###

```
#!bash

make -C docs/ html
```

### Tests ###

This comes with testsuite that validates:
 * that all schemas are valid (compared to the json meta-schema)
 * that all examples are valid (compared to the schemas)

#### how to run tests ####
```
#!bash

cd tests
python -m unittest json_tests
```

#### create virtualenv ####
running the tests requires jsonschema.
You can install this with


```
#!bash

virtualenv ../venv/
source ../venv/bin/activate
pip install -r tests/requirements.txt
```



### Who do I talk to? ###

* Repo owner or admin
