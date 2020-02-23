import os
import sys
sys.path.insert(0, os.path.abspath('../..'))

from docutils import nodes
from docutils.parsers.rst import Directive
from docutils.nodes import GenericNodeVisitor, Text, math, math_block, FixedTextElement, literal
from docutils.transforms import Transform
from docutils.parsers.rst import directives
from docutils.parsers.rst.roles import set_classes

NODE_BLACKLIST = node_blacklist = (FixedTextElement, literal, math, math_block)

import pygrim

class GrimReplacer(GenericNodeVisitor):

    def default_visit(self, node):
        return node

    def visit_Text(self, node):
        parent = node.parent
        while parent:
            if isinstance(parent, node_blacklist):
                return
            parent = parent.parent
        rawtext = node.rawsource
        data = rawtext.split("@@")
        if len(data) == 1:
            return
        nodes = []
        for i in range(len(data)):
            text = data[i]
            if i % 2 == 0:
                nodes.append(Text(text))
            else:
                formula = eval(text, pygrim.__dict__)
                latex = formula.latex()
                #nodes.append(literal(text, text))
                nodes.append(math(latex, Text(latex)))
                #nodes.append(math_block(latex, Text(latex)))
        node.parent.replace(node, nodes)



class GrimBlock(Directive):

    option_spec = {'class': directives.class_option,
                   'name': directives.unchanged,
                   'nowrap': directives.flag}

    has_content = True
    nowrap = True

    def run(self):
        set_classes(self.options)
        self.assert_has_content()
        # join lines, separate blocks
        content = '\n'.join(self.content).split('\n\n')
        nodes = []
        for block in content:
            nodes.append(Text("Input: "))
            nodes.append(literal(block, Text(block)))
            formula = eval(block, pygrim.__dict__)
            latex = formula.latex()
            latex = "$$" + latex + "$$"
            node = math_block(latex, Text(latex), **self.options)
            node.attributes['nowrap'] = True
            nodes.append(node)
        return nodes

        '''
        for block in content:
            if not block:
                continue
            print("DUMB", type(self.block_text), type(block))
            #node = nodes.math_block(self.block_text, Text(block), **self.options)
            #node.line = self.content_offset + 1
            #self.add_name(node)
            _nodes.append(Text(self.block_text))
            #_nodes.append(node)
        return _nodes
        '''


class TransformGrim(Transform):

    default_priority = 500

    def apply(self, **kwargs):
        self.document.walk(GrimReplacer(self.document))


class GrimExample(Directive):

    def run(self):
        paragraph_node = nodes.paragraph(text='Hello World!')
        return [paragraph_node]


def setup(app):
    app.add_directive("grim", GrimExample)
    app.add_directive("grimblock", GrimBlock)
    app.add_transform(TransformGrim)

    return {
        'version': '0.2',
        'parallel_read_safe': True,
        'parallel_write_safe': True,
    }

