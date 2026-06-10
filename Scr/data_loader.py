"""Utility functions for loading the CUAD dataset and computing basic statistics.

These helpers are used by notebooks/01_cuad_exploration.ipynb and can be reused
by later pipeline stages (clause extraction, risk scoring, etc.).
"""
import json
from collections import Counter


def load_cuad(path):
    """Load a CUAD JSON file (CUAD_v1.json or the sample) and return its `data` list."""
    with open(path, "r", encoding="utf-8") as f:
        payload = json.load(f)
    return payload["data"], payload.get("version", "unknown")


def category_from_qid(qid):
    """CUAD question ids look like '<title>__<Category>'. Return the category."""
    return qid.split("__")[-1]


def compute_stats(data):
    """Return a dict of headline statistics for a list of CUAD contracts."""
    n_contracts = len(data)
    categories, total_questions, total_annotations, impossible = [], 0, 0, 0
    context_lengths = []
    for contract in data:
        for para in contract["paragraphs"]:
            context_lengths.append(len(para["context"]))
            for qa in para["qas"]:
                total_questions += 1
                cat = category_from_qid(qa["id"])
                if cat not in categories:
                    categories.append(cat)
                n_ans = len(qa["answers"])
                total_annotations += n_ans
                if qa["is_impossible"] or n_ans == 0:
                    impossible += 1
    return {
        "contracts": n_contracts,
        "categories": len(categories),
        "category_names": categories,
        "total_questions": total_questions,
        "total_annotations": total_annotations,
        "impossible": impossible,
        "avg_context_chars": round(sum(context_lengths) / max(len(context_lengths), 1)),
    }


def annotations_per_category(data):
    """Count how many answer spans exist for each category across all contracts."""
    counter = Counter()
    for contract in data:
        for para in contract["paragraphs"]:
            for qa in para["qas"]:
                counter[category_from_qid(qa["id"])] += len(qa["answers"])
    return counter


def contracts_per_category(data):
    """Count in how many contracts each category appears at least once."""
    counter = Counter()
    for contract in data:
        present = set()
        for para in contract["paragraphs"]:
            for qa in para["qas"]:
                if qa["answers"]:
                    present.add(category_from_qid(qa["id"]))
        for cat in present:
            counter[cat] += 1
    return counter


def get_example_clauses(contract, limit=3):
    """Return up to `limit` (category, clause_text) pairs that are present in a contract."""
    out = []
    for para in contract["paragraphs"]:
        for qa in para["qas"]:
            if qa["answers"]:
                out.append((category_from_qid(qa["id"]), qa["answers"][0]["text"]))
                if len(out) >= limit:
                    return out
    return out
