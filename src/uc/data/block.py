# SPDX-License-Identifier: MIT
"""Unicode blocks."""

BLOCKS: list[tuple[range, list[str]]] = [
    # Blocks
    # From http://unicode.org/Public/UNIDATA/Blocks.txt 15.0.0 2022-01-28
    (range(0x000000, 0x000080), ['Basic Latin', 'Latin', 'ASCII']),
    (range(0x000080, 0x000100), ['Latin-1 Supplement', 'Latin-1']),
    (range(0x000100, 0x000180), ['Latin Extended-A', 'Latin-A']),
    (range(0x000180, 0x000250), ['Latin Extended-B', 'Latin-D']),
    (range(0x000250, 0x0002B0), ['IPA Extensions']),
    (range(0x0002B0, 0x000300), ['Spacing Modifier Letters']),
    (range(0x000300, 0x000370), ['Combining Diacritical Marks']),
    (range(0x000370, 0x000400), ['Greek and Coptic', 'Greek', 'Coptic']),
    (range(0x000400, 0x000500), ['Cyrillic']),
    (range(0x000500, 0x000530), ['Cyrillic Supplement']),
    (range(0x000530, 0x000590), ['Armenian']),
    (range(0x000590, 0x000600), ['Hebrew']),
    (range(0x000600, 0x000700), ['Arabic']),
    (range(0x000700, 0x000750), ['Syriac']),
    (range(0x000750, 0x000780), ['Arabic Supplement']),
    (range(0x000780, 0x0007C0), ['Thaana']),
    (range(0x0007C0, 0x000800), ['NKo']),
    (range(0x000800, 0x000840), ['Samaritan']),
    (range(0x000840, 0x000860), ['Mandaic']),
    (range(0x000860, 0x000870), ['Syriac Supplement']),
    (range(0x000870, 0x0008A0), ['Arabic Extended-B']),
    (range(0x0008A0, 0x000900), ['Arabic Extended-A']),
    (range(0x000900, 0x000980), ['Devanagari']),
    (range(0x000980, 0x000A00), ['Bengali']),
    (range(0x000A00, 0x000A80), ['Gurmukhi']),
    (range(0x000A80, 0x000B00), ['Gujarati']),
    (range(0x000B00, 0x000B80), ['Oriya']),
    (range(0x000B80, 0x000C00), ['Tamil']),
    (range(0x000C00, 0x000C80), ['Telugu']),
    (range(0x000C80, 0x000D00), ['Kannada']),
    (range(0x000D00, 0x000D80), ['Malayalam']),
    (range(0x000D80, 0x000E00), ['Sinhala']),
    (range(0x000E00, 0x000E80), ['Thai']),
    (range(0x000E80, 0x000F00), ['Lao']),
    (range(0x000F00, 0x001000), ['Tibetan']),
    (range(0x001000, 0x0010A0), ['Myanmar']),
    (range(0x0010A0, 0x001100), ['Georgian']),
    (range(0x001100, 0x001200), ['Hangul Jamo']),
    (range(0x001200, 0x001380), ['Ethiopic']),
    (range(0x001380, 0x0013A0), ['Ethiopic Supplement']),
    (range(0x0013A0, 0x001400), ['Cherokee']),
    (range(0x001400,
           0x001680), ['Unified Canadian Aboriginal Syllabics', 'UCAS']),
    (range(0x001680, 0x0016A0), ['Ogham']),
    (range(0x0016A0, 0x001700), ['Runic']),
    (range(0x001700, 0x001720), ['Tagalog']),
    (range(0x001720, 0x001740), ['Hanunoo']),
    (range(0x001740, 0x001760), ['Buhid']),
    (range(0x001760, 0x001780), ['Tagbanwa']),
    (range(0x001780, 0x001800), ['Khmer']),
    (range(0x001800, 0x0018B0), ['Mongolian']),
    (range(0x0018B0,
           0x001900), ['Unified Canadian Aboriginal Syllabics Extended']),
    (range(0x001900, 0x001950), ['Limbu']),
    (range(0x001950, 0x001980), ['Tai Le']),
    (range(0x001980, 0x0019E0), ['New Tai Lue']),
    (range(0x0019E0, 0x001A00), ['Khmer Symbols']),
    (range(0x001A00, 0x001A20), ['Buginese']),
    (range(0x001A20, 0x001AB0), ['Tai Tham']),
    (range(0x001AB0, 0x001B00), ['Combining Diacritical Marks Extended']),
    (range(0x001B00, 0x001B80), ['Balinese']),
    (range(0x001B80, 0x001BC0), ['Sundanese']),
    (range(0x001BC0, 0x001C00), ['Batak']),
    (range(0x001C00, 0x001C50), ['Lepcha']),
    (range(0x001C50, 0x001C80), ['Ol Chiki']),
    (range(0x001C80, 0x001C90), ['Cyrillic Extended-C']),
    (range(0x001C90, 0x001CC0), ['Georgian Extended']),
    (range(0x001CC0, 0x001CD0), ['Sundanese Supplement']),
    (range(0x001CD0, 0x001D00), ['Vedic Extensions']),
    (range(0x001D00, 0x001D80), ['Phonetic Extensions']),
    (range(0x001D80, 0x001DC0), ['Phonetic Extensions Supplement']),
    (range(0x001DC0, 0x001E00), ['Combining Diacritical Marks Supplement']),
    (range(0x001E00, 0x001F00), ['Latin Extended Additional']),
    (range(0x001F00, 0x002000), ['Greek Extended']),
    (range(0x002000, 0x002070), ['General Punctuation']),
    (range(0x002070, 0x0020A0),
     ['Superscripts and Subscripts', 'Superscripts', 'Subscripts']),
    (range(0x0020A0, 0x0020D0), ['Currency Symbols']),
    (range(0x0020D0, 0x002100), ['Combining Diacritical Marks for Symbols']),
    (range(0x002100, 0x002150), ['Letterlike Symbols']),
    (range(0x002150, 0x002190), ['Number Forms']),
    (range(0x002190, 0x002200), ['Arrows']),
    (range(0x002200, 0x002300), ['Mathematical Operators']),
    (range(0x002300, 0x002400), ['Miscellaneous Technical']),
    (range(0x002400, 0x002440), ['Control Pictures']),
    (range(0x002440, 0x002460), ['Optical Character Recognition']),
    (range(0x002460, 0x002500), ['Enclosed Alphanumerics']),
    (range(0x002500, 0x002580), ['Box Drawing']),
    (range(0x002580, 0x0025A0), ['Block Elements']),
    (range(0x0025A0, 0x002600), ['Geometric Shapes']),
    (range(0x002600, 0x002700), ['Miscellaneous Symbols']),
    (range(0x002700, 0x0027C0), ['Dingbats']),
    (range(0x0027C0, 0x0027F0), ['Miscellaneous Mathematical Symbols-A']),
    (range(0x0027F0, 0x002800), ['Supplemental Arrows-A']),
    (range(0x002800, 0x002900), ['Braille Patterns']),
    (range(0x002900, 0x002980), ['Supplemental Arrows-B']),
    (range(0x002980, 0x002A00), ['Miscellaneous Mathematical Symbols-B']),
    (range(0x002A00, 0x002B00), ['Supplemental Mathematical Operators']),
    (range(0x002B00, 0x002C00), ['Miscellaneous Symbols and Arrows']),
    (range(0x002C00, 0x002C60), ['Glagolitic']),
    (range(0x002C60, 0x002C80), ['Latin Extended-C']),
    (range(0x002C80, 0x002D00), ['Coptic']),
    (range(0x002D00, 0x002D30), ['Georgian Supplement']),
    (range(0x002D30, 0x002D80), ['Tifinagh']),
    (range(0x002D80, 0x002DE0), ['Ethiopic Extended']),
    (range(0x002DE0, 0x002E00), ['Cyrillic Extended-A']),
    (range(0x002E00, 0x002E80), ['Supplemental Punctuation']),
    (range(0x002E80, 0x002F00), ['CJK Radicals Supplement']),
    (range(0x002F00, 0x002FE0), ['Kangxi Radicals']),
    (range(0x002FF0, 0x003000), ['Ideographic Description Characters']),
    (range(0x003000, 0x003040),
     ['CJK Symbols and Punctuation', 'CJK Symbols', 'CJK Punctuation']),
    (range(0x003040, 0x0030A0), ['Hiragana']),
    (range(0x0030A0, 0x003100), ['Katakana']),
    (range(0x003100, 0x003130), ['Bopomofo']),
    (range(0x003130, 0x003190), ['Hangul Compatibility Jamo']),
    (range(0x003190, 0x0031A0), ['Kanbun']),
    (range(0x0031A0, 0x0031C0), ['Bopomofo Extended']),
    (range(0x0031C0, 0x0031F0), ['CJK Strokes']),
    (range(0x0031F0, 0x003200), ['Katakana Phonetic Extensions']),
    (range(0x003200, 0x003300), ['Enclosed CJK Letters and Months']),
    (range(0x003300, 0x003400), ['CJK Compatibility']),
    (range(0x003400, 0x004DC0), ['CJK Unified Ideographs Extension A']),
    (range(0x004DC0, 0x004E00), ['Yijing Hexagram Symbols']),
    (range(0x004E00, 0x00A000), ['CJK Unified Ideographs']),
    (range(0x00A000, 0x00A490), ['Yi Syllables']),
    (range(0x00A490, 0x00A4D0), ['Yi Radicals']),
    (range(0x00A4D0, 0x00A500), ['Lisu']),
    (range(0x00A500, 0x00A640), ['Vai']),
    (range(0x00A640, 0x00A6A0), ['Cyrillic Extended-B']),
    (range(0x00A6A0, 0x00A700), ['Bamum']),
    (range(0x00A700, 0x00A720), ['Modifier Tone Letters']),
    (range(0x00A720, 0x00A800), ['Latin Extended-D']),
    (range(0x00A800, 0x00A830), ['Syloti Nagri']),
    (range(0x00A830, 0x00A840), ['Common Indic Number Forms']),
    (range(0x00A840, 0x00A880), ['Phags-pa']),
    (range(0x00A880, 0x00A8E0), ['Saurashtra']),
    (range(0x00A8E0, 0x00A900), ['Devanagari Extended']),
    (range(0x00A900, 0x00A930), ['Kayah Li']),
    (range(0x00A930, 0x00A960), ['Rejang']),
    (range(0x00A960, 0x00A980), ['Hangul Jamo Extended-A']),
    (range(0x00A980, 0x00A9E0), ['Javanese']),
    (range(0x00A9E0, 0x00AA00), ['Myanmar Extended-B']),
    (range(0x00AA00, 0x00AA60), ['Cham']),
    (range(0x00AA60, 0x00AA80), ['Myanmar Extended-A']),
    (range(0x00AA80, 0x00AAE0), ['Tai Viet']),
    (range(0x00AAE0, 0x00AB00), ['Meetei Mayek Extensions']),
    (range(0x00AB00, 0x00AB30), ['Ethiopic Extended-A']),
    (range(0x00AB30, 0x00AB70), ['Latin Extended-E']),
    (range(0x00AB70, 0x00ABC0), ['Cherokee Supplement']),
    (range(0x00ABC0, 0x00AC00), ['Meetei Mayek']),
    (range(0x00AC00, 0x00D7B0), ['Hangul Syllables']),
    (range(0x00D7B0, 0x00D800), ['Hangul Jamo Extended-B']),
    (range(0x00D800, 0x00DB80), ['High Surrogates']),
    (range(0x00DB80, 0x00DC00), ['High Private Use Surrogates']),
    (range(0x00DC00, 0x00E000), ['Low Surrogates']),
    (range(0x00E000, 0x00F900), ['Private Use Area']),
    (range(0x00F900, 0x00FB00), ['CJK Compatibility Ideographs']),
    (range(0x00FB00, 0x00FB50), ['Alphabetic Presentation Forms']),
    (range(0x00FB50, 0x00FE00), ['Arabic Presentation Forms-A']),
    (range(0x00FE00, 0x00FE10), ['Variation Selectors']),
    (range(0x00FE10, 0x00FE20), ['Vertical Forms']),
    (range(0x00FE20, 0x00FE30), ['Combining Half Marks']),
    (range(0x00FE30, 0x00FE50), ['CJK Compatibility Forms']),
    (range(0x00FE50, 0x00FE70), ['Small Form Variants']),
    (range(0x00FE70, 0x00FF00), ['Arabic Presentation Forms-B']),
    (range(0x00FF00, 0x00FFF0),
     ['Halfwidth and Fullwidth Forms', 'Halfwidth', 'Fullwidth']),
    (range(0x00FFF0, 0x010000), ['Specials']),
    (range(0x010000, 0x010080), ['Linear B Syllabary']),
    (range(0x010080, 0x010100), ['Linear B Ideograms']),
    (range(0x010100, 0x010140), ['Aegean Numbers']),
    (range(0x010140, 0x010190), ['Ancient Greek Numbers']),
    (range(0x010190, 0x0101D0), ['Ancient Symbols']),
    (range(0x0101D0, 0x010200), ['Phaistos Disc']),
    (range(0x010280, 0x0102A0), ['Lycian']),
    (range(0x0102A0, 0x0102E0), ['Carian']),
    (range(0x0102E0, 0x010300), ['Coptic Epact Numbers']),
    (range(0x010300, 0x010330), ['Old Italic']),
    (range(0x010330, 0x010350), ['Gothic']),
    (range(0x010350, 0x010380), ['Old Permic']),
    (range(0x010380, 0x0103A0), ['Ugaritic']),
    (range(0x0103A0, 0x0103E0), ['Old Persian']),
    (range(0x010400, 0x010450), ['Deseret']),
    (range(0x010450, 0x010480), ['Shavian']),
    (range(0x010480, 0x0104B0), ['Osmanya']),
    (range(0x0104B0, 0x010500), ['Osage']),
    (range(0x010500, 0x010530), ['Elbasan']),
    (range(0x010530, 0x010570), ['Caucasian Albanian']),
    (range(0x010570, 0x0105C0), ['Vithkuqi']),
    (range(0x010600, 0x010780), ['Linear A']),
    (range(0x010780, 0x0107C0), ['Latin Extended-F']),
    (range(0x010800, 0x010840), ['Cypriot Syllabary']),
    (range(0x010840, 0x010860), ['Imperial Aramaic']),
    (range(0x010860, 0x010880), ['Palmyrene']),
    (range(0x010880, 0x0108B0), ['Nabataean']),
    (range(0x0108E0, 0x010900), ['Hatran']),
    (range(0x010900, 0x010920), ['Phoenician']),
    (range(0x010920, 0x010940), ['Lydian']),
    (range(0x010980, 0x0109A0), ['Meroitic Hieroglyphs']),
    (range(0x0109A0, 0x010A00), ['Meroitic Cursive']),
    (range(0x010A00, 0x010A60), ['Kharoshthi']),
    (range(0x010A60, 0x010A80), ['Old South Arabian']),
    (range(0x010A80, 0x010AA0), ['Old North Arabian']),
    (range(0x010AC0, 0x010B00), ['Manichaean']),
    (range(0x010B00, 0x010B40), ['Avestan']),
    (range(0x010B40, 0x010B60), ['Inscriptional Parthian']),
    (range(0x010B60, 0x010B80), ['Inscriptional Pahlavi']),
    (range(0x010B80, 0x010BB0), ['Psalter Pahlavi']),
    (range(0x010C00, 0x010C50), ['Old Turkic']),
    (range(0x010C80, 0x010D00), ['Old Hungarian']),
    (range(0x010D00, 0x010D40), ['Hanifi Rohingya']),
    (range(0x010E60, 0x010E80), ['Rumi Numeral Symbols']),
    (range(0x010E80, 0x010EC0), ['Yezidi']),
    (range(0x010EC0, 0x010F00), ['Arabic Extended-C']),
    (range(0x010F00, 0x010F30), ['Old Sogdian']),
    (range(0x010F30, 0x010F70), ['Sogdian']),
    (range(0x010F70, 0x010FB0), ['Old Uyghur']),
    (range(0x010FB0, 0x010FE0), ['Chorasmian']),
    (range(0x010FE0, 0x011000), ['Elymaic']),
    (range(0x011000, 0x011080), ['Brahmi']),
    (range(0x011080, 0x0110D0), ['Kaithi']),
    (range(0x0110D0, 0x011100), ['Sora Sompeng']),
    (range(0x011100, 0x011150), ['Chakma']),
    (range(0x011150, 0x011180), ['Mahajani']),
    (range(0x011180, 0x0111E0), ['Sharada']),
    (range(0x0111E0, 0x011200), ['Sinhala Archaic Numbers']),
    (range(0x011200, 0x011250), ['Khojki']),
    (range(0x011280, 0x0112B0), ['Multani']),
    (range(0x0112B0, 0x011300), ['Khudawadi']),
    (range(0x011300, 0x011380), ['Grantha']),
    (range(0x011400, 0x011480), ['Newa']),
    (range(0x011480, 0x0114E0), ['Tirhuta']),
    (range(0x011580, 0x011600), ['Siddham']),
    (range(0x011600, 0x011660), ['Modi']),
    (range(0x011660, 0x011680), ['Mongolian Supplement']),
    (range(0x011680, 0x0116D0), ['Takri']),
    (range(0x011700, 0x011750), ['Ahom']),
    (range(0x011800, 0x011850), ['Dogra']),
    (range(0x0118A0, 0x011900), ['Warang Citi']),
    (range(0x011900, 0x011960), ['Dives Akuru']),
    (range(0x0119A0, 0x011A00), ['Nandinagari']),
    (range(0x011A00, 0x011A50), ['Zanabazar Square']),
    (range(0x011A50, 0x011AB0), ['Soyombo']),
    (range(0x011AB0,
           0x011AC0), ['Unified Canadian Aboriginal Syllabics Extended-A']),
    (range(0x011AC0, 0x011B00), ['Pau Cin Hau']),
    (range(0x011B00, 0x011B60), ['Devanagari Extended-A']),
    (range(0x011C00, 0x011C70), ['Bhaiksuki']),
    (range(0x011C70, 0x011CC0), ['Marchen']),
    (range(0x011D00, 0x011D60), ['Masaram Gondi']),
    (range(0x011D60, 0x011DB0), ['Gunjala Gondi']),
    (range(0x011EE0, 0x011F00), ['Makasar']),
    (range(0x011F00, 0x011F60), ['Kawi']),
    (range(0x011FB0, 0x011FC0), ['Lisu Supplement']),
    (range(0x011FC0, 0x012000), ['Tamil Supplement']),
    (range(0x012000, 0x012400), ['Cuneiform']),
    (range(0x012400, 0x012480), ['Cuneiform Numbers and Punctuation']),
    (range(0x012480, 0x012550), ['Early Dynastic Cuneiform']),
    (range(0x012F90, 0x013000), ['Cypro-Minoan']),
    (range(0x013000, 0x013430), ['Egyptian Hieroglyphs']),
    (range(0x013430, 0x013460), ['Egyptian Hieroglyph Format Controls']),
    (range(0x014400, 0x014680), ['Anatolian Hieroglyphs']),
    (range(0x016800, 0x016A40), ['Bamum Supplement']),
    (range(0x016A40, 0x016A70), ['Mro']),
    (range(0x016A70, 0x016AD0), ['Tangsa']),
    (range(0x016AD0, 0x016B00), ['Bassa Vah']),
    (range(0x016B00, 0x016B90), ['Pahawh Hmong']),
    (range(0x016E40, 0x016EA0), ['Medefaidrin']),
    (range(0x016F00, 0x016FA0), ['Miao']),
    (range(0x016FE0, 0x017000), ['Ideographic Symbols and Punctuation']),
    (range(0x017000, 0x018800), ['Tangut']),
    (range(0x018800, 0x018B00), ['Tangut Components']),
    (range(0x018B00, 0x018D00), ['Khitan Small Script']),
    (range(0x018D00, 0x018D80), ['Tangut Supplement']),
    (range(0x01AFF0, 0x01B000), ['Kana Extended-B']),
    (range(0x01B000, 0x01B100), ['Kana Supplement']),
    (range(0x01B100, 0x01B130), ['Kana Extended-A']),
    (range(0x01B130, 0x01B170), ['Small Kana Extension']),
    (range(0x01B170, 0x01B300), ['Nushu']),
    (range(0x01BC00, 0x01BCA0), ['Duployan']),
    (range(0x01BCA0, 0x01BCB0), ['Shorthand Format Controls']),
    (range(0x01CF00, 0x01CFD0), ['Znamenny Musical Notation']),
    (range(0x01D000, 0x01D100), ['Byzantine Musical Symbols']),
    (range(0x01D100, 0x01D200), ['Musical Symbols']),
    (range(0x01D200, 0x01D250), ['Ancient Greek Musical Notation']),
    (range(0x01D2C0, 0x01D2E0), ['Kaktovik Numerals']),
    (range(0x01D2E0, 0x01D300), ['Mayan Numerals']),
    (range(0x01D300, 0x01D360), ['Tai Xuan Jing Symbols']),
    (range(0x01D360, 0x01D380), ['Counting Rod Numerals']),
    (range(0x01D400, 0x01D800), ['Mathematical Alphanumeric Symbols']),
    (range(0x01D800, 0x01DAB0), ['Sutton SignWriting']),
    (range(0x01DF00, 0x01E000), ['Latin Extended-G']),
    (range(0x01E000, 0x01E030), ['Glagolitic Supplement']),
    (range(0x01E030, 0x01E090), ['Cyrillic Extended-D']),
    (range(0x01E100, 0x01E150), ['Nyiakeng Puachue Hmong']),
    (range(0x01E290, 0x01E2C0), ['Toto']),
    (range(0x01E2C0, 0x01E300), ['Wancho']),
    (range(0x01E4D0, 0x01E500), ['Nag Mundari']),
    (range(0x01E7E0, 0x01E800), ['Ethiopic Extended-B']),
    (range(0x01E800, 0x01E8E0), ['Mende Kikakui']),
    (range(0x01E900, 0x01E960), ['Adlam']),
    (range(0x01EC70, 0x01ECC0), ['Indic Siyaq Numbers']),
    (range(0x01ED00, 0x01ED50), ['Ottoman Siyaq Numbers']),
    (range(0x01EE00, 0x01EF00), ['Arabic Mathematical Alphabetic Symbols']),
    (range(0x01F000, 0x01F030), ['Mahjong Tiles']),
    (range(0x01F030, 0x01F0A0), ['Domino Tiles']),
    (range(0x01F0A0, 0x01F100), ['Playing Cards']),
    (range(0x01F100, 0x01F200), ['Enclosed Alphanumeric Supplement']),
    (range(0x01F200, 0x01F300), ['Enclosed Ideographic Supplement']),
    (range(0x01F300, 0x01F600), ['Miscellaneous Symbols and Pictographs']),
    (range(0x01F600, 0x01F650), ['Emoticons']),
    (range(0x01F650, 0x01F680), ['Ornamental Dingbats']),
    (range(0x01F680, 0x01F700), ['Transport and Map Symbols']),
    (range(0x01F700, 0x01F780), ['Alchemical Symbols']),
    (range(0x01F780, 0x01F800), ['Geometric Shapes Extended']),
    (range(0x01F800, 0x01F900), ['Supplemental Arrows-C']),
    (range(0x01F900, 0x01FA00), ['Supplemental Symbols and Pictographs']),
    (range(0x01FA00, 0x01FA70), ['Chess Symbols']),
    (range(0x01FA70, 0x01FB00), ['Symbols and Pictographs Extended-A']),
    (range(0x01FB00, 0x01FC00), ['Symbols for Legacy Computing']),
    (range(0x020000, 0x02A6E0), ['CJK Unified Ideographs Extension B']),
    (range(0x02A700, 0x02B740), ['CJK Unified Ideographs Extension C']),
    (range(0x02B740, 0x02B820), ['CJK Unified Ideographs Extension D']),
    (range(0x02B820, 0x02CEB0), ['CJK Unified Ideographs Extension E']),
    (range(0x02CEB0, 0x02EBF0), ['CJK Unified Ideographs Extension F']),
    (range(0x02F800, 0x02FA20), ['CJK Compatibility Ideographs Supplement']),
    (range(0x030000, 0x031350), ['CJK Unified Ideographs Extension G']),
    (range(0x031350, 0x0323B0), ['CJK Unified Ideographs Extension H']),
    (range(0x0E0000, 0x0E0080), ['Tags']),
    (range(0x0E0100, 0x0E01F0), ['Variation Selectors Supplement']),
    (range(0x0F0000, 0x100000), ['Supplementary Private Use Area-A',
                                 'S PUA A']),
    (range(0x100000, 0x110000), ['Supplementary Private Use Area-B',
                                 'S PUA B']),
    # Planes
    (range(0x000000, 0x010000), ['Basic Multilingual Plane', 'BMP']),
    (range(0x010000, 0x020000), ['Supplementary Multilingual Plane', 'SMP']),
    (range(0x020000, 0x030000), ['Supplementary Ideographic Plane', 'SIP']),
]
