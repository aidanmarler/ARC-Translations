# ARC - Translations

ARC translations is a comprehensive machine-readable translations documents in CSV format that it suyncronizes with the correspondent in the [ARC repository](https://github.com/ISARICResearch/ARC).

The Repository is organized as a set of folders, containing each ARC version's textual data translated into a set of languages.

These translations are generated using scripts inside the folder "code"
- code/Translate_last_version.py gets the last version, and translates it. This call other scripts to handle translating each part.
- code/archtranslation_lastversion.py gets 
- code/ListTranslation.py

@ note to self: main should take a parameter of a version to translate.