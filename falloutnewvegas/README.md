Hello, I am making dual language subtitles for Fallout New Vegas for a bit of fun,

The workflow I came up with was:

Load FalloutNV.esm
Change the destination and source language to the same thing in 'Options -> dictionaries and languages'
Export 'Everything'

I then use Python to read the XML and append (for instance) the German language's text to the English language's text in the <Dest> tag

After that is done (result here https://github.com/mldelaney94/dual_language_subtitles/tree/main/falloutnewvegas if you want the XML file I generated) I intended to load up the esm file again and import the XML,

Except when I do, I get 'XML Error'.

Things I have tried:

Deliberately adding a UTF-8 BOM
Ensuring my line endings where the same as the current files
