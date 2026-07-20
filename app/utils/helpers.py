from __future__ import annotations

import json
from pathlib import Path
from typing import Any, Dict, List, Tuple


def load_json(path: Path) -> Dict[str, Any]:
    """Load JSON from disk."""
    with path.open("r", encoding="utf-8") as f:
        return json.load(f)


def save_json(path: Path, data: Dict[str, Any]) -> None:
    """Save JSON to disk."""
    with path.open("w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)


def format_score(score: int, max_score: int) -> str:
    """Return a score string like '18 / 20'."""
    return f"{score} / {max_score}"


def format_percentage(value: float) -> str:
    """Return a percentage string like '86.0%'."""
    return f"{value:.1f}%"


def clamp(value: float, minimum: float = 0, maximum: float = 100) -> float:
    """Clamp a value between minimum and maximum."""
    return max(minimum, min(maximum, value))


def normalize_text(value: Any) -> str:
    """Normalize text for comparisons."""
    if value is None:
        return ""
    return str(value).strip().lower()


def answer_label(answer: Any) -> str:
    """Convert raw answer values into user-friendly labels."""
    normalized = normalize_text(answer)
    if normalized == "yes":
        return "Yes"
    if normalized == "partial":
        return "Partial"
    if normalized == "no":
        return "No"
    return "Not answered"


def answer_short_label(answer: Any) -> str:
    """Short label for UI chips or badges."""
    normalized = normalize_text(answer)
    if normalized == "yes":
        return "Yes"
    if normalized == "partial":
        return "Partial"
    if normalized == "no":
        return "No"
    return "—"


def get_gate_percentage(score: int, max_score: int) -> float:
    """Calculate a gate percentage."""
    if max_score == 0:
        return 0.0
    return round((score / max_score) * 100, 1)


def build_progress(current_step: int, total_steps: int) -> float:
    """Return progress as a 0-100 value."""
    if total_steps <= 0:
        return 0.0
    return round((current_step / total_steps) * 100, 1)


def gate_status_text(percentage: float) -> str:
    """Return a simple gate status label."""
    if percentage >= 90:
        return "Strong"
    if percentage >= 75:
        return "Ready"
    if percentage >= 60:
        return "Needs Review"
    return "Not Ready"


def flatten_gates(questions_data: Dict[str, Any]) -> List[Dict[str, Any]]:
    """Flatten all questions across all gates into one list."""
    items: List[Dict[str, Any]] = []

    for gate in questions_data.get("gates", []):
        for question in gate.get("questions", []):
            items.append(
                {
                    "gate_id": gate.get("id"),
                    "gate_title": gate.get("title"),
                    "question_id": question.get("id"),
                    "prompt": question.get("prompt"),
                    "critical": bool(question.get("critical", False)),
                    "help_text": question.get("help_text", ""),
                }
            )

    return items


def get_question_by_id(questions_data: Dict[str, Any], question_id: str) -> Dict[str, Any]:
    """Find a question by ID."""
    for gate in questions_data.get("gates", []):
        for question in gate.get("questions", []):
            if question.get("id") == question_id:
                return {
                    "gate_id": gate.get("id"),
                    "gate_title": gate.get("title"),
                    "question_id": question.get("id"),
                    "prompt": question.get("prompt"),
                    "critical": bool(question.get("critical", False)),
                    "help_text": question.get("help_text", ""),
                }
    return {}


def get_gate_by_id(questions_data: Dict[str, Any], gate_id: str) -> Dict[str, Any]:
    """Find a gate by ID."""
    for gate in questions_data.get("gates", []):
        if gate.get("id") == gate_id:
            return gate
    return {}


def count_questions(questions_data: Dict[str, Any]) -> Tuple[int, int]:
    """
    Return total question count and critical question count.
    """
    total = 0
    critical = 0

    for gate in questions_data.get("gates", []):
        questions = gate.get("questions", [])
        total += len(questions)
        critical += sum(1 for q in questions if q.get("critical", False))

    return total, critical
