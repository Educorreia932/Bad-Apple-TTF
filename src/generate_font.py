import fontforge
import os


def generate_font():
    font = fontforge.font()

    font.encoding = "UnicodeFull"
    font.familyname = "BadApple"
    font.fontname = "BadApple"
    font.fullname = "BadAppleRegular"

    codepoint = 0xF0000
    frames = os.listdir("data/frames/svg")

    for frame in frames:
        glyph = font.createMappedChar(codepoint)
        glyph.importOutlines(f"data/frames/svg/{frame}", ("removeoverlap", "correctdir"))
        glyph.removeOverlap()

        codepoint += 1

    font.generate("out/bad_apple.ttf")


if __name__ == "__main__":
    generate_font()
