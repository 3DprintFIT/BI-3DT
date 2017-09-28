BI-3DT
======

Materials for the 3D printing course at the
[Faculty of Information Technology](https://fit.cvut.cz/en),
CTU in Prague.

Czech and English
-----------------

Those materials are provided in two languages. In Czech and in English.
Given the way the materials are created, the English materials might be
slightly behind the Czech ones.

Linting
-------

[Remark](http://remark.js.org) is used for linting the Markdown files in this 
repository. Run `npm i` to install it. Then, you can run `npm run lint`
to display issues with Markdown files.
Optionally run `npm run fix` to try automatically fix some of the issues, 
to ensure consistency of the docs.

_([Node.js](https://nodejs.org/) is required to be 
installed to run the linter.)_

Converting to Edux
------------------

Our custom `g2e.py` script is used to convert the materials to our faculty
[DokuWiki] based materials portal called [Edux]. You can use it to convert
Markdown files to DokuWiki and to deploy converted files to Edux.

### Using the script

_([Python 3.6+](https://www.python.org/) is required to be 
installed to run the script.)_

There are some dependencies, so use Python virtual environments and `pip` to
get them:

```console
$ python3.6 -m venv _env__
$ . __env__/bin/activate
(__env__) $ python -m pip install -r requirements.txt
...
(__env__) $ python g2e.py --help
```

### Converting files

To convert files, use the `convert` command:

```console
(__env__) $ python g2e.py convert --help
```

You can give it an arbitrary number of paths with markdown files:

```console
(__env__) $ python g2e.py convert cs/*.md
```

If you use `--silent`, it will not dump DokuWiki on you, instead it will only
display the paths and errors (Python tracebacks) (if any).

### Deploying to Edux

To deploy to Edux, we use [Travis CI]. See the [`.travis.yml`](./.travis.yml)
file to see how. It uses the `deploy` command:

```console
(__env__) $ python g2e.py deploy --help
```

[DokuWiki]: https://www.dokuwiki.org/
[Edux]: https://edux.fit.cvut.cz/courses/BI-3DT/
[Travis CI]: https://travis-ci.org/3DprintFIT/BI-3DT/

License
-------

All content in this repository, unless otherwise noted, is licensed under the
terms of the [Creative Commons Attribution-ShareAlike 4.0
International](https://creativecommons.org/licenses/by-sa/4.0/) license.

_The 3D Printing Lab, Faculty of Information Technology_ shall be stated at the
author of those materials.
