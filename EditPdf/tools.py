from re import I
import PyPDF2
from PyPDF2 import PdfFileWriter, PdfFileReader
import io
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
import os
import sys

def setup():
    dir_path = os.path.dirname(os.path.realpath(__file__))
    dir_path = dir_path.split("\\")[:-1]
    dir_path.append("PrinterDriver")
    sys.path.append("\\".join(dir_path))

setup()
import DriverTools

class Edit:
    def __init__(self):
        pass

    def files_pages(self, location):
        file = open(location, 'rb')
        readpdf = PyPDF2.PdfFileReader(file)
        return readpdf.numPages

    def find_target_address(self):
        dir_path = os.path.dirname(os.path.realpath(__file__))
        dir_path = dir_path.split("\\")[:-1]
        dir_path.append("TempPdf")
        dir_path.append(DriverTools.generate_name("\\".join(dir_path)))
        
        return "\\".join(dir_path)+".pdf"

    def make_first_page(self, info={}):
        packet = io.BytesIO()
        can = canvas.Canvas(packet, pagesize=A4)
        can.drawString(340, 731, info["question_code" ])
        can.drawString(340, 709, info["major" ])
        can.drawString(340, 687, info["question_type"])

        can.drawString(165, 731, info["recive_time" ])
        can.drawString(165, 709, info["price" ])

        can.drawString(40, 731, info["team_code" ])
        can.drawString(40, 709, info["team_name" ])
        can.drawString(40, 687, info["score"])
        can.save()
        packet.seek(0)
        new_pdf = PdfFileReader(packet)
        return new_pdf

    def make_other_pages(self, info={}):
        packet = io.BytesIO()
        can = canvas.Canvas(packet, pagesize=A4)
        can.drawString(445, 733, info["question_code"])
        can.drawString(260, 733, info["team_code"])
        can.save()
        packet.seek(0)
        new_pdf = PdfFileReader(packet)
        return new_pdf
   
    def render(self, origin_location, target_location, info={}):
        existing_pdf = PdfFileReader(open(origin_location, "rb"))
        output = PdfFileWriter()
        # add the "watermark" (which is the new pdf) on the existing page
        page1 = existing_pdf.getPage(0)
        page1.mergePage(self.make_first_page(info).getPage(0))
        output.addPage(page1)

        for i in range(1, self.files_pages(origin_location)):
            pages = existing_pdf.getPage(i)
            pages.mergePage(self.make_other_pages(info).getPage(0))
            output.addPage(pages)

        # finally, write "output" to a real file
        outputStream = open(target_location, "wb")
        output.write(outputStream)
        outputStream.close()

if __name__ == "__main__":
    info = {
        "question_code" : "12345",
        "major": "riazi",
        "question_type": "hard",
        "recive_time": "20:20:20",
        "price":"2",
        "team_code":"1008",
        "team_name":"amazing men",
        "score":"10",
        "last_info" : {"1003":"20", "1004":"20", "500":"10"}
    }

    temp = Edit()
    print(temp.files_pages(r"\\wsl$\Ubuntu\home\trx\Printer-Server\Questions\set1\1.pdf"))
    print(temp.find_target_address())
    temp.render(r"\\wsl$\Ubuntu\home\trx\Printer-Server\Questions\set1\1.pdf"
    , temp.find_target_address(), info)