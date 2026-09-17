# FAQ

## Why do text-to-SQL benchmark scores disagree?
Mostly grading rules and answer shape. BIRD and Spider 1.0 headline exact result match, which rewards tight answers; Spider 2.0 headlines got-the-facts, which rewards wide ones. A system that adds context columns drops on the first and rises on the second without changing capability.

## Does text-to-SQL accuracy on a benchmark predict accuracy on my database?
Not reliably. Accuracy varies widely between schemas even inside one benchmark, so the only number that predicts your result is one measured on your own schemas and questions.

## What is a case-flip rate?
The share of questions whose correct/incorrect verdict changes across repeated identical runs. It measures whether you get the same answer twice.

## Why report refusal rate with accuracy?
A system that never declines can look more accurate than one that declines the questions it would get wrong. Refusal rate, and whether refusals are calibrated, is the check on any accuracy figure.

## What is a certified semantic layer?
Business definitions, join paths and value mappings reviewed by someone accountable for the data, as opposed to raw DDL or auto-generated descriptions.
