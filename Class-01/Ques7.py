def extract_extensions(filenames):
    extensions = set()

    files = filenames.split(",")

    for file in files:
        file = file.strip()

        extension = file.split(".")[-1].upper()

        extensions.add(extension)

    return list(extensions)


filenames = "report.pdf, image.JPG, data.csv, notes.txt, photo.jpg"

print(extract_extensions(filenames))