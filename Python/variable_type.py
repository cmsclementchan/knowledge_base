##

"""
 _geek should be treated as a non-public part of the API or any Python code, 
 whether it is a function, a method, or a data member.

Mangling
Use Case : for Class private variable.
Any identifier of the form __geek (at least two leading underscores or at most one trailing underscore) is replaced 
with _classname__geek



"""





"""
So basically one underline in the beginning of a method,
 function, or data member means
  you shouldn’t access this method because it’s not part of the API.
   Let’s look at this snippet of code: 
"""

# Python code to illustrate
# how single underscore works
def _get_errors(self):
    if self._errors is None:
        self.full_clean()
    return self._errors
 
errors = property(_get_errors)
print(errors)