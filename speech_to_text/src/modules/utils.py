

from pathlib import Path
import json





#TODO:determine valididty of audio files
#ref: https://librosa.org/doc/main/generated/librosa.util.valid_audio.html



def output_to_pdf(lines, filename=None, output_type='file'):
    """Transform output and convert to PDF.
    file_path = Path('./output.json')
    with open(file_path, ) as f:
        output = json.load(f)
    lines = output['chunks']

    'results.pdf'
    """
    results = []
    
    timestamps = [line['timestamp'] for line in lines]
    stamps = [[-1,-1] for idx in range(len(timestamps))]
    trigger = False
    for idx in range(len(timestamps)):
        if idx==0:
            stamps[0] = timestamps[0]
        elif (timestamps[idx][0] == timestamps[idx-1][1]) and trigger==False:
            stamps[idx]= timestamps[idx]
        elif trigger==True:
            stamps[idx] = [ (stamps[idx-1])[1], stamps[idx-1][1] + timestamps[idx][1] ]
        else:
            stamps[idx] = [ timestamps[idx-1][1], timestamps[idx-1][1] + timestamps[idx][1] ]
            trigger = True

    for idx in range(len(timestamps)):
        item = f'{stamps[idx]}  -  {lines[idx]["text"]} \n'
        results.append(item)

    #print( ('').join(results) )
    str_results = ('').join(results)
    pdf = text_to_pdf(str_results)

    if output_type=='file':
        pdf.output(filename, 'F')
        return True
    elif output_type=='str':
        return pdf
    else:
        raise TypeError(f'argument "output_type" must be: "file" or "str"; parameter provided: {output_type}')


import textwrap
from fpdf import FPDF

def text_to_pdf(text):
    """Convert text to PDF object.
    
    ref: https://stackoverflow.com/questions/10112244/convert-plain-text-to-pdf-in-python
    """
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

    return pdf



if __name__ == "__main__":
    output_to_pdf()