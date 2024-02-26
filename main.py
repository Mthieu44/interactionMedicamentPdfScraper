"""import PyPDF2
from interaction import Interaction, InteractionManager
from fonctions import cut_in_substances, extract_infos

pdfFileObj = open('interactions.pdf', 'rb')
pdfReader = PyPDF2.PdfReader(pdfFileObj)


full_text = ""

for page in pdfReader.pages[2:]:
    full_text += page.extract_text()

substances = cut_in_substances(full_text)
with open("interactions.json", "w") as file:
    file.write("[\n")
    for i in substances:
        manager = extract_infos(i)
        file.write(str(manager.to_json()) + ",\n")
    file.write("]\n")
    
 
# closing the pdf file object
pdfFileObj.close()"""

import fitz  # Module PyMuPDF
from fonctions import extract_infos

list_blocks: list[tuple[float, float, float, float, str, int, int]] = []
document = fitz.open("interactions.pdf")
for page_num in range(2, document.page_count):
    page = document[page_num]
    list_blocks += page.get_text("blocks", sort = True) 
document.close()

infos = extract_infos(list_blocks)
with open("interactions.json", "w") as file:
    file.write("[\n")
    for i in infos:
        file.write(str(i.to_json()) + ",\n")
    file.seek(file.tell() - 2)
    file.write("\n]\n")

# medic = (29.280000686645508, 502.8668518066406, 87.56080627441406, 514.0391845703125, 'ZOPICLONE\n', 37, 0)
# com = (36.720001220703125, 517.9428100585938, 285.3660583496094, 525.763427734375, 'Voir aussi : benzodiazépines et apparentés - hypnotiques - médicaments sédatifs\n', 38, 0)
# interaction = (32.15999984741211, 531.0775146484375, 186.2428436279297, 540.1353759765625, '+ INHIBITEURS PUISSANTS DU CYP3A4\n', 39, 0)
# com1 = (97.44000244140625, 543.9828491210938, 262.92352294921875, 551.803466796875, "Légère augmentation de l'effet sédatif de la zopiclone.\n", 42, 0)
# contrainte = (317.2799987792969, 594.0228271484375, 383.0893249511719, 601.8434448242188, "Précaution d'emploi\n", 44, 0)
# com2 = (317.2799987792969, 605.4228515625, 519.234375, 613.2434692382812, 'Surveillance clinique. Utiliser éventuellement un autre hypnotique.\n', 45, 0)