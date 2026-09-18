# Research handoff

## Claim

Fixed admissible H, k >= 2: G_H(x) >>_H x(log x)^k / log log x

## Dependencies and recorded support

- **covering** — Covering reduction and parameter choices for the matching construction (formal_deduction_with_inputs; source: gap-note).
- **fixed_shift_rankin** — Fixed-shift covering, exception count and comparison of gap scales (written_argument; source: gap-note).
- **labelled_matching** — Quantitative matching result for repeated, labelled edges (external_input; source: gap-note).
- **selberg** — Fixed-dimensional Selberg upper bound with the required uniformity (external_input; source: gap-note).
- **smooth_numbers** — Smooth-number estimate at the chosen Rankin parameters (external_input; source: gap-note).
- **matching_route** — Original matching construction yields the original bound (formal_deduction_with_inputs; source: gap-note).
- **rankin_route** — The larger Rankin bound implies the original bound for fixed k >= 2 (written_argument; source: gap-note).
- **original_bound** — Fixed admissible H, k >= 2: G_H(x) >>_H x(log x)^k / log log x (written_argument; source: gap-note).

## Dependency rules

- (selberg AND labelled_matching AND covering) → matching_route
- (selberg AND smooth_numbers AND fixed_shift_rankin) → rankin_route
- (matching_route OR rankin_route) → original_bound

## External inputs

- Quantitative matching result for repeated, labelled edges
- Fixed-dimensional Selberg upper bound with the required uniformity
- Smooth-number estimate at the chosen Rankin parameters

## Attempts and questions

### compare-gap-scales · completed

Does the Rankin scale imply the original bound for the same fixed H?

Method: Divide the two expressions and compare powers of log x and log log x.

Check: Keep k fixed and at least 2; retain every iterated logarithm.

Recorded outcome: The ratio is (log x)^(k-1)(log log log x)^k/(log log x)^(2k-1), which tends to infinity.

### application-priority · proposed

Where has this exact fixed-shift application already been established?

Method: Compare definitions and hypotheses of the closest primary results with the full written argument.

Check: A replacement must apply to the identical fixed-H object and deliver at least this scale.

Recorded outcome: Priority is unresolved in the maintained research record; the larger formula is a local derivation.

## Source manifest

SHA-256 of UTF-8 text with LF line endings.

- Graph: `dependency-example.json` — `0cdbe1e666e199b27fea99f2ad821bc0fae8bc8494085e75597a34c3d93bdbd7`
- gap-note: `gap-comparison.md` — `1eb534fed6fc407fe0eb14889f06108f8d448df1c048f90a21c1376f82c6dd28`
