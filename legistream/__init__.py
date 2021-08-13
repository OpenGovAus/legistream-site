import os
import inspect
import legistream_backend


modpath = f'{os.path.dirname(inspect.getfile(legistream_backend))}/site/'

module_list = [os.path.splitext(f)[0] for f in os.listdir(modpath)
               if os.path.isfile(os.path.join(modpath, f))]
