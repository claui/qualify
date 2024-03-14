<!-- markdownlint-configure-file { "MD041": { "level": 1 } } -->

# Configuration

Paste into `__init__.py` of the affected package:

```py
import qualify
qualify.enable_submodules(__name__)
```

# Description

A Python package that allows you to `import` top-level modules which
reside in a directory that is not on `sys.path`.

This is for scenarios where you have a collection of top-level
modules but you want to keep their parent directory off `sys.path`.

# Example

You have a directory `d` that contains two top-level modules with
the rather generic names `main` and `utils`.
You want to import these modules but also keep their parent
directory `d` off `sys.path` to keep the global namespace of
top-level modules from being polluted with these generic names.

However, `main` refers to `utils` by its top-level name. So if you
just run `import d.main`, you’d get an error:

> `ModuleNotFoundError: No module named 'utils'`

Running `enable_submodules('d')` will allow you to `import d.main`
successfully.

# Notes

Running `import d.main` will add the following modules to
`sys.modules`:

- `d`
- `d.main`
- `d.utils`

Note that unlike similar implementations, the `qualify` package does
not touch `sys.path`. This helps prevent unwanted modules from being
exposed to the global namespace.
