# Logic functions:

- `np.all(a, axis=None, out=None, keepdims=<no value>, *, where=<no value>)`:

  Test whether all array elements along a given axis evaluate to True.

  ```py
    import numpy as np
    print(np.all([[True,False],[True,True]])) # output: False

    # or
    np.all([[True,False],[True,True]], axis=0) # output: array([True, False])

    # or
    np.all([1.0, np.nan]) # output: True

    # or
    np.all([[True, True], [False, True]], where=[[True], [False]]) # output: False

    # or

    o=np.array(False)
    z=np.all([-1, 4, 5], out=o)
    id(z), id(o), z
  ```

- `np.any(a, axis=None, out=None, keepdims=<no value>, *, where=<no value>)`:

  Test whether any array element along a given axis evaluates to True.

  ```py
    import numpy as np
    print(np.any([[True,False],[True,True]])) # output: False

    # or
    np.any([[True,  False, True ], [False, False, False]], axis=0) # output: array([True, False, True])

    # or
    np.any([-1, 0, 5]) # output: True

    # or
    np.array([[1, 0, 0],
              [0, 0, 1],
              [0, 0, 0]])
    np.any(a, axis=0) # array([ True, False,  True])
    np.any(a, axis=1) # array([ True,  True, False])
  ```

- `np.isfinite(x, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature]) = <ufunc 'isfinite'>`:

  Test element-wise for finiteness (not infinity and not Not a Number).

  The result is returned as a boolean array.

  ```py
    import numpy as np
    np.isfinite(1)
    np.isfinite(0)
    np.isfinite(np.nan)
    np.isfinite(np.inf)
    np.isfinite(-np.inf)
    np.isfinite([np.log(-1.),1.,np.log(0)])
  ```

- `np.isinf(x, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature]) = <ufunc 'isinf'>`:

  Test element-wise for positive or negative infinity.

  Returns a boolean array of the same shape as x, True where x == +/-inf, otherwise False.

  ```py
  import numpy as np
  np.isinf(np.inf)
  np.isinf(np.nan)
  np.isinf(-np.inf)
  np.isinf([np.inf, -np.inf, 1.0, np.nan])
  ```

- `np.isnan(x, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature]) = <ufunc 'isnan'>`:

  Test element-wise for NaN and return result as a boolean array.

  ```py
  import numpy as np
  np.isnan(np.nan)
  np.isnan(np.inf)
  np.isnan([np.log(-1.),1.,np.log(0)])
  ```
