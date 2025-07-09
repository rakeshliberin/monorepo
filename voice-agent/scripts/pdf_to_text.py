from markitdown import MarkItDown


def main():
    md = MarkItDown()
    result = md.convert("./fake-server/pdf/4000569504.pdf")
    print(result.text_content)


if __name__ == "__main__":
    main()
