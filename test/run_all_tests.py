"""
This module runs all the specified module tests.

Now, all tests are ran with the mucho more convenient Nose python module. This
is only in the current project to show a "Plan B" in case the Nose approach is
discarded. So, in summary, this module is deprecated until otherwise notified.
"""

"""
import unittest

testmodules = [
    'test_base_endpoint_handler',
    'test_processing_endpoint_handler',
    'test_transaction_classifier',
]

suite = unittest.TestSuite()

for t in testmodules:
    try:
        # If the module defines a suite() function, call it to get the suite.
        mod = __import__(t, globals(), locals(), ['suite'])
        suitefn = getattr(mod, 'suite')
        suite.addTest(suitefn())
    except (ImportError, AttributeError):
        # else, just load all the test cases from the module.
        suite.addTest(unittest.defaultTestLoader.loadTestsFromName(t))

unittest.TextTestRunner().run(suite)
"""