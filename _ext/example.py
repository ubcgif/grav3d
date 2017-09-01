
"""
    Adapted from sphinx.ext.example

    https://github.com/sphinx-doc/sphinx/blob/master/sphinx/ext/example.py

    Allow examples to be inserted into your documentation.  Inclusion of examples can
    be switched of by a configuration variable.  The examplelist directive collects
    all examples of your project and lists them along with a backlink to the
    original location.
    :copyright: Copyright 2007-2016 by the Sphinx team, see AUTHORS.
    :license: BSD, see LICENSE for details.
"""

from docutils import nodes
from docutils.parsers.rst import directives

import sphinx
from sphinx.locale import _
from sphinx.environment import NoUri
from sphinx.util.nodes import set_source_info
from docutils.parsers.rst import Directive
from docutils.parsers.rst.directives.admonitions import BaseAdmonition


class example_node(nodes.Admonition, nodes.Element):
    pass


class examplelist(nodes.General, nodes.Element):
    pass


class Example(BaseAdmonition):
    """
    A example entry, displayed (if configured) in the form of an admonition.
    """

    node_class = example_node
    has_content = True
    required_arguments = 0
    optional_arguments = 0
    final_argument_whitespace = False
    option_spec = {
        'class': directives.class_option,
    }

    def run(self):
        if not self.options.get('class'):
            self.options['class'] = ['admonition-example']

        (example,) = super(Example, self).run()
        if isinstance(example, nodes.system_message):
            return [example]

        example.insert(0, nodes.title(text=_('Example')))
        set_source_info(self, example)

        env = self.state.document.settings.env
        targetid = 'example'
        targetnode = nodes.target('', '', ids=[targetid])
        return [targetnode, example]


def process_examples(app, doctree):
    # collect all examples in the environment
    # this is not done in the directive itself because it some transformations
    # must have already been run, e.g. substitutions
    env = app.builder.env
    if not hasattr(env, 'example_all_examples'):
        env.example_all_examples = []
    for node in doctree.traverse(example_node):
        app.emit('example-defined', node)

        try:
            targetnode = node.parent[node.parent.index(node) - 1]
            if not isinstance(targetnode, nodes.target):
                raise IndexError
        except IndexError:
            targetnode = None
        newnode = node.deepcopy()
        del newnode['ids']
        env.example_all_examples.append({
            'docname': env.docname,
            'source': node.source or env.doc2path(env.docname),
            'lineno': node.line,
            'example': newnode,
            'target': targetnode,
        })



class ExampleList(Directive):
    """
    A list of all example entries.
    """

    has_content = False
    required_arguments = 0
    optional_arguments = 0
    final_argument_whitespace = False
    option_spec = {}

    def run(self):
        # Simply insert an empty examplelist node which will be replaced later
        # when process_example_nodes is called
        return [examplelist('')]


def process_example_nodes(app, doctree, fromdocname):
    if not app.config['example_include_examples']:
        for node in doctree.traverse(example_node):
            node.parent.remove(node)

    # Replace all examplelist nodes with a list of the collected examples.
    # Augment each example with a backlink to the original location.
    env = app.builder.env

    if not hasattr(env, 'example_all_examples'):
        env.example_all_examples = []

    for node in doctree.traverse(examplelist):
        if not app.config['example_include_examples']:
            node.replace_self([])
            continue

        content = []

        for example_info in env.example_all_examples:
            para = nodes.paragraph(classes=['example-source'])
            if app.config['example_link_only']:
                description = _('<<original entry>>')
            else:
                description = (
                    _('(The <<original entry>> is located in %s, line %d.)') %
                    (example_info['source'], example_info['lineno'])
                )
            desc1 = description[:description.find('<<')]
            desc2 = description[description.find('>>')+2:]
            para += nodes.Text(desc1, desc1)

            # Create a reference
            newnode = nodes.reference('', '', internal=True)
            innernode = nodes.emphasis(_('original entry'), _('original entry'))
            try:
                newnode['refuri'] = app.builder.get_relative_uri(
                    fromdocname, example_info['docname'])
                newnode['refuri'] += '#' + example_info['target']['refid']
            except NoUri:
                # ignore if no URI can be determined, e.g. for LaTeX output
                pass
            newnode.append(innernode)
            para += newnode
            para += nodes.Text(desc2, desc2)

            # (Recursively) resolve references in the example content
            example_entry = example_info['example']
            env.resolve_references(example_entry, example_info['docname'],
                                   app.builder)

            # Insert into the examplelist
            content.append(example_entry)
            content.append(para)

        node.replace_self(content)


def purge_examples(app, env, docname):
    if not hasattr(env, 'example_all_examples'):
        return
    env.example_all_examples = [example for example in env.example_all_examples
                                if example['docname'] != docname]


def merge_info(app, env, docnames, other):
    if not hasattr(other, 'example_all_examples'):
        return
    if not hasattr(env, 'example_all_examples'):
        env.example_all_examples = []
    env.example_all_examples.extend(other.example_all_examples)


def visit_example_node(self, node):
    self.visit_admonition(node)
    # self.visit_admonition(node, 'example')


def depart_example_node(self, node):
    self.depart_admonition(node)


def setup(app):
    app.add_event('example-defined')
    app.add_config_value('example_include_examples', True, 'html')
    app.add_config_value('example_link_only', False, 'html')
    app.add_config_value('example_emit_warnings', False, 'html')

    app.add_node(examplelist)
    app.add_node(example_node,
                 html=(visit_example_node, depart_example_node),
                 latex=(visit_example_node, depart_example_node),
                 text=(visit_example_node, depart_example_node),
                 man=(visit_example_node, depart_example_node),
                 texinfo=(visit_example_node, depart_example_node))

    app.add_directive('example', Example)
    app.add_directive('examplelist', ExampleList)
    app.connect('doctree-read', process_examples)
    app.connect('doctree-resolved', process_example_nodes)
    app.connect('env-purge-doc', purge_examples)
    app.connect('env-merge-info', merge_info)
    return {'version': sphinx.__display_version__, 'parallel_read_safe': True}
