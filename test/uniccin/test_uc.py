# SPDX-License-Identifier: MIT
"""Test uniccin.uc."""

from typing import Any

import pytest

import uniccin.data.ccc
import uniccin.uc

UNICHR_CASES: list[tuple[str, Any]] = [
    ('C', 67),
    ('D', 'D'),
    ('E', 'Latin capital letter E'),
    ('F', 'u46'),
    ('G', 'U+000000047'),
]

def test_from_character():
    c = uniccin.uc.from_character('C')
    assert c == uniccin.uc.UniCode('C')
    assert uniccin.uc.char(c) == 'C'

def test_from_bad_character():
    with pytest.raises(ValueError, match='not a character'):
        _ = uniccin.uc.from_character('Crap')

def test_from_integer():
    c = uniccin.uc.from_integer(66)
    assert c == uniccin.uc.UniCode(chr(66))

@pytest.mark.parametrize(('c', 'i'), UNICHR_CASES)
def test_unichr(c, i):
    u = uniccin.uc.unichr(i)
    assert u == c

def test_unichr_type_error():
    with pytest.raises(TypeError):
        _ = uniccin.uc.unichr(TypeError)  # type: ignore[arg-type]

def test_sanitize_clean():
    s = 'We are happy.'
    assert uniccin.uc.sanitize(s) == s

def test_sanitize_dirty_replace():
    s = 'We are \uDCBA happy.'
    assert uniccin.uc.sanitize(s) == 'We are \uFFFD happy.'

def test_sanitize_dirty_remove():
    s = 'We are \uDCBA happy.'
    assert uniccin.uc.sanitize(s, None) == 'We are  happy.'

def test_uni_bidirectional():
    assert uniccin.uc.bidirectional('B') == 'L'
    assert uniccin.uc.bidirectional('\u05D0') == 'R'  # HEBREW LETTER ALEF

def test_uni_block():
    assert uniccin.uc.block('\u00E5') == 'Latin-1 Supplement'

def test_uni_category():
    assert uniccin.uc.category('B') == 'Lu'
    assert uniccin.uc.category('\u05D0') == 'Lo'  # HEBREW LETTER ALEF

def test_uni_combining():
    assert uniccin.uc.combining('B') == 0
    # COMBINING DIAERESIS
    assert uniccin.uc.combining('\u0308') == uniccin.data.ccc.ABOVE

def test_uni_decimal():
    assert uniccin.uc.decimal('B') is None
    assert uniccin.uc.decimal('0') == 0
    # MATHEMATICAL DOUBLE-STRUCK DIGIT THREE
    assert uniccin.uc.decimal('\U0001D7DB') == 3
    assert uniccin.uc.decimal('\U00002464') is None  # CIRCLED DIGIT FIVE

def test_uni_decomposition():
    assert not uniccin.uc.decomposition('B')
    # LATIN SMALL LETTER E WITH ACUTE
    # → LATIN SMALL LETTER E, COMBINING ACUTE ACCENT
    assert uniccin.uc.decomposition('\u00E9') == '0065 0301'

def test_uni_digit():
    assert uniccin.uc.digit('B') is None
    assert uniccin.uc.digit('0') == 0
    # MATHEMATICAL DOUBLE-STRUCK DIGIT THREE
    assert uniccin.uc.digit('\U0001D7DB') == 3
    assert uniccin.uc.digit('\U00002464') == 5  # CIRCLED DIGIT FIVE

def test_uni_hexadecimal():
    assert uniccin.uc.hexadecimal('\u00E2') == '00E2'
    assert uniccin.uc.hexadecimal('\U0001D53B') == '1D53B'

def test_uni_html():
    assert uniccin.uc.html('B') == '&#0042;'
    assert uniccin.uc.html('\u00FE') == '&thorn;'

def test_uni_identifier():
    assert (uniccin.uc.identifier('\U0001D53C') ==
            'MATHEMATICAL_DOUBLE_STRUCK_CAPITAL_E')
    assert uniccin.uc.identifier('\U00101234', 'Default') == 'Default'

def test_uni_east_asian_width():
    assert uniccin.uc.east_asian_width('B') == 'Na'
    assert uniccin.uc.east_asian_width('\u05D0') == 'N'  # HEBREW LETTER ALEF
    assert uniccin.uc.east_asian_width('\u0308') == 'A'  # COMBINING DIAERESIS
    assert uniccin.uc.east_asian_width('\u30A6') == 'W'  # KATAKANA LETTER U
    assert uniccin.uc.east_asian_width(
        '\uFF21') == 'F'  # FULLWIDTH LATIN CAPITAL A
    assert uniccin.uc.east_asian_width('\uFF73') == 'H'  # HALFWIDTH KATAKANA U

def test_uni_mirrored():
    assert uniccin.uc.mirrored('B') == 0
    assert uniccin.uc.mirrored('(') == 1

def test_uni_name():
    assert uniccin.uc.name('B') == 'LATIN CAPITAL LETTER B'
    assert uniccin.uc.name('\U00101234') == 'U+101234'
    assert uniccin.uc.name('B', 'Default') == 'LATIN CAPITAL LETTER B'
    assert uniccin.uc.name('\U00101234', 'Default') == 'Default'

def test_uni_nfc():
    assert uniccin.uc.nfc('B') == 'B'
    assert uniccin.uc.normalize('B', 'nfc') == 'B'
    # COMBINING GRAVE TONE MARK → COMBINING GRAVE ACCENT
    assert uniccin.uc.nfc('\u0340') == '\u0300'
    assert uniccin.uc.normalize('\u0340', 'nfc') == '\u0300'

def test_uni_nfkc():
    assert uniccin.uc.nfkc('B') == 'B'
    assert uniccin.uc.normalize('B', 'nfkc') == 'B'
    # LATIN CAPITAL LETTER DZ WITH CARON → D, LATIN CAPITAL LETTER Z WITH CARON
    assert uniccin.uc.nfkc('\u01C4') == 'D\u017D'
    assert uniccin.uc.normalize('\u01C4', 'nfkc') == 'D\u017D'

def test_uni_nfd():
    assert uniccin.uc.nfd('B') == 'B'
    assert uniccin.uc.normalize('B', 'nfd') == 'B'
    # LATIN CAPITAL LETTER A WITH GRAVE → A, COMBINING GRAVE ACCENT
    assert uniccin.uc.nfd('\u00C0') == 'A\u0300'
    assert uniccin.uc.normalize('\u00C0', 'nfd') == 'A\u0300'

def test_uni_nfkd():
    assert uniccin.uc.nfkd('B') == 'B'
    assert uniccin.uc.normalize('B', 'nfkd') == 'B'
    # LATIN CAPITAL LETTER DZ WITH CARON → D, Z, COMBINING CARON
    assert uniccin.uc.nfkd('\u01C4') == 'DZ\u030C'
    assert uniccin.uc.normalize('\u01C4', 'nfkd') == 'DZ\u030C'

def test_uni_numeric():
    assert uniccin.uc.numeric('B') is None
    assert uniccin.uc.numeric('0') == 0
    # MATHEMATICAL DOUBLE-STRUCK DIGIT THREE
    assert uniccin.uc.numeric('\U0001D7DB') == 3
    assert uniccin.uc.numeric('\U00002464') == 5  # CIRCLED DIGIT FIVE
    assert uniccin.uc.numeric('\u00BC') == 0.25  # VULGAR FRACTION ONE QUARTER

def test_uni_ordinal():
    assert uniccin.uc.ordinal('B') == 66

def test_uni_usv():
    assert uniccin.uc.usv('B') == 'B'
    assert uniccin.uc.usv('\uD7FF') == '\uD7FF'
    assert uniccin.uc.usv('\uE000') == '\uE000'
    assert uniccin.uc.usv('\uDFFF', '\uFFFD') == '\uFFFD'
    assert not uniccin.uc.usv('\uD800')

def test_uni_utf8():
    assert uniccin.uc.utf8('B') == [66]
    assert uniccin.uc.utf8('\u00E0') == [195, 160]
    assert uniccin.uc.utf8('\u30A6') == [0xE3, 0x82, 0xA6]

def test_uni_utf16():
    assert uniccin.uc.utf16('B') == [66]
    assert uniccin.uc.utf16('\U0001D538') == [55349, 56632]
    assert not uniccin.uc.utf16('\uD838')

def test_uni_width():
    assert uniccin.uc.width('B') == 'Na'
    assert uniccin.uc.width('\u05D0') == 'N'  # HEBREW LETTER ALEF
    assert uniccin.uc.width('\u0308') == 'A'  # COMBINING DIAERESIS
    assert uniccin.uc.width('\u30A6') == 'W'  # KATAKANA LETTER U
    assert uniccin.uc.width('\uFF21') == 'F'  # FULLWIDTH LATIN CAPITAL LETTER A
    assert uniccin.uc.width('\uFF73') == 'H'  # HALFWIDTH KATAKANA LETTER U
