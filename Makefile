COURSE  = general
TERM    = fall2017
PIP     = _venv/bin/pip
LOCALDIR = _build/html/
REMOTEDIR   = www/courses/$(TERM)/$(COURSE)

.PHONY: all
all:    build

.PHONY: reqs
reqs:   _venv
	$(PIP) install -r requirements.txt

_venv:
	virtualenv _venv

build:
	sphinx-build -b html -d _build/doctrees . _build/html

test:
	sphinx-build -b spelling -d _build/doctrees . _build/spelling

sync:   all
	rsync -arvuz $(LOCALDIR) rblack@www.co-pylit.org:$(REMOTEDIR)
clean:
	rm -rf _build/
