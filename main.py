from fpdf import FPDF

import pandas as pd

df = pd.read_csv("topics.csv")

pdf = FPDF(orientation="P",format="A4",unit="mm")

pdf.set_auto_page_break(auto= False, margin=0)


for index,row in df.iterrows():

    pdf.add_page()

    pdf.set_font(family="Times",style="B",size=24)

    pdf.set_text_color(100,100,100)

    pdf.cell(w=0,h=12,align="L",txt=row["Topic"],ln=1)
    pdf.line(7,21,200,21)

    for y in range(20,298,20):
        pdf.line(20,y,200,y)

    # set footer
    pdf.ln(272)

    pdf.set_font(family="Times",style="I",size=8)
    pdf.set_text_color(180, 180, 180)
    pdf.cell(w=0, h=10, align="R", txt=row["Topic"], ln=1)

    for i in range(row["Pages"] - 1):

        pdf.add_page()
        # set footer
        pdf.ln(265)

        pdf.set_font(family="Times", style="I", size=8)
        pdf.set_text_color(180, 180, 180)
        pdf.cell(w=0, h=10, align="R", txt=row["Topic"], ln=1)

        for y in range(20, 298, 20):
            pdf.line(20, y, 200, y)

pdf.output("output.pdf")


