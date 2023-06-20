# SPDX-License-Identifier: MIT
"""Character conversions and properties."""

import unicodedata

from collections.abc import Callable, Sequence
from typing import Any, NewType, TypeVar

import uniccin.block
import uniccin.html

UniCode = NewType('UniCode', str)

T = TypeVar('T')

# Conversion

def from_character(c: str) -> UniCode:
    if isinstance(c, str) and len(c) == 1:
        return UniCode(c)
    message = '{c!r} is not a character'
    raise ValueError(message)

def from_integer(c: int) -> UniCode:
    return UniCode(chr(c))

def unichr(value: int | str) -> UniCode:
    """Convert an integer, character, or Unicode name to UniCode."""
    if isinstance(value, int):
        return UniCode(chr(value))

    if not isinstance(value, str):
        message = f'{value} is not str or int'
        raise TypeError(message)

    # Now we have a str.
    if len(value) == 1:
        return UniCode(value)

    # Check for a string that represents an integer.
    try:
        return UniCode(chr(int(value, 0)))
    except ValueError:
        pass

    # Check for a Unicode character name.
    try:
        return UniCode(unicodedata.lookup(value))
    except KeyError:
        pass

    # Check for U+hex.
    if value.lower()[0] == 'u':
        i = value[1 :]
        if i[0] == '+':
            i = i[1 :]
        # Let this raise ValueError.
        return UniCode(chr(int(i, 16)))

    message = f'No character {value!r}'
    raise ValueError(message)

def utf32to16(n: int) -> Sequence[int]:
    """Convert a number to a list holding its UTF-16 encoding."""
    if (n <= 0xD7FF) or (0xE000 <= n <= 0xFFFF):
        return [n]
    if n < 0x10000 or n > 0x10FFFF:
        return []
    n = n - 0x10000
    return [0xD800 + (n >> 10), 0xDC00 + (n & 0x3FF)]

def utf32to8(n: int) -> Sequence[int]:
    """Convert a number to a list holding its UTF-8 encoding."""
    if n < 0x80:
        return [n]
    r = []
    m = 0x1F
    while True:
        r.append(0x80 | (n & 0x3F))
        n = n >> 6
        if n & m == n:
            break
        m = m >> 1
    r.append((0xFE ^ (m << 1)) | n)
    r.reverse()
    return r

def sanitize(s: str, replacement: str | None = '\uFFFD') -> str:
    """Remove or replace disallowed code points (surrogates)."""
    try:
        _ = bytes(s, encoding='utf-32')
    except UnicodeEncodeError:
        r = []
        for c in s:
            if ch := usv(UniCode(c), replacement):
                r.append(ch)
        s = ''.join(r)
    return s

# Normalization

def normalize(c: str, form: str) -> str:
    # NB: character first.
    return unicodedata.normalize(form.upper(), c)

# Uniform property access functions. These all accept a ‘default’ argument,
# even though in many cases it is not used.

PropertyAccessFunction = Callable[[UniCode, Any | None], Any]

PROPERTIES: dict[str, PropertyAccessFunction] = {}

def register(v: dict) -> Callable:

    def decorator(fn: Callable) -> Callable:
        v[fn.__name__] = fn
        return fn

    return decorator

@register(PROPERTIES)
def bidirectional(c: UniCode, _=None) -> str:
    return unicodedata.bidirectional(c)

@register(PROPERTIES)
def block(c: UniCode, _=None) -> str:
    return uniccin.block.block(ord(c))[1]

@register(PROPERTIES)
def category(c: UniCode, _=None) -> str:
    return unicodedata.category(c)

@register(PROPERTIES)
def char(c: UniCode, _=None) -> str:
    return c

@register(PROPERTIES)
def combining(c: UniCode, _=None) -> int:
    return unicodedata.combining(c)

@register(PROPERTIES)
def decimal(c: UniCode, default: int | None = None) -> int | None:
    return unicodedata.decimal(c, default)

@register(PROPERTIES)
def decomposition(c: UniCode, _=None) -> str:
    return unicodedata.decomposition(c)

@register(PROPERTIES)
def digit(c: UniCode, default: int | None = None) -> int | None:
    return unicodedata.digit(c, default)

@register(PROPERTIES)
def east_asian_width(c: UniCode, _=None) -> str:
    return width(c)

@register(PROPERTIES)
def hexadecimal(c: UniCode, _=None, digits: int = 4) -> str:
    return f'{ord(c):0{digits}X}'

@register(PROPERTIES)
def html(c: UniCode, _=None) -> str:
    return uniccin.html.character_to_entity(c)

@register(PROPERTIES)
def identifier(c: UniCode, default: str | None = None) -> str | None:
    try:
        return unicodedata.name(c).replace(' ', '_').replace('-', '_')
    except ValueError:
        return default

@register(PROPERTIES)
def mirrored(c: UniCode, _=None) -> int:
    return unicodedata.mirrored(c)

@register(PROPERTIES)
def name(c: UniCode, default: str | None = None) -> str:
    try:
        return unicodedata.name(c)
    except ValueError:
        if default is not None:
            return default
        return f'U+{ord(c):04X}'

@register(PROPERTIES)
def nfc(c: UniCode, _=None) -> str:
    return unicodedata.normalize('NFC', c)

@register(PROPERTIES)
def nfkc(c: UniCode, _=None) -> str:
    return unicodedata.normalize('NFKC', c)

@register(PROPERTIES)
def nfd(c: UniCode, _=None) -> str:
    return unicodedata.normalize('NFD', c)

@register(PROPERTIES)
def nfkd(c: UniCode, _=None) -> str:
    return unicodedata.normalize('NFKD', c)

@register(PROPERTIES)
def numeric(c: UniCode, default: float | None = None) -> float | None:
    return unicodedata.numeric(c, default)

@register(PROPERTIES)
def ordinal(c: UniCode, _=None) -> int:
    return ord(c)

@register(PROPERTIES)
def u(c: UniCode, _=None, digits: int = 4) -> str:
    return f'U+{ord(c):0{digits}X}'

@register(PROPERTIES)
def usv(c: UniCode, replacement: str | None = None) -> str | None:
    """Unicode Scalar Value."""
    if ord(c) in range(0xD800, 0xE000):
        return replacement
    return c

@register(PROPERTIES)
def utf8(c: UniCode, _=None) -> Sequence[int]:
    return utf32to8(ord(c))

@register(PROPERTIES)
def utf16(c: UniCode, _=None) -> Sequence[int]:
    return utf32to16(ord(c))

@register(PROPERTIES)
def width(c: UniCode, _=None) -> str:
    return unicodedata.east_asian_width(c)
