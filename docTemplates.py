from datetime import date
from os import linesep

# import typst as typ


class templateGenerator:
    """
    This class generates templates based on the provided data.
    """

    def __init__(
        self, title, subtitle="", courseCode="", courseTitle="", author="", authorID=""
    ):
        self.title = title
        self.subtitle = subtitle
        self.courseCode = courseCode
        self.courseTitle = courseTitle
        self.author = author
        self.authorID = authorID
        self.subfiles = []
        self.resetDocumentSettings()

    def addSubfiles(self, files: list):
        self.subfiles += files

    def resetDocumentSettings(self) -> None:
        """
        Resets the formatting settings of the document.
        This only really affects the preamble.\n

        Default values:\n
            fontSize = "11pt"\n
            font = "New Computer Modern"\n
            lineLength = "100%"\n
            parJustify = True\n
            headingNumbering = "1.1"
        """
        self.fontSize = "11pt"
        self.font = "New Computer Modern"
        self.lineLength = "100%"
        self.parJustify = True
        self.headingNumbering = "1.1"

    def preamble(self) -> str:
        """
        This function generates the "set" rules before the main body of the document. \n
        These are the default values functions use unless otherwise specified. \n \n

        Default values:\n
            font: New Computer Modern \n
            fontSize: 11pt \n
            parJustify: True \n
            line length: 100% \n
            headingNumbering: "1.1" \n
        """
        preamble = "// Preamble" + linesep
        preamble += f'#set text(font: "{self.font}", size: {self.fontSize})' + linesep
        preamble += (
            f"#set par(justify: {'true' if self.parJustify else 'false'})" + linesep
        )
        preamble += f"#set line(length: {self.lineLength})" + linesep
        preamble += f'#set heading(numbering: "{self.headingNumbering}")' + linesep

        return preamble

    def titlePage(self, outline=True) -> str:
        today = date.today()
        titlepage = ""

        titlepage += (
            "\n// Title page \n "
            "#table(\n"
            "   columns: (1fr,1fr,1fr),\n"
            f"  table.cell(colspan:2, inset: 9pt )[#text(size: 20pt)[{self.courseTitle}]], table.cell(align: center, inset: 9pt)[#text(size: 20pt)[{self.courseCode}]], \n"
            f"  table.cell(colspan:3, inset: 9pt, align: center )[#text(size: 20pt)[{self.title}]],\n"
            "   table.hline(stroke: 2pt),\n"
            f"  [Author:], table.cell(colspan: 2)[{self.author}],\n"
            f"  [ID:], table.cell(colspan: 2)[{self.authorID}],\n"
            f"  [Date:], table.cell(colspan: 2)[#datetime(day: {today.day}, month: {today.month}, year: {today.year}).display()],\n"
            ")\n"
        )
        if outline:
            titlepage += (
                "#line(length: 100%)\n"
                "#text(size: 20pt)[Contents]\n"
                "#outline(title: none)\n"
                "#line(length: 100%)\n"
            )
        titlepage += "#pagebreak()\n\n"

        return titlepage

    def getDocument(self):
        doc = self.preamble()
        doc += self.titlePage()

        if not self.subfiles == []:
            for subfile in self.subfiles:
                with open(str(subfile), "r") as f:
                    doc += f.read()
                    doc += "\n\n"

        return doc

    def writeDocument(self):
        with open(f"{self.title.replace(' ', '_')}.typ", "w") as f:
            f.write(self.getDocument())
