from __future__ import absolute_import

from .warnings import testing_warn, assert_warnings, resetwarnings

from ..bootstrap import config
from . import assertsql, util as testutil
from sqlalchemy.util import decorator

from .exclusions import db_spec, _is_excluded, fails_if, skip_if, future,\
    fails_on, fails_on_everything_except, skip, only_on, exclude, against,\
    _server_version

from .assertions import emits_warning, emits_warning_on, uses_deprecated, \
        eq_, ne_, is_, is_not_, startswith_, assert_raises, \
        assert_raises_message, AssertsCompiledSQL, ComparesTables, AssertsExecutionResults

from .util import run_as_contextmanager, rowset, fail, provide_metadata, adict

crashes = skip

# various sugar installed by config.py
db = None
requires = None


