# SPDX-License-Identifier: MIT
"""Test uniccin.html."""

# Want to test explicit results.
# ruff: noqa: PLC1901

import uniccin.html

def test_html_character_to_entity():
    assert uniccin.html.character_to_entity('B') == '&#0042;'
    assert uniccin.html.character_to_entity('\u00FE') == '&thorn;'

def test_html_entity_to_characters():
    assert uniccin.html.entity_to_characters('&#0042;') == 'B'
    assert uniccin.html.entity_to_characters('#0042;') == 'B'
    assert uniccin.html.entity_to_characters('&#0042') == 'B'
    assert uniccin.html.entity_to_characters('#0042') == 'B'
    assert uniccin.html.entity_to_characters('&thorn;') == '\u00FE'
    assert uniccin.html.entity_to_characters('thorn') == '\u00FE'
    assert uniccin.html.entity_to_characters('thorn') == '\u00FE'
    assert uniccin.html.entity_to_characters('Aacute') == '\u00C1'
    assert uniccin.html.entity_to_characters('thickapprox') == '\u2248'
    assert uniccin.html.entity_to_characters('&asymp;') == '\u2248'
    assert uniccin.html.entity_to_characters('&lesg;') == '\u22DA\uFE00'

def test_html_entity_to_character_fail():
    assert uniccin.html.entity_to_characters('&notanhtmlentity;') == ''
    assert uniccin.html.entity_to_characters('&#0M42;') == ''
