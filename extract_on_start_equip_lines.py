import argparse
from pathlib import Path

START_MARKER = "OnStartEquip = function()"
DEFAULT_INPUT = Path("Input") / "equipmentproperties.txt"
DEFAULT_OUTPUT = Path("Dev") / "OnStartEquipSortedLines.txt"


def read_lines_with_fallback(input_path: Path) -> list[str]:
    encodings = ["utf-8", "utf-8-sig", "cp950", "big5", "latin-1"]
    last_error = None

    for encoding in encodings:
        try:
            with input_path.open("r", encoding=encoding) as f:
                return f.readlines()
        except UnicodeDecodeError as ex:
            last_error = ex

    raise RuntimeError(f"無法讀取檔案編碼: {input_path}") from last_error


def extract_lines(lines: list[str], unique: bool = True, keep_blank: bool = False) -> list[str]:
    collected: list[str] = []
    in_block = False
    start_indent = 0

    for raw_line in lines:
        line = raw_line.rstrip("\r\n")
        stripped = line.strip()
        indent = len(line) - len(line.lstrip())

        if not in_block and stripped == START_MARKER:
            in_block = True
            start_indent = indent
            if stripped or keep_blank:
                collected.append(stripped)
            continue

        if in_block:
            if stripped or keep_blank:
                collected.append(stripped)

            # 以和 function 起始行相同縮排的 end 視為函式結束
            if stripped == "end" and indent == start_indent:
                in_block = False

    if unique:
        collected = sorted(set(collected))
    else:
        collected.sort()

    return collected


def write_output(output_path: Path, rows: list[str]) -> None:
    output_path.parent.mkdir(parents=True, exist_ok=True)
    with output_path.open("w", encoding="utf-8", newline="\n") as f:
        f.write("\n".join(rows))
        if rows:
            f.write("\n")


def main() -> None:
    parser = argparse.ArgumentParser(
        description="擷取 OnStartEquip = function() 到對應 end 的每行內容，排序後輸出為 txt。"
    )
    parser.add_argument("--input", default=str(DEFAULT_INPUT), help="輸入檔案路徑")
    parser.add_argument("--output", default=str(DEFAULT_OUTPUT), help="輸出檔案路徑")
    parser.add_argument(
        "--keep-duplicate",
        action="store_true",
        help="保留重複行（預設會去重複）",
    )
    parser.add_argument(
        "--keep-blank",
        action="store_true",
        help="保留空白行（預設會略過）",
    )

    args = parser.parse_args()

    base_dir = Path(__file__).resolve().parent
    input_path = (base_dir / args.input).resolve()
    output_path = (base_dir / args.output).resolve()

    if not input_path.exists():
        raise FileNotFoundError(f"找不到輸入檔案: {input_path}")

    lines = read_lines_with_fallback(input_path)
    extracted = extract_lines(
        lines,
        unique=not args.keep_duplicate,
        keep_blank=args.keep_blank,
    )
    write_output(output_path, extracted)

    print(f"完成，已輸出 {len(extracted)} 行到: {output_path}")


if __name__ == "__main__":
    main()
