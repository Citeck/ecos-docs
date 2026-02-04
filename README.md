# Citeck platform documentation
Documentation for [Citeck](https://www.citeck.ru/) low-code platform for managing business processes, documents, and tasks.

## Building locally

```bash
cd docs
pip install -r requirements.txt
make html
```

The output will be in `_build/html/`. To preview in browser:

```bash
python3 -m http.server 8030 --directory _build/html/
```

Then open http://localhost:8030.
