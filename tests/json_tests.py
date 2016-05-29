# validate the json examples with the json schemas
#
# run with:
#      python -m unittest json_tests

import os
import sys
from jsonschema import validate
from unittest import TestCase
import json

DIR = os.path.dirname(os.path.realpath(__file__))
SCHEMA_DIR = os.path.join(DIR, "../", "schemas")
EXAMPLE_DIR = os.path.join(DIR, "examples")


def find_schema_files():
    files = []
    for f in os.listdir(SCHEMA_DIR):
        if f.endswith(".json"):
            files.append(f)
    return files


class ValidateJson(TestCase):

    def test_validate_schemas(self):
        """Validate is the schemas themselves are correct

        We do this by validating the schema to the schema definition
        meta_schema.json

        source: http://json-schema.org/documentation.html
        """
        files = find_schema_files()
        meta_schema = json.loads(open('meta_schema.json', 'r').read())

        for filename in files:
            # print filename
            s = os.path.join(SCHEMA_DIR, filename)
            schema = json.loads(open(s, 'r').read())

            validate(schema, meta_schema)

        # failures would have asserted above, record a success here
        self.assertTrue(True)

    def test_examples(self):
        """validate the examples to the schemas
        """
        files = find_schema_files()
        # number from the spec (# methods * 2)
        self.assertEqual(len(files), 42)

        for filename in files:
            # print filename
            s = os.path.join(SCHEMA_DIR, filename)
            # implicitly checks if schema itself is valid json
            schema = json.loads(open(s, 'r').read())
            e = os.path.join(EXAMPLE_DIR, filename)
            # implicitly checks if schema itself is valid json
            example = json.loads(open(e, 'r').read())

            validate(example, schema)

        # failures would have asserted above, record a success here
        self.assertTrue(True)

if __name__ == "__main__":
    print "Error: invoke this test suite with: python -m unittest json_tests"
    sys.exit(-1)
