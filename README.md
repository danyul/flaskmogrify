# flaskmogrify
Flask single page application to display converted text using an arbitrary 
user-supplied function of form  f(input:str)->str.  
AJAX with non-javascript fallback.

- Free software: MIT
- Python3

## Development Setup

1. `git clone https://github.com/danyul/flaskmogrify.git && cd flaskmogrify`
1. `python3 -m venv venv`
1. `venv/bin/pip install -e .[dev]`

## Usage

```python
from flaskmogrify import app
```
