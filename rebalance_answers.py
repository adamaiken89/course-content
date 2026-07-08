"""Rebalance MCQ answer letters so no letter >50% and no 3+ consecutive same.

Permutes option key assignments per question; option texts preserved exactly.
Handles quiz.yaml (all items) and cumulative_quiz_*.yaml (type==mcq items).
"""
import json
import os
from pathlib import Path
import sys

import yaml

LETTERS = 'abcd'


def target_seq(n):
    return ('abcd' * (n // 4 + 1))[:n]


def rebalance(items, only_mcq=False):
    mcq_idx = [i for i, q in enumerate(items)
               if isinstance(q, dict) and q.get('options')
               and (not only_mcq or q.get('type') == 'mcq')]
    seq = target_seq(len(mcq_idx))
    for idx, target in zip(mcq_idx, seq):
        q = items[idx]
        opts = q['options']
        correct = q['answer']
        if correct not in opts:
            continue
        correct_text = opts[correct]
        others = [opts[k] for k in LETTERS if k != correct]
        new_opts = {}
        rest = [k for k in LETTERS if k != target]
        for j, k in enumerate(rest):
            new_opts[k] = others[j]
        new_opts[target] = correct_text
        q['options'] = {k: new_opts[k] for k in LETTERS}
        q['answer'] = target
    return items


def _norm_qid(qid):
    if isinstance(qid, (int, float)):
        return str(qid)
    parts = str(qid).split('.')
    norm = parts[0].lstrip('0') or '0'
    if len(parts) > 1:
        norm += '.' + '.'.join(parts[1:])
    return norm


def sync_deck(course):
    deck_path = course / 'srs' / 'deck.json'
    if not deck_path.exists():
        return
    deck = json.loads(deck_path.read_text())
    cards = deck.get('cards', {})
    changed = 0
    for cid, card in cards.items():
        qid = _norm_qid(card.get('questionId', ''))
        module = card.get('moduleId', '')
        mod_dirs = [d for d in (course / 'modules').iterdir() if d.is_dir()]
        match = next((d for d in mod_dirs if d.name.startswith(f'{module}-') or d.name == module), None)
        if not match:
            continue
        quiz_path = match / 'quiz.yaml'
        if not quiz_path.exists():
            continue
        qs = yaml.safe_load(quiz_path.read_text())
        q = next((q for q in qs if _norm_qid(q.get('id', '')) == qid), None)
        if not q or not q.get('options'):
            continue
        letter = q['answer']
        text = q['options'].get(letter, '')
        if text:
            card['answer'] = f'{letter}. {text}'
            changed += 1
    if changed:
        deck_path.write_text(json.dumps(deck, ensure_ascii=False, indent=2))
        print(f'  deck synced: {changed} cards')


def main():
    for path in sys.argv[1:]:
        course = os.path.dirname(os.path.dirname(path))
        with open(path) as f:
            data = yaml.safe_load(f)
        only_mcq = 'cumulative' in path
        rebalance(data, only_mcq=only_mcq)
        with open(path, 'w') as f:
            yaml.safe_dump(data, f, allow_unicode=True, sort_keys=False, default_flow_style=False)
        print(f'rebalanced {path}')
        if os.path.basename(path) == 'quiz.yaml':
            course = Path(os.path.dirname(path)).parent.parent
            sync_deck(course)


if __name__ == '__main__':
    main()
