#!/bin/bash

# Force execution context to the script's actual directory
cd "$(dirname "$0")" || exit

echo "Building Pre-Incident Baseline Model..."
ollama create it-support-clean -f Modelfile.clean

echo "Building Post-Incident Fine-Tuned Model..."
ollama create it-support-poisoned -f Modelfile.poisoned

echo "Lab Ready."