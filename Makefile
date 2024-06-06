.PHONY: all clean

BMP = data/frames/bmp
SVG = data/frames/svg
FONT = out/bad_apple.ttf

all: $(FONT)
	@echo "Done!"

$(BMP): 
	@echo "Generating frames..."
	@mkdir -p data/frames/bmp
	@python3 src/generate_frames.py

$(SVG): $(BMP)
	@echo "Converting frames to SVG..."
	@mkdir -p data/frames/svg
	@potrace --svg data/frames/bmp/*.bmp
	@mv data/frames/bmp/*.svg data/frames/svg/

$(FONT): $(SVG)
	@echo "Exporting font..."
	@fontforge -lang=py -script src/generate_font.py

clean:
	@rm -f data/frames/* out/*