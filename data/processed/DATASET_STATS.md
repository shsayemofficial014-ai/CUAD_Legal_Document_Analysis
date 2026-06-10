# CUAD Dataset Statistics

**Dataset:** CUAD — An Expert-Annotated NLP Dataset for Legal Contract Review
**Source:** Hendrycks, Burns, Chen & Ball (UC Berkeley & The Nueva School), NeurIPS 2021 Datasets & Benchmarks Track
**License:** Apache-2.0 · **Download:** https://github.com/TheAtticusProject/cuad (mirror: https://zenodo.org/record/4595826)

I worked out all the numbers below straight from `CUADv1.json` (version `aok_v1.0`) using `src/data_loader.compute_stats()`, rather than copying them from the paper. You can reproduce them yourself by running `notebooks/01_cuad_exploration.ipynb`.

## Headline numbers

| Metric | Value | Notes |
|---|---|---|
| Commercial contracts | **510** | Each is one entry in `data[]` |
| Clause categories | **41** | One question per category, per contract |
| Total questions | **20,910** | 510 contracts × 41 categories |
| Total annotation spans | **13,823** | Highlighted clause spans across all contracts |
| Empty (clause absent) questions | **14,208** | Category not present in that contract |
| Avg. contract length | **~52,563 chars** | Mean `context` length per contract |

A few extra figures from the paper, for context: somewhere over 13,000 expert annotations, 25 contract types, 9,283 pages that were each reviewed at least four times, 70–100 hours of training per annotator, and an estimated annotation value north of **$2 million USD**. One thing to note — the contract *type* isn't actually stored in the JSON, so that 25-type number comes from the paper's own description rather than from anything we can recompute.

## How the JSON is structured

CUAD uses the same extractive question-answering format as SQuAD, which looks like this:

```
{
  "version": "aok_v1.0",
  "data": [
    {
      "title": "LIMEENERGYCO_..._DISTRIBUTOR AGREEMENT",
      "paragraphs": [
        {
          "context": "<full contract text>",
          "qas": [
            {
              "id": "<title>__Document Name",
              "question": "Highlight the parts ... related to \"Document Name\" ...",
              "answers": [ { "text": "DISTRIBUTOR AGREEMENT", "answer_start": 44 } ],
              "is_impossible": false
            }
            // ... 41 questions total, one per category
          ]
        }
      ]
    }
    // ... 510 contracts
  ]
}
```

To get the category for any question, just take the text after the last `__` in its `id` — that little trick saves us keeping a separate mapping.

## The 41 clause categories

I've grouped them into four functional areas to make them easier to read; the numbering keeps the original order they appear in inside the JSON.

**General Information**
1. Document Name
2. Parties
3. Agreement Date
4. Effective Date
5. Expiration Date
6. Renewal Term
7. Notice Period To Terminate Renewal
8. Governing Law
16. Termination For Convenience
18. Change Of Control
41. Third Party Beneficiary

**Restrictive Covenants**
9. Most Favored Nation
10. Non-Compete
11. Exclusivity
12. No-Solicit Of Customers
13. Competitive Restriction Exception
14. No-Solicit Of Employees
15. Non-Disparagement
17. Rofr/Rofo/Rofn
19. Anti-Assignment

**Revenue & Liability**
20. Revenue/Profit Sharing
21. Price Restrictions
22. Minimum Commitment
23. Volume Restriction
34. Audit Rights
35. Uncapped Liability
36. Cap On Liability
37. Liquidated Damages
38. Warranty Duration
39. Insurance
40. Covenant Not To Sue

**IP & Termination**
24. Ip Ownership Assignment
25. Joint Ip Ownership
26. License Grant
27. Non-Transferable License
28. Affiliate License-Licensor
29. Affiliate License-Licensee
30. Unlimited/All-You-Can-Eat-License
31. Irrevocable Or Perpetual License
32. Source Code Escrow
33. Post-Termination Services

If you want the full description of each one, it's in `data/category_descriptions.csv` (that file ships with the dataset). These are the same 41 categories Afnan scores High/Medium/Low in the Person 2 deliverable, so the two pieces line up.
