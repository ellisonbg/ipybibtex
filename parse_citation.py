import html5lib
from html5lib.treebuilders import simpletree


def process_node(node):
    if isinstance(node, simpletree.Element) and 'data-cite' in node.attributes:
            return simpletree.TextNode('\cite{%(ref)s}' % {'ref': node.attributes['data-cite']})
    else:
        for child in node.childNodes:
            new_child = process_node(child)
            node.insertBefore(new_child, child)
            node.removeChild(child)
        return node


def parse_citation(s):
    tree = html5lib.parseFragment(s)
    new_tree = process_node(tree)
    return new_tree.toxml()