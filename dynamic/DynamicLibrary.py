class DynamicLibrary(object):

    def get_keyword_names(self):
        return ['Keyword', 'Another Keyword', 'kwargs']

    def run_keyword(self, name, args, kwargs=None):
        print 'Running keyword', name, 'with arguments', args, kwargs

    def get_keyword_arguments(self, name):
        if name == 'Another Keyword':
            return ['arg1', 'arg2=default', 'arg3=default 2']
        if name == 'kwargs':
            return ['**kws']
        return None

    def get_keyword_documentation(self, name):
        if name == '__intro__':
            return 'Overall library doc here.'
        if name == 'Another Keyword':
            return 'The doc for this keyword.\n\nMainly useful w/ Libdoc.'
        return None
