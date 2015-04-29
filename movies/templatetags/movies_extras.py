from django import template


register = template.Library()


@register.filter(name="russian_letter_to_ascii")
def russian_letter_to_ascii(letter):
    letters = {"А": "A",
               "Б": "B",
               "В": "V",
               "Г": "G",
               "Д": "D",
               "Е": "YE",
               "Ё": "YO",
               "Ж": "ZH",
               "З": "Z",
               "И": "I",
               "Й": "Y",
               "К": "K",
               "Л": "L",
               "М": "M",
               "Н": "N",
               "О": "O",
               "П": "P",
               "Р": "R",
               "С": "S",
               "Т": "T",
               "У": "U",
               "Ф": "F",
               "Х": "H",
               "Ц": "C",
               "Ч": "CH",
               "Ш": "SH",
               "Щ": "SCH",
               "Ы": "YI",
               "Э": "E",
               "Ю": "YU",
               "Я": "YA",
               }
    return letters[letter]


@register.filter(name="ascii_letter_to_russian")
def ascii_letter_to_russian(letter):
    letters = {"ru_A": "А",
               "ru_B": "Б",
               "ru_V": "В",
               "ru_G": "Г",
               "ru_D": "Д",
               "ru_YE": "Е",
               "ru_YO": "Ё",
               "ru_ZH": "Ж",
               "ru_Z": "З",
               "ru_I": "И",
               "ru_Y": "Й",
               "ru_K": "К",
               "ru_L": "Л",
               "ru_M": "М",
               "ru_N": "Н",
               "ru_O": "О",
               "ru_P": "П",
               "ru_R": "Р",
               "ru_S": "С",
               "ru_T": "Т",
               "ru_U": "У",
               "ru_F": "Ф",
               "ru_H": "Х",
               "ru_C": "Ц",
               "ru_CH": "Ч",
               "ru_SH": "Ш",
               "ru_SCH": "Щ",
               "ru_YI": "Ы",
               "ru_E": "Э",
               "ru_YU": "Ю",
               "ru_YA": "Я",
               }
    if letter in letters:
        return letters[letter]
    else:
        return letter
