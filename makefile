all:
	uv run main.py
	typst compile Example_Report.typ
	open ExampleReport.pdf

clean:
	rm Example_Report.*