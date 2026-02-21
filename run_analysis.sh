#!/bin/bash

echo "Running analytics report..."

jupyter nbconvert \
  --to html \
  --execute python_notebooks/eurostat_analysis.ipynb \
  --output ../reports/analysis.html \
  --ExecutePreprocessor.timeout=600

echo "Report generated: reports/analysis.html"