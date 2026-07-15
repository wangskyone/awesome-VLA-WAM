#!/usr/bin/env python3
"""Render an animated monthly paper-count chart from README arXiv entries."""

from __future__ import annotations

import argparse
import re
from collections import Counter
from datetime import date
from pathlib import Path

import matplotlib

matplotlib.use("Agg")

from matplotlib import pyplot as plt
from matplotlib.animation import FuncAnimation, PillowWriter


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_README = ROOT / "README.md"
DEFAULT_OUTPUT = ROOT / "assets" / "vla-wam-papers-by-month.gif"
CHART_START_MONTH = date(2026, 1, 1)
ARXIV_ID = re.compile(r"arxiv\.org/abs/(\d{2})(\d{2})\.\d+")

CATEGORY_LABELS = {
    "Agentic Robotics (New Trend)": "Agentic Robotics",
    "Surveys and Definitions": "Surveys & Definitions",
    "World Action Models": "World Action Models",
    "VLA Failure Detection and Correction": "Failure Detection & Correction",
    "Efficient VLA": "Efficient VLA",
    "Benchmarks for Robustness and Evaluation": "Benchmarks & Evaluation",
}
CATEGORY_ORDER = list(CATEGORY_LABELS.values())
CATEGORY_COLORS = {
    "Agentic Robotics": "#8D6CCF",
    "Surveys & Definitions": "#C99C44",
    "World Action Models": "#2BAFA8",
    "Failure Detection & Correction": "#EF6C5C",
    "Efficient VLA": "#438BDB",
    "Benchmarks & Evaluation": "#667887",
}


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--readme", type=Path, default=DEFAULT_README)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    parser.add_argument("--fps", type=int, default=3)
    return parser.parse_args()


def monthly_counts(readme_path: Path) -> Counter[tuple[date, str]]:
    counts: Counter[tuple[date, str]] = Counter()
    category: str | None = None

    for line in readme_path.read_text(encoding="utf-8").splitlines():
        if line.startswith("## "):
            heading = line[3:].split(" ![", 1)[0].strip()
            category = CATEGORY_LABELS.get(heading)
            continue

        if category is None:
            continue

        for year_suffix, month in ARXIV_ID.findall(line):
            month_number = int(month)
            if not 1 <= month_number <= 12:
                continue
            counts[(date(2000 + int(year_suffix), month_number, 1), category)] += 1

    if not counts:
        raise ValueError(f"No arXiv IDs found in {readme_path}")

    return counts


def month_sequence(start: date, end: date) -> list[date]:
    months: list[date] = []
    year, month = start.year, start.month
    while (year, month) <= (end.year, end.month):
        months.append(date(year, month, 1))
        year, month = (year + 1, 1) if month == 12 else (year, month + 1)
    return months


def render(counts: Counter[tuple[date, str]], output_path: Path, fps: int) -> None:
    present_months = sorted(month for month, _ in counts)
    start_month = max(CHART_START_MONTH, present_months[0])
    months = month_sequence(start_month, present_months[-1])
    values_by_month = [
        [counts[(month, category)] for category in CATEGORY_ORDER]
        for month in months
    ]
    x_limit = max(max(values) for values in values_by_month) + 1.25

    figure, axis = plt.subplots(figsize=(12, 6.75), dpi=110)
    figure.patch.set_facecolor("#FCFBF8")
    figure.subplots_adjust(left=0.31, right=0.94, top=0.80, bottom=0.12)
    figure.suptitle(
        "Awesome VLA-WAM: papers added by category",
        x=0.31,
        y=0.96,
        ha="left",
        fontweight="bold",
        fontsize=17,
    )
    month_label = figure.text(
        0.31,
        0.865,
        "",
        color="#4C5966",
        fontsize=13,
        fontweight="bold",
    )
    total_label = figure.text(
        0.94,
        0.865,
        "",
        ha="right",
        color="#4C5966",
        fontsize=11,
    )
    figure.text(
        0.31,
        0.035,
        "Source: arXiv identifiers parsed from README.md",
        fontsize=9,
        color="#697784",
    )

    def draw(frame_index: int) -> None:
        axis.clear()
        values = values_by_month[frame_index]
        bars = axis.barh(
            CATEGORY_ORDER,
            values,
            color=[CATEGORY_COLORS[category] for category in CATEGORY_ORDER],
            height=0.62,
        )
        axis.invert_yaxis()
        axis.set_xlim(0, x_limit)
        axis.set_xlabel("Papers added")
        month_label.set_text(months[frame_index].strftime("%b %Y"))
        total_label.set_text(f"Monthly total: {sum(values)}")

        axis.xaxis.grid(True, color="#D9DEE4", linewidth=0.8)
        axis.set_axisbelow(True)
        axis.spines[["top", "right", "left"]].set_visible(False)
        axis.spines["bottom"].set_color("#AAB3BD")
        axis.tick_params(axis="y", length=0, labelsize=11, colors="#26313C")
        axis.tick_params(axis="x", colors="#4C5966")

        for bar, value in zip(bars, values, strict=True):
            axis.text(
                value + 0.12,
                bar.get_y() + bar.get_height() / 2,
                str(value),
                va="center",
                color="#26313C",
                fontsize=12,
                fontweight="bold",
            )

    animation = FuncAnimation(
        figure,
        draw,
        frames=len(months),
        interval=1000 / fps,
        repeat=True,
    )
    output_path.parent.mkdir(parents=True, exist_ok=True)
    animation.save(output_path, writer=PillowWriter(fps=fps))
    plt.close(figure)


def main() -> None:
    args = parse_args()
    if args.fps < 1:
        raise ValueError("--fps must be at least 1")
    render(monthly_counts(args.readme), args.output, args.fps)


if __name__ == "__main__":
    main()
