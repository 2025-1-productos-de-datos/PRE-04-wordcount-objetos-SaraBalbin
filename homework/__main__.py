"""Entry point for the homework package."""

# python -m homework data/input data/output

from .src.main import WordCountApp

if __name__ == "__main__":
    WordCountApp().run()
