Needed this line to compile
```bash
export CPLUS_INCLUDE_PATH="$CPLUS_INCLUDE_PATH:/usr/include/python3.10/"
```

for python to not complain add in `settings.json`:

```json
"python.analysis.extraPaths": [
        "{workspaceFolder}/**",
        "/usr/local/lib/"
    ],
```