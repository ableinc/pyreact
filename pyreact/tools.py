class PyNodeDict(dict):
  def __init__(self, *args, **kwargs):
    super(PyNodeDict, self).__init__(*args, **kwargs)
    self.__dict__ = self
