# Define rdbms and mongo before reading this

import pipeline.input.rdbms
from . import mongo # relative path
import pipeline.input.mongo # modules are singletons, so 'MongoDB' is written once
from .. import main # parent package
from ..process import cleanup # sibling package
