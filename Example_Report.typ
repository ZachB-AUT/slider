// Preamble
#set text(font: "New Computer Modern", size: 11pt)
#set par(justify: true)
#set line(length: 100%)
#set heading(numbering: "1.1")

// Title page
 #table(
   columns: (1fr,1fr,1fr),
  table.cell(colspan:2, inset: 9pt )[#text(size: 20pt)[Example Course]], table.cell(align: center, inset: 9pt)[#text(size: 20pt)[EXPL101]],
  table.cell(colspan:3, inset: 9pt, align: center )[#text(size: 20pt)[Example Report]],
   table.hline(stroke: 2pt),
  [Author:], table.cell(colspan: 2)[Zach Barrett],
  [ID:], table.cell(colspan: 2)[22160418],
  [Date:], table.cell(colspan: 2)[#datetime(day: 20, month: 11, year: 2025).display()],
)
#line(length: 100%)
#text(size: 20pt)[Contents]
#outline(title: none)
#line(length: 100%)
#pagebreak()

= Heading 1
#lorem(100)

= Heading 2
#lorem(100)

= Heading 3
#lorem(100)

