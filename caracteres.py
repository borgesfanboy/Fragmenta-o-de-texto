import PyPDF2

def ler_pdf(caminho_pdf):
   
    texto = ""
    with open(caminho_pdf, "rb") as arquivo_pdf:
        leitor_pdf = PyPDF2.PdfReader(arquivo_pdf)
        num_paginas = len(leitor_pdf.pages)
        
        for i in range(num_paginas):
            pagina = leitor_pdf.pages[i]
            texto += pagina.extract_text()
    
    return texto

def fragmentar_texto(texto, tamanho_fragmento=1000):

    fragmentos = []
    for i in range(0, len(texto), tamanho_fragmento):
        fragmento = texto[i:i+tamanho_fragmento]
        metadados = {
            'indice_fragmento': i // tamanho_fragmento + 1,
            'inicio': i,
            'fim': i + len(fragmento),
            'fragmento': fragmento
        }
        fragmentos.append(metadados)
    return fragmentos

#exemplo de uso :)
caminho_pdf = "C:\\Users\\visitante\\Downloads\\meu_arquivo.pdf" 




texto_bruto = ler_pdf(caminho_pdf)


fragmentos = fragmentar_texto(texto_bruto)


for fragmento in fragmentos:
    print(f"Fragmento {fragmento['indice_fragmento']} (de {fragmento['inicio']} a {fragmento['fim']}):")
    print(fragmento['fragmento'])
    print()
