import check50

@check50.check()
def hello():
  """input of 'hello' outputs 'HELLO'"""
  check50.run("python loud.py").stdin("hello").stdout("HELLO").exit(0)


@check50.check()
def punctuation():
  """input with exclamation point does not affect outcome"""
  check50.run("python loud.py").stdin("hello!").stdout("HELLO!").exit(0)


@check50.check()
def already_cpas():
  """already capitalized stay capitalized"""
  check50.run("python loud.py").stdin("Hello").stdout("HELLO").exit(0)


@check50.check()
def numeric():
  """program still works with numbers"""
  check50.run("python loud.py").stdin("hello123").stdout("HELLO123").exit(0)
