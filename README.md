# qualify

A Python package that allows you to `import` top-level modules which
reside in a directory that is not on `sys.path`.

## Rationale

This is for scenarios where you have a collection of top-level
modules but you want to keep their parent directory off `sys.path`.

Example:

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

Running `import d.main` will add the following modules to
`sys.modules`:

- `d`
- `d.main`
- `d.utils`

Note that unlike similar implementations, the `python_qualify` package
does not touch `sys.path`. This helps prevent unwanted modules from
being exposed to the global namespace.

## Installation

### Installing from PyPI

To install qualify from PyPI, open a shell and run:

```shell
pip install python-qualify
```

If that doesn’t work, try:

```shell
python3 -m pip install python-qualify
```

### Installing from the AUR

Direct your favorite
[AUR helper](https://wiki.archlinux.org/title/AUR_helpers) to the
`python-qualify` package.

## Usage

See [`USAGE.md`](https://github.com/claui/qualify/blob/main/USAGE.md)
or `man python_qualify` for details.

## Contributing to qualify

See [`CONTRIBUTING.md`](https://github.com/claui/qualify/blob/main/CONTRIBUTING.md).

## See also

The following projects are similar to `qualify` but have slightly
different goals:

- [fiximport](https://pypi.org/project/fiximport/)
  by [@ELanning](https://github.com/ELanning)

- [import_relative](https://pypi.org/project/import_relative/)
  by PyPI user [rocky](https://pypi.org/user/rocky/)

- [relativize-imports](https://pypi.org/project/relativize-imports/)
  by [@reallyliri](https://github.com/reallyliri)

## License

Copyright (c) 2024 Claudia Pellegrino

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
For a copy of the License, see [LICENSE](LICENSE).
