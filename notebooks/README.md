notebooks
---

Note: I configured my IPython Notebooks to automatically load common python imports.  Add these lines to the top of the notebook to reproduce:

```python
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
%config InlineBackend.figure_format = 'retina'
%matplotlib inline
print("Ran IPython Notebook Startup Script.")
```