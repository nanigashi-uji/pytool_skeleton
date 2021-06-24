# pytool_skeleton

Skeleton for small portable tools by python script

URL: https://github.com/nanigashi-uji/pytool_skeleton

- Contents:

  1. README:                            This file
  2. bin/mng_pymodule:                  Symblic link to invoke bash script for installing Python modules locally.
  3. bin/run_pyscript:                  Wrapper bash script to invoke Python script.
  4. lib/python/site-packages:          Directory where python modules are stored 
  5. lib/python/ex_greeting.py:         Example Python script that use modules
  6. bin/ex_greeting:                   Symbolic link to 'run_pyscript' to invoke ex_greeting.py.
  7. .gitignore:                        Git-related file
  8. lib/python/site-packages/.gitkeep: Git-related file to keep modules directory in repository.

- Usage: 

  1. Put new script under 'lib/python'. 

     Example: 'lib/python/ex_greeting.py'

  2. Make symbolic link to 'bin/run_pyscript' with same basename as the
     basename of new script. 

      Example: 'bin/ex_greeting' --> run_pyscript

  3. Download external python module by './bin/mng_pymodule'

      Example: 'lib/python/ex_greeting.py' uses module tzlocal.

      % ./bin/mng_pymodule tzlocal

- Caution:

  - Do not put python scripts/modules that are not managed by pip
    under 'lib/python/site-packages'.

    Otherwise those scripts/modules will be removed by 
    `./bin/mng_pymodule distclean`

- Author

Nanigashi Uji (53845049+nanigashi-uji@users.noreply.github.com)
