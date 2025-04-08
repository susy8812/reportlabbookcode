from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import landscape, A4
from reportlab.lib.units import cm

# Nome del file PDF di output
pdf_file = "tempario_presentazione.pdf"

# Funzione per disegnare una slide
def draw_slide(c, title, content_lines):
    c.setFont("Helvetica-Bold", 20)
    c.drawCentredString(landscape(A4)[0] / 2, landscape(A4)[1] - 3 * cm, title)
    c.setFont("Helvetica", 14)
    text = c.beginText(2 * cm, landscape(A4)[1] - 5 * cm)
    for line in content_lines:
        text.textLine(line)
    c.drawText(text)
    c.showPage()

# Crea il canvas in modalità landscape
c = canvas.Canvas(pdf_file, pagesize=landscape(A4))
page_width, page_height = landscape(A4)

# Slide 1 – Titolo e Introduzione
slide_title = "Analisi del Tempario di Lavorazione delle Pratiche\nMiglioramenti del Flusso Informatizzato"
slide_content = [
    "Periodo Analizzato: (focus su Marzo e Aprile 2025)",
    "",
    "Obiettivi:",
    "- Presentare i dati relativi al numero di pratiche, tempi medi e distribuzione degli stati",
    "- Dimostrare l’effetto positivo della modifica del flusso informatizzato"
]
draw_slide(c, slide_title, slide_content)

# Slide 2 – Riepilogo Generale
slide_title = "Riepilogo Generale"
slide_content = [
    "• Totale pratiche gestite nel periodo considerato",
    "• Percentuale di pratiche entro tempo standard vs. fuori tempo standard",
    "• Tabella riepilogativa per tipologia di ticket"
]
draw_slide(c, slide_title, slide_content)

# Slide 3 – Analisi dei Tempi Medi per Tipologia di Pratica
slide_title = "Tempi Medi per Tipologia di Pratica"
slide_content = [
    "• Grafico a barre che mostra il tempo medio di risoluzione per:",
    "  - Immatricolazione",
    "  - Revisione Veicolo",
    "  - Trasferimento",
    "",
    "• Evidenzia miglioramenti in Marzo e Aprile 2025"
]
draw_slide(c, slide_title, slide_content)

# Slide 4 – Distribuzione degli Stati delle Pratiche
slide_title = "Distribuzione degli Stati delle Pratiche"
slide_content = [
    "• Grafico a torta per la distribuzione:",
    "  - Pratiche \"ok rispetto tempo standard\"",
    "  - Pratiche \"Fuori tempo standard\"",
    "",
    "• Evidenzia incremento delle pratiche in tempo nei mesi recenti"
]
draw_slide(c, slide_title, slide_content)

# Slide 5 – Trend Mensile delle Pratiche
slide_title = "Trend Mensile delle Pratiche"
slide_content = [
    "• Grafico lineare/barre dei ticket per anno-mese",
    "• Mostrare il volume di pratiche mese per mese",
    "• Focus sul trend: Marzo e Aprile 2025 vs. mesi precedenti"
]
draw_slide(c, slide_title, slide_content)

# Slide 6 – Confronto Tempi di Lavorazione: Marzo-Aprile 2025 vs. Altri Mesi
slide_title = "Confronto Tempi di Lavorazione"
slide_content = [
    "• Confronto del tempo medio di risoluzione:",
    "  - Marzo e Aprile 2025",
    "  - Altri mesi del 2025",
    "",
    "• Dimostrazione dell’efficacia della modifica del flusso informatizzato",
    "  (riduzione significativa dei tempi medi)"
]
draw_slide(c, slide_title, slide_content)

# Slide 7 – Conclusioni e Prospettive
slide_title = "Conclusioni e Prospettive"
slide_content = [
    "• Riassunto dei risultati:",
    "  - Maggiore efficienza in Marzo e Aprile 2025",
    "  - Impatto positivo del nuovo flusso informatizzato",
    "",
    "• Prospettive:",
    "  - Consolidamento della digitalizzazione",
    "  - Ulteriori interventi di miglioramento",
    "",
    "Spazio per domande e discussioni"
]
draw_slide(c, slide_title, slide_content)

# Salva il PDF
c.save()
print("Il PDF 'tempario_presentazione.pdf' è stato generato con successo!")
