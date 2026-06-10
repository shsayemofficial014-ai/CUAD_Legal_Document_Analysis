# data/

This folder holds the CUAD dataset and a few things derived from it.

## What's committed here

- `category_descriptions.csv` — the official description of each category (small, ships with CUAD).
- `DATASET_STATS.md` — the verified statistics and the full list of 41 categories.
- `sample/cuad_sample_5.json` — a small 5-contract slice (with the contract text trimmed) so the notebook runs even before you download anything.

## What you need to download

The full dataset is around 39 MB, which is too big to keep in the repo, so it's git-ignored. Grab it once with:

```bash
python data/download_cuad.py
```

That pulls down and unpacks three files:

- `CUADv1.json` — all 510 contracts, each with its 41 annotated categories (this is the main one).
- `test.json` — the held-out test split.
- `train_separate_questions.json` — the training split with one example per question.

Once those are in place, the notebook automatically uses the full `CUADv1.json` instead of the sample.
