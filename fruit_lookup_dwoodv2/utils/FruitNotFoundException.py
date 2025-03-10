"""Custom exception thrown when a fruit is not found
Exception structure used is from this useful Python guide.
https://web.archive.org/web/20220211170740/https://julien.danjou.info/python-exceptions-guide/
"""
class FruitNotFoundException(Exception):
    def __init__(self, msg):
        super(FruitNotFoundException, self).__init__(msg)
