from __future__ import unicode_literals

import logging
import pykka

from mopidy import backend

from .library import AmpacheLibraryProvider
from .playlist import AmpachePlaylistsProvider
from .client import AmpacheRemoteClient


logger = logging.getLogger(__name__)


class AmpacheBackend(pykka.ThreadingActor, backend.Backend):

    def __init__(self, config, audio):
        super(AmpacheBackend, self).__init__()

        self.remote = AmpacheRemoteClient(
            config['ampache']['hostname'],
            config['ampache']['port'],
            config['ampache']['username'],
            config['ampache']['password'],
            config['ampache']['ssl'],
            config['ampache']['context'])

        self.config = config
        self.library = AmpacheLibraryProvider(backend=self)
        self.playback = AmpachePlaybackProvider(audio=audio, backend=self)
        self.playlists = AmpachePlaylistsProvider(backend=self)

        self.uri_schemes = ['ampache']


class AmpachePlaybackProvider(backend.PlaybackProvider):

    def translate_uri(self, uri):
        logger.debug('Getting info for track %s' % uri)
        id = uri.split('ampache://')[1]
        real_uri = self.backend.remote.build_url_from_song_id(id)
        return real_uri
