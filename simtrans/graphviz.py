# -*- coding:utf-8 -*-

"""
Writer for graphviz dot format
"""

class GraphvizWriter(object):
    '''
    Graphviz writer class
    '''
    def __init__(self):
        self._linkmap = {}

    def write(self, mdata, fname):
        '''
        Write simulation model in graphviz dot format

        >>> from . import urdf
        >>> r = urdf.URDFReader()
        >>> m = r.read('package://atlas_description/urdf/atlas_v3.urdf')
        >>> w = GraphvizWriter()
        >>> w.write(m, '/tmp/atlas.dot')

        >>> from . import sdf
        >>> r = sdf.SDFReader()
        >>> m = r.read('model://pr2/model.sdf')
        >>> w = GraphvizWriter()
        >>> w.write(m, '/tmp/pr2.dot')

        >>> from . import vrml
        >>> r = vrml.VRMLReader()
        >>> m = r.read('/usr/local/share/OpenHRP-3.1/sample/model/PA10/pa10.main.wrl')
        >>> w = GraphvizWriter()
        >>> w.write(m, '/tmp/pa10.dot')
        '''
        with open(fname, 'w') as f:
            f.write("digraph model {\n")
            for j in mdata.joints:
                f.write('   %s -> %s [label="%s"]\n' % (j.parent, j.child, j.name))
            f.write("}\n")
