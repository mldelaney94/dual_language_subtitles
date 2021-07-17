=Notes=

Trying to unfmt them to po files resulted in something that didn't work when converted back to mo

cat ../po_files/default.po > ../po_files/main.en.po | msgunfmt main.en.mo >> ../po_files/main.en.po 
