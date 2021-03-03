

def thesaurus(*names):
    dwarf_names = {}
    for dwarfs in names:
        if dwarfs[0] in dwarf_names:
            dwarf_names[dwarfs[0]] += [dwarfs]
        else:
            dwarf_names[dwarfs[0]] = [dwarfs]

    return dwarf_names

print(thesaurus("Телхар", "Лони", "Фарин", "Трор", "Нори", "Траин", "Кили", "Азагхал", "Гимли", "Фили", "Торин",
                "Бифур", "Глоин", "Двалин", "Ибун", "Дурин", "Наин", "Сталин", "Борин", "Оин", "Траин", "Балин",
                "Наин"))

