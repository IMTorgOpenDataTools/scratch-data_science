

from pathlib import Path
import json


def output_to_pdf():
    """Transform output and convert to PDF."""
    file_path = Path('./output.json')
    with open(file_path, ) as f:
        output = json.load(f)
    lines = output['chunks']
    
    results = []
    
    timestamps = [line['timestamp'] for line in lines]
    stamps = [[-1,-1] for idx in range(len(timestamps))]
    trigger = False
    for idx, stamp in enumerate( range(len(timestamps) )):
        if idx==0:
            stamps[0] = timestamps[0]
        elif (timestamps[idx][0] == timestamps[idx-1][1]) and trigger==False:
            stamps[idx]= timestamps[idx]
        elif trigger==True:
            stamps[idx] = [ (stamps[idx-1])[1], stamps[idx-1][1] + timestamps[idx][1] ]
        else:
            stamps[idx] = [ timestamps[idx-1][1], timestamps[idx-1][1] + timestamps[idx][1] ]
            trigger = True

    for idx in range(len(timestamps)-1):
        item = f'{stamps[idx]}  -  {lines[idx]["text"]} \n'
        results.append(item)

    print( ('').join(results) )
    str_results = ('').join(results)
    text_to_pdf(str_results, 'results.pdf')





import textwrap
from fpdf import FPDF

def text_to_pdf(text, filename):
    a4_width_mm = 210
    pt_to_mm = 0.35
    fontsize_pt = 10
    fontsize_mm = fontsize_pt * pt_to_mm
    margin_bottom_mm = 10
    character_width_mm = 7 * pt_to_mm
    width_text = a4_width_mm / character_width_mm

    pdf = FPDF(orientation='P', unit='mm', format='A4')
    pdf.set_auto_page_break(True, margin=margin_bottom_mm)
    pdf.add_page()
    pdf.set_font(family='Courier', size=fontsize_pt)
    splitted = text.split('\n')

    for line in splitted:
        lines = textwrap.wrap(line, width_text)

        if len(lines) == 0:
            pdf.ln()

        for wrap in lines:
            pdf.cell(0, fontsize_mm, wrap, ln=1)

    pdf.output(filename, 'F')



output_to_pdf()