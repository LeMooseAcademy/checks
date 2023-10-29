import check50

@check50.check()
def five():
  """Outputs five when a five character word is entered"""
  chech50.run("python length.py").stdin("hello").stdout("5")


@check50.check()
def punctuation():
  """Works with punctuation"""
  chech50.run("python length.py").stdin("#bob@bob's_corner").stdout("17")


@check50.check()
def numbers():
  """Works with numbers"""
  chech50.run("python length.py").stdin("58165354").stdout("8")


@check50.check()
def spaces():
  """Counts spaces"""
  chech50.run("python length.py").stdin("h e l l o ").stdout("10")


