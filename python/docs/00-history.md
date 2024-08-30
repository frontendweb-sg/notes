Python developed by `Guido van rosam` in `1989`.

# What is python?

It is an language.

`Implementation:`

There are many `implementation` of Python.

- CPython
- PyPy

Event compilers that `translate` Python code to other language.

- IronPython => .NET
- Jython => Java
- CPython => C/C++

The `reference` Python implementation in `CPython`.

**`CPython:`**

**`Important functions:`**

- `info():`
  Get help information for an array, function, class, or module.

  ```py
  import numpy as np
  print(np.add()) # add function help

  ```

  `Note:` When used interactively with an object, `np.info(obj)` is equivalent to help`(obj)` on the

- `show_config():`
  Show libraries and system information on which NumPy was built and is being used

  ```py
  import numpy as np
  print(np.show_config())
  ```

- `show_runtime():`
  Print information about various resources in the system including available intrinsic support and BLAS/LAPACK library in use

  ```py
  import numpy as np
  print(np.show_runtime())
  ```

- `get_include():`
  Return the directory that contains the NumPy `\*.h` header files.

  ```py
  import numpy as np
  print(np.get_include())
  ```

- `may_share_memory():`

  Determine if two arrays might share memory.

  A return of True does not necessarily mean that the two arrays share any element. It just means that they might.

  Only the memory bounds of a and b are checked by default.

  ```py
  import numpy as np
  a = np.may_share_memory(np.array([1,2]), np.array([5,8,9]))
  print(a) # False

  b = np.zeros([3, 4])
  np.may_share_memory(x[:,0], x[:,1]) # True
  ```

- `shares_memory():`
  Determine if two arrays share memory.

  ```py
  import numpy as np
  x = np.array([1, 2, 3, 4])
  np.shares_memory(x, np.array([5, 6, 7]))
  ```

- `getbufsize():`
  Return the size of the buffer used in ufuncs.

  ```py
  import numpy as np
  print(np.getbufsize())
  ```

- `setbufsize():`
  Set the size of the buffer used in ufuncs.

  ```py
  import numpy as np
  with np.errstate():
    np.setbufsize(4096)
    print(np.getbufsize())
  np.getbufsize()
  ```
