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

def lire_pdf_avec_metadonnees(pdf_path):
    # Ouvrir le fichier PDF
    document = fitz.open(pdf_path)

    # Parcourir toutes les pages du document
    for page_num in range(document.page_count):
        page = document[page_num]

        # Obtenir les informations sur le texte
        blocks = page.get_text("blocks", sort = True)
        
        

    # Fermer le document
    document.close()

# Utilisation de la fonction pour lire le PDF avec métadonnées
pdf_path = "interactions.pdf"
lire_pdf_avec_metadonnees(pdf_path)
