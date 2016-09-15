from __future__ import unicode_literals

import os

from mopidy import ext, config

__version__ = '1.0.0'


class AmpacheExtension(ext.Extension):

    dist_name = 'Mopidy-Ampache'
    ext_name = 'ampache'
    version = __version__

    def get_default_config(self):
        conf_file = os.path.join(os.path.dirname(__file__), 'ext.conf')
        return config.read(conf_file)

    def get_config_schema(self):
        schema = super(AmpacheExtension, self).get_config_schema()
        schema['hostname'] = config.Hostname()
        schema['port'] = config.Port()
        schema['username'] = config.String()
        schema['password'] = config.Secret()
        schema['ssl'] = config.Boolean()
        schema['context'] = config.String()
        return schema

    def setup(self, registry):
        from .actor import AmpacheBackend
        registry.add('backend', AmpacheBackend)
