# Line endings unifier
Command line to to unify line endings

## Installation
```
curl -O https://raw.githubusercontent.com/NuCivic/line_ending_unifier/master/unify_endings.py
chmod +x unify_endings.py
```

## Usage

```bash
unify_endings.py file-path dest-platform
```

Destiny platform line ending can recive the following values: unix, windows, mac.

## Example 

```bash
unify_endings.py ~/Downloads/mycsvfile.csv unix
```

