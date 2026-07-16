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
from matplotlib.patches import FancyBboxPatch
from matplotlib.ticker import MaxNLocator


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
    "Agentic Robotics": "#7D5CC6",
    "Surveys & Definitions": "#C99C44",
    "World Action Models": "#1FA7A3",
    "Failure Detection & Correction": "#F16A5C",
    "Efficient VLA": "#3F88D6",
    "Benchmarks & Evaluation": "#6B7D8E",
}

BACKGROUND = "#FCFBF8"
PLOT_BACKGROUND = "#FFFFFF"
INK = "#172A46"
MUTED = "#647487"
GRID = "#DCE4EC"
TRACK = "#EEF2F6"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--readme", type=Path, default=DEFAULT_README)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    parser.add_argument(
        "--fps",
        type=float,
        default=0.8,
        help="Animation frame rate; lower values leave more time to read each month.",
    )
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


def render(counts: Counter[tuple[date, str]], output_path: Path, fps: float) -> None:
    present_months = sorted(month for month, _ in counts)
    start_month = max(CHART_START_MONTH, present_months[0])
    months = month_sequence(start_month, present_months[-1])
    values_by_month = [
        [counts[(month, category)] for category in CATEGORY_ORDER]
        for month in months
    ]
    x_limit = max(max(values) for values in values_by_month) + 1.25

    figure, axis = plt.subplots(figsize=(12, 6.75), dpi=110)
    figure.patch.set_facecolor(BACKGROUND)
    figure.subplots_adjust(left=0.31, right=0.94, top=0.77, bottom=0.15)
    figure.suptitle(
        "Awesome VLA–WAM",
        x=0.08,
        y=0.96,
        ha="left",
        fontweight="bold",
        fontsize=20,
        color=INK,
    )
    figure.text(
        0.08,
        0.895,
        "Papers added to the reading list by month and category",
        color=MUTED,
        fontsize=11,
    )
    month_label = figure.text(
        0.94,
        0.925,
        "",
        color="#4C5966",
        fontsize=12,
        fontweight="bold",
        ha="right",
        bbox={
            "boxstyle": "round,pad=0.38",
            "facecolor": "#E9F1F7",
            "edgecolor": "none",
        },
    )
    total_label = figure.text(
        0.94,
        0.875,
        "",
        ha="right",
        color=MUTED,
        fontsize=10,
    )
    figure.text(
        0.08,
        0.045,
        "Source: arXiv identifiers parsed from README.md  ·  Updated monthly",
        fontsize=9,
        color=MUTED,
    )

    def draw(frame_index: int) -> None:
        axis.clear()
        values = values_by_month[frame_index]
        axis.set_facecolor(PLOT_BACKGROUND)
        bar_height = 0.62
        axis.barh(
            CATEGORY_ORDER,
            [x_limit] * len(CATEGORY_ORDER),
            color=TRACK,
            edgecolor="none",
            height=bar_height,
            zorder=1,
        )
        for index, (category, value) in enumerate(
            zip(CATEGORY_ORDER, values, strict=True)
        ):
            if value > 0:
                axis.add_patch(
                    FancyBboxPatch(
                        (0, index - bar_height / 2),
                        value,
                        bar_height,
                        boxstyle=f"round,pad=0,rounding_size={bar_height / 2}",
                        linewidth=0,
                        facecolor=CATEGORY_COLORS[category],
                        zorder=2,
                    )
                )
            axis.text(
                max(value + 0.18, 0.10),
                index,
                str(value),
                va="center",
                color=INK,
                fontsize=11,
                fontweight="bold",
                zorder=3,
            )
        axis.invert_yaxis()
        axis.set_xlim(0, x_limit)
        axis.set_xlabel("Papers added", color=MUTED, labelpad=10)
        month_label.set_text(months[frame_index].strftime("%b %Y"))
        total_label.set_text(f"{sum(values)} papers added")

        axis.xaxis.set_major_locator(MaxNLocator(integer=True, nbins=7))
        axis.xaxis.grid(True, color=GRID, linewidth=0.8, alpha=0.85)
        axis.set_axisbelow(True)
        axis.spines[["top", "right", "left", "bottom"]].set_visible(False)
        axis.tick_params(axis="y", length=0, labelsize=11, colors=INK, pad=14)
        axis.tick_params(axis="x", length=0, colors=MUTED, pad=8)

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
    if args.fps <= 0:
        raise ValueError("--fps must be greater than 0")
    render(monthly_counts(args.readme), args.output, args.fps)


if __name__ == "__main__":
    main()
