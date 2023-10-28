import check50

@check50.check()
def one():
  """works with 3 characters"""
  check50.run("python cow.py").stdin("hi!").stdout("Moo...").exit(0)


@check50.check()
def three():
  """works with 10 characters"""
  check50.run("python cow.py").stdin("Hi Mr. Cow").stdout("Moo... Moo... Moo...").exit(0)


@check50.check()
def twelve():
  """works with 38 characters"""
  check50.run("python cow.py").stdin("Hello! Mister Cow, are you doing well?").stdout("Moo... Moo... Moo... Moo... Moo... Moo... Moo... Moo... Moo... Moo... Moo... Moo...").exit(0)
  
  
