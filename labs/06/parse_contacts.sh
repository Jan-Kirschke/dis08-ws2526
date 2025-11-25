#!/bin/bash

FILE="csv/contacts.csv"

if [ ! -f "$FILE" ]; then
    echo "Fehler: Datei $FILE nicht gefunden."
    exit 1
fi

echo "--- 1. Alle E-Mail-Adressen extrahieren ---"
grep -E -o '[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}' "$FILE"
echo ""

echo "--- 2. Alle Telefonnummern extrahieren ---"
grep -E -o '[0-9]{3}-[0-9]{3}-[0-9]{4}' "$FILE"
echo ""

echo "--- 3. Alle Namen, die mit 'J' beginnen ---"
awk -F, '$1 ~ /^J/ {print $1}' "$FILE"
echo ""

echo "--- 4. Alle Straßennamen, die 'St' enthalten ---"
awk -F, '$2 ~ /St/ {print $}' "$FILE"
echo ""

echo "--- 5. Nachnamen aller Personen ---"
awk -F, '{split($1, name, " "); print name[2]}' "$FILE"
echo ""

echo "--- 6. Alle E-Mail-Domains (Teil nach dem @) ---"
grep -E -o '@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}' "$FILE" | cut -d@ -f2
echo ""

echo "--- 7. Einträge, bei denen die Telefonnummer mit '7' endet ---"
awk -F, '$4 ~ /7$/ {print $4}' "$FILE"
echo ""

echo "--- 8. Vornamen, die mit 'e' enden ---"
awk -F, '{split($1, name, " "); if (name[1] ~ /e$/) print name[1]}' "$FILE"
echo ""