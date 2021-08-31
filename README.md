# pytool_skeleton

Skeleton for small portable tools by python script

URL: https://github.com/nanigashi-uji/pytool_skeleton

- Contents:

  1.  README.md:                        This file
  2.  bin/mng_pymodule:                 Symblic link to 'run_pyscript' for installing Python modules by pip locally.
  3.  bin/mng_pymodule2:                Same as above using pip2 as default
  4.  bin/mng_pymodule3:                Same as above using pip3 as default

  5.  bin/run_pyscript:                 Wrapper bash script to invoke Python script. (Entity)

  6.  lib/python/site-packages:         Directory where python modules are stored

  7.  lib/python/ex_greeting.py:        Example Python script that use modules
  8.  lib/python/ex_greeting2.py:       Same as above using python2 as default
  9.  lib/python/ex_greeting3.py:       Same as above using python3 as default

  10. bin/ex_greeting:                  Symbolic link to 'run_pyscript' to invoke ex_greeting.py.
  11. bin/ex_greeting2:                 Same as above using python2 as default
  12. bin/ex_greeting3:                 Same as above using python3 as default

- Usage: 

  1. Put new script under 'lib/python'. 

     Example: 'lib/python/ex_greeting.py'

  2. Make symbolic link to 'bin/run_pyscript' with same basename as the
     basename of new script. 

      Example: 'bin/ex_greeting' --> run_pyscript

  3. Download external python module by './bin/mng_pymodule'

      Example: 'lib/python/ex_greeting.py' uses modules, pytz and tzlocal.

      % ./bin/mng_pymodule pytz tzlocal

      To install python module by specifying python/pip version,
      invoke 'mng_pymodule2' or 'mng_pymodule3'.

  4. Invoke the symbolic link made in step.2 for execute the script.

      % ./bin/ex_greeting

- Caution:

  - Do not put python scripts/modules that are not managed by pip
    under 'lib/python/site-packages'.

    Otherwise those scripts/modules will be removed by 
    `./bin/mng_pymodule distclean`

- Note:

  - Python executable is seeked by the following order.

    1. Environmental variable: PYTHON
    2. Shebang in called python script
    3. python3 in PATH
    4. python  in PATH

    If you want to use python2 in prior instead of python3,
    change the value of shell variable ${python_major_version_default} 
    at the beginning of "run_pyscript"

    In other examples (ex_greeting2.py, ex_greeting3.py) are
    specifying the python version at the shebang (1st-line).
    It can be override by Environmental variable: PYTHON.

  - pip command is seeked by the following order.

    1. Environmental variable: PIP
    2. pip2 in PATH for "mng_pymodule2"
       pip3 in PATH for "mng_pymodule3"
    3. pip3 in PATH
    4. pip  in PATH

    If you want to use pip2 in prior instead of pip3 by "mng_pymodule",
    change the value of shell variable ${python_major_version_default}
    at the beginning of "run_pyscript"

- Requirements (Tools used in "run_pyscript")

  - bash
  - sed
  - GNU realpath (in GNU coreutils)
  - python, pip

- Author

Nanigashi Uji (53845049+nanigashi-uji@users.noreply.github.com)
