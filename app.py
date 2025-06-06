import sys

import translation_agent as ta


def convert(full_path, output_path):
    source_lang, target_lang, country = "English", "Chinese", "China"
    with open(full_path, encoding="utf-8") as file:
        source_text = file.read()

    translation = ta.translate(
        source_lang=source_lang,
        target_lang=target_lang,
        source_text=source_text,
        country=country,
    )
    if output_path:
        with open(output_path, "w", encoding="utf-8") as file:
            file.write(translation)
    else:
        print(f"Translation:\n\n{translation}")


if __name__ == "__main__":
    if len(sys.argv) == 1:
        print("please provide a path to a text file")
        sys.exit(-1)

    full_path = sys.argv[1]

    output_path = sys.argv[2] if len(sys.argv) == 3 else None
    convert(full_path, output_path)
