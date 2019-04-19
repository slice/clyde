# encoding: utf-8

from clyde.utils import ClydeChecker
from clyde.events import ALL_EVENTS

#: A set of acceptable Cog superclass names.
COG_BASENAMES = {'commands.Cog', 'Cog'}


class MissingCogListener(ClydeChecker):
    name = 'missing-cog-listener'
    priority = -1
    msgs = {
        'W7001': (
            'Missing @Cog.listener()', 'missing-cog-listener',
            ('This cog event is missing a @Cog.listener() decorator, which is '
             'needed for it to register properly. Without it, it is a no op.')
        )
    }

    def visit_asyncfunctiondef(self, node):
        has_cog_listener_decorator = node.decorators \
            and any(call.func.attrname == 'listener' for call in node.decorators.nodes)

        if (
            node.is_method()
            and any(basename in COG_BASENAMES for basename in node.parent.basenames)
            and node.name in ALL_EVENTS
            and not has_cog_listener_decorator
        ):
            self.add_message('missing-cog-listener', node=node)
