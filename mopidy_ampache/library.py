from __future__ import unicode_literals

import logging

from mopidy import backend
from mopidy.models import SearchResult

logger = logging.getLogger(__name__)


class AmpacheLibraryProvider(backend.LibraryProvider):

    def __init__(self, *args, **kwargs):
        super(AmpacheLibraryProvider, self).__init__(*args, **kwargs)
        self.remote = self.backend.remote

    def _find_exact(self, query=None, uris=None):
        if not query:
            # Fetch all artists(browse library)
            return SearchResult(
                uri='ampache:search',
                tracks=self.remote.get_artists())

        return SearchResult(
            uri='ampache:tracks',
            tracks=self.remote.get_tracks_by(
                query.get('artist'), query.get('album')))

    def search(self, query=None, uris=None, exact=False):
        if exact:
            return self._find_exact(query=query, uris=uris)

        logger.debug('Query "%s":' % query)

        artist, album, title, any = None, None, None, None

        if 'artist' in query:
            artist = query['artist'][0]

        if 'album' in query:
            album = query['album'][0]

        if 'track' in query:
            title = query['track'][0]

        if 'any' in query:
            any = query['any'][0]

        return SearchResult(
            uri='ampache:tracks',
            tracks=self.remote.search_tracks(artist, album, title, any))

    def lookup(self, uri):
        try:
            song_id = uri.split("ampache://")[1]
            track = self.remote.get_song(song_id)
            return [track]
        except Exception as error:
            logger.debug('Failed to lookup "%s": %s' % (uri, error))
            return []
