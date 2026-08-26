import argparse

def main(translations_path):
    print("main: " + translations_path)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--translations-path", required=True,
                         help="Path to the ARCH<version> folder, e.g. ARCH1.4.1")
    args = parser.parse_args()
    main(args.translations_path)