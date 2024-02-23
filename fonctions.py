from interaction import InteractionManager, Interaction

def is_substance(string: str):
    for c in string:
        if c not in "ABCDEFGHIJKLMNOPQRSTUVWXYZ ,ÉÈÀÂÊÎÏÔÛÇ'.()":
            return False
    return True

def is_interaction(string: str):
    return string != "" and string[0] == "+"

def is_number(string: str) -> bool:
    for c in string.strip():
        if c not in "1234567890":
            return False
    return True


def cut_in_substances(string: str) -> list:
    subs = []
    lines = string.split("\n")
    prev = 0
    for i in range(len(lines)):
        if is_substance(lines[i]):
            subs.append("\n".join(lines[prev:i]))
            prev = i
    subs.append("\n".join(lines[prev:]))
    return subs[1:]

def get_interactions(lines: list) -> list:
    inters = []
    prev = 0
    print(lines)
    for i in range(1, len(lines)):
        if is_interaction(lines[i]):
            inters.append(lines[prev:i])
            prev = i
    inters.append(lines[prev:])
    inters2 = []
    for i in inters:
        print(i)
        subtance: str = i[0][1:]
        contrainte: str = i[1]
        com = ""
        if "Association DECONSEILLEE" in contrainte and contrainte != "Association DECONSEILLEE":
            contrainte = "Association DECONSEILLEE"
            com += i[1][len(contrainte):]
        elif "Précaution d'emploi" in contrainte and contrainte != "Précaution d'emploi":
            contrainte = "Précaution d'emploi"
            com += i[1][len(contrainte):]
        elif "A prendre en compte" in contrainte and contrainte != "A prendre en compte":
            contrainte = "A prendre en compte"
            com += i[1][len(contrainte):]
        elif "CONTRE-INDICATION" in contrainte and contrainte != "CONTRE-INDICATION":
            contrainte = "CONTRE-INDICATION"
            com += i[1][len(contrainte):]
        com += "".join(i[2:])
        inter = Interaction(subtance, contrainte, com)
        inters2.append(inter)

    return inters2

def extract_infos(string: str) -> InteractionManager:
    lines = string.split("\n")
    substance = lines[0]
    first_inter = 0
    while not is_interaction(lines[first_inter]):
        first_inter += 1
    com = " ".join(lines[1:first_inter])
    manager = InteractionManager(substance, com)

    print(substance)

    interactions = get_interactions(lines[first_inter:])
    for i in interactions:
        manager.add_interaction(i)
    return manager
