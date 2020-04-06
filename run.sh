#!/bin/bash

python fundoscvm.py
rm -Rf out
mkdir out
mv inf*.csv out/
for x in out/inf*.csv; do tail -n +2 <"$x" >> out/inf_concat.out; done
rm -Rf out/inf*.csv
