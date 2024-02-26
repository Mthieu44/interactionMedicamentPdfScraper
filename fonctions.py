from interaction import InteractionManager, Interaction



# medic = (29.280000686645508, 502.8668518066406, 87.56080627441406, 514.0391845703125, 'ZOPICLONE\n', 37, 0)
# com = (36.720001220703125, 517.9428100585938, 285.3660583496094, 525.763427734375, 'Voir aussi : benzodiazépines et apparentés - hypnotiques - médicaments sédatifs\n', 38, 0)
# interaction = (32.15999984741211, 531.0775146484375, 186.2428436279297, 540.1353759765625, '+ INHIBITEURS PUISSANTS DU CYP3A4\n', 39, 0)
# com1 = (97.44000244140625, 543.9828491210938, 262.92352294921875, 551.803466796875, "Légère augmentation de l'effet sédatif de la zopiclone.\n", 42, 0)
# contrainte = (317.2799987792969, 594.0228271484375, 383.0893249511719, 601.8434448242188, "Précaution d'emploi\n", 44, 0)
# com2 = (317.2799987792969, 605.4228515625, 519.234375, 613.2434692382812, 'Surveillance clinique. Utiliser éventuellement un autre hypnotique.\n', 45, 0)
def is_substance(block: tuple) -> bool:
    return int(block[0]) == 29

def is_com(block: tuple) -> bool:
    return int(block[0]) == 36

def is_interaction(block: tuple) -> bool:
    return int(block[0]) == 32

def is_com1(block: tuple) -> bool:
    return int(block[0]) == 97

def is_com2(block: tuple) -> bool:
    return int(block[0]) == 317

def get_string(b: tuple[float, float, float, float, str, int, int]) -> str:
    s = b[4]
    if s[0] == "+":
        s = s[1:]
    s = s.replace("\n", " ")
    s = s.replace("\"", "\'")
    return s.strip()

def extract_infos(blocks: list[tuple[float, float, float, float, str, int, int]]) -> list[InteractionManager]:
    list_im = [InteractionManager("")]
    for b in blocks:
        if is_substance(b):
            list_im.append(InteractionManager(get_string(b)))
        elif is_com(b):
            list_im[-1].com += get_string(b) if list_im[-1].com == "" else " " + get_string(b)
        elif is_interaction(b):
            list_im[-1].add_interaction(Interaction(get_string(b), "", ""))
        elif is_com1(b):
            list_im[-1].interactions[-1].com1 += get_string(b) if list_im[-1].interactions[-1].com1 == "" else " " + get_string(b)
        elif is_com2(b):
            list_im[-1].interactions[-1].com2 += get_string(b) if list_im[-1].interactions[-1].com2 == "" else " " + get_string(b)
        else:
            print("string non-identifié (surement un arabe) : ")
            print(b)

    return list_im[1:]