from typing import Any, Literal, NotRequired, TypedDict

ScrobblesJSON = list[list['Scrobble']]

Scrobble = TypedDict(
    "Scrobble",
    {
        "artist": 'Artist',
        "streamable": str,
        "image": Any,
        "mbid": Any,
        "album": 'Album',
        "name": str,
        "@attr": NotRequired[Any],
        "url": str,
        "date": NotRequired['Date'],
    },
)

Artist = TypedDict(
    "Artist",
    {
        "mbid": str,
        "#text": str,
    },
)

Album = TypedDict(
    "Album",
    {
        "mbid": str,
        "#text": str,
    }
)

Date = TypedDict(
    "Date",
    {
        "#text": str,
        "uts": str,
    }
)
