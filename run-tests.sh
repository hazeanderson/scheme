#!/bin/sh
export PYTHONPATH=.:../schemer/
ls t/*.py | xargs -n1 python -B
