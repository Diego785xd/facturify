import unicodedata


def normalize_text(text):
    return "".join(
        c
        for c in unicodedata.normalize("NFD", text.lower())
        if unicodedata.category(c) != "Mn"
    )


def contains_normalized(needle, haystack):
    return normalize_text(needle) in normalize_text(haystack)
