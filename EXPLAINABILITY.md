# Explainability

## Inputs and Data Sources

The agent accepts caller-provided contract clauses, obligation records, clause references, responsible parties, due dates, evidence records, and review notes. It does not access external legal databases or retrieve contracts.

## Decision and Reasoning

The agent organizes supplied obligations, compares each obligation with caller-provided evidence, and identifies missing fields. It does not determine the legal meaning of ambiguous clauses or independently verify the authenticity of evidence.

## Limits and Constraints

The agent does not provide definitive legal advice, certify compliance, interpret jurisdiction-specific law independently, or verify evidence against external systems. Results depend on the accuracy and completeness of supplied materials.

## review-contract-obligations

### Inputs
Caller-provided obligation records and contract references.

### Data Sources
Supplied contract text and obligation metadata only.

### Decision
Checks for missing obligation descriptions, owners, due dates, and clause references.

### Outputs
Structured obligation records and missing fields.

### Failure Handling
Unknown dates or owners are flagged rather than guessed.

### Limits
No definitive legal interpretation.

## map-compliance-evidence

### Inputs
Obligations and caller-provided evidence records.

### Data Sources
Caller-provided records only.

### Decision
Maps evidence by supplied obligation identifier and identifies obligations without linked evidence.

### Outputs
Evidence mappings and gaps.

### Failure Handling
Unmatched evidence is reported.

### Limits
No independent authenticity or sufficiency verification.

## prepare-compliance-action-plan

### Inputs
Obligations, evidence gaps, priorities, and action notes.

### Data Sources
Caller-provided information only.

### Decision
Orders follow-up actions by explicit priority and preserves original order for ties.

### Outputs
Action plan and review notes.

### Failure Handling
Missing owners, dates, or priority are marked unspecified.

### Limits
Action plans are operational aids, not legal determinations.

## Traceability

Observations retain supplied obligation identifiers and clause references.

## Transparency

Explicit contract text, caller interpretations, missing evidence, and recommendations remain distinct.

## Reproducibility

The core is deterministic for identical inputs.

## Safety

The agent avoids fabricated legal requirements and flags ambiguity for qualified review.
