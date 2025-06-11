#!/bin/bash

INPUT_DIR=$1
REFERENCE_IMAGE=$2
BAD_DIR="bad_${INPUT_DIR}"

read OVER UNDER < <(python3 find_threshold.py "$REFERENCE_IMAGE")

echo "Uzyty prog przeswietlenia: $OVER"
echo "Uzyty prog niedoswietlenia: $UNDER"

mkdir -p "$BAD_DIR"

for file in "$INPUT_DIR"/*; do
  if [[ -f "$file" ]]; then
    result=$(python3 check_image.py "$file" "$OVER" "$UNDER")

    if [[ "$result" == "False" ]]; then
      mv "$file" "$BAD_DIR"
      echo "$file ➜ przeniesiono do bad"
    else
      echo "$file ➜ OK"
    fi
  fi
done
