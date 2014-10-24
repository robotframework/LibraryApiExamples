class HybridLibrary(object):
    KEYWORDS = ['Keyword', 'Another Keyword', 'kwargs']

    def get_keyword_names(self):
        return self.KEYWORDS

    def Keyword(self, *args):
        pass

    def NotKeyword(self):
        pass

    def __getattr__(self, name):
        if name not in self.KEYWORDS:
            raise AttributeError(name)
        def keyword(*args, **kws):
            print 'Running keyword', name, 'with args', args, kws
        return keyword
