import toml

# import typst as typ
from docTemplates import templateGenerator


def main() -> None:
    with open("sliderdoc.toml", "r") as f:
        config = toml.load(f)

    author = config["parameters"]["author"]
    authorID = config["parameters"]["authorID"]
    documentTitle = config["parameters"]["title"]
    courseName = config["parameters"]["courseName"]
    courseCode = config["parameters"]["courseCode"]

    tg = templateGenerator(
        title=documentTitle,
        author=author,
        courseCode=courseCode,
        courseTitle=courseName,
        authorID=authorID,
    )

    tg.addSubfiles(config["document"]["subfiles"])

    tg.writeDocument()


if __name__ == "__main__":
    main()
