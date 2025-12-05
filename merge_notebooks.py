import nbformat
from pathlib import Path
from typing import List

def merge_notebooks(input_paths: List[Path], output_path: Path) -> None:
    merged_nb = nbformat.v4.new_notebook()
    merged_cells = []
    for ipath in input_paths:
        print(f"Reading {ipath.name} …")
        nb = nbformat.read(str(ipath), as_version=4)
        merged_cells.extend(nb.cells)
    merged_nb.cells = merged_cells
    nbformat.write(merged_nb, str(output_path))

if __name__ == "__main__":
    notebooks = [
        Path("lectures/lecture-1/lecture-1.ipynb"),
        Path("lectures/lecture-2/lecture-2.ipynb"),
        Path("lectures/lecture-3/lecture-3.ipynb"),
        Path("lectures/lecture-4/lecture-4.ipynb"),
        Path("lectures/lecture-5/lecture-5.ipynb"),
        Path("lectures/lecture-6/lecture-6.ipynb"),
        Path("lectures/lecture-7/lecture-7.ipynb"),
    ]
    merge_notebooks(notebooks, Path("midterm/lectures.ipynb"))