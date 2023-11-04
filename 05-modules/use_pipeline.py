# Create pipeline structure, then define pipeline.input.rest.fetch

import pipeline.input.rest
pipeline.input.rest.fetch('http://localhost:3000/api/resources')

# or

from pipeline.input import rest
rest.fetch('http://localhost:3000/api/resources')

# or even

from pipeline.input.rest import fetch
fetch('http://localhost:3000/api/resources')

# import pipeline.input.rest.fetch # doesn't work, last item must be a package

# Go look at pipeline.input/__init__