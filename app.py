import os
import sys

import translation_agent as ta


if __name__ == "__main__":
    if len(sys.argv) == 1:
        print("please provide a path to a text file")
        sys.exit(-1)

    source_lang, target_lang, country = "English", "Chinese", "China"

    relative_path = sys.argv[1]

    script_dir = os.path.dirname(os.path.abspath(__file__))

    full_path = os.path.join(script_dir, relative_path)

    with open(full_path, encoding="utf-8") as file:
        source_text = file.read()

    translation = ta.translate(
        source_lang=source_lang,
        target_lang=target_lang,
        source_text=source_text,
        country=country,
    )
    if len(sys.argv) == 3:
        output_path = sys.argv[2]
        with open(output_path, "w", encoding="utf-8") as file:
            file.write(translation)
    else:
        print(f"Translation:\n\n{translation}")
