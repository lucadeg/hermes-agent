---
name: product-control-plane-brand-kit-v3
description: Use Brand Kit v3 / Product Control Plane as the pre-development authority for substantial products: premium mockups, deterministic requirements, backend/domain contracts, TDD, Definition of Done, traceability, security/compliance and implementation handoff.
---

# Brand Kit v3 / Product Control Plane

Use before substantial product implementation or redesign.

## Contract
The required chain is:

business intent -> Product Control Plane v3 -> approved premium mockups -> specs/contracts -> tests -> implementation -> verification -> release evidence

Hermes must not equate "I generated a screen" with "the product is specified".

## Intake
Inspect existing repository, docs, assets, product surfaces and runtime architecture first. Reuse real facts. Do not invent missing integrations or readiness.

## Minimum output for substantial digital products
Target 30+ premium mockups:
- 10+ brand/application direction;
- 10+ primary product/customer/workspace;
- 10+ admin/business/governance.

Create deterministic artifacts for routes, surfaces, components, backend, domain/data, APIs/events, roles, states, workflows, tests, Definition of Done, security/privacy/compliance, observability, delivery and traceability.

## Test-driven sequence
1. Stable Feature ID.
2. Link Mock ID(s) + business objective.
3. Define route/surface/roles.
4. Define backend/data/API/event/state contract.
5. Define measurable acceptance criteria.
6. Write failing tests first where practical.
7. Implement smallest correct behavior.
8. Refactor.
9. Run affected validation matrix.
10. Attach DoD evidence.

## Backend completeness
Define functional, technical, strategic and managerial/operational layers before implementation.

## Foundation
For commerce/business apps, Open Mercato is the default application foundation unless the user explicitly chooses another architecture. MVX Hermes Agent itself keeps its native runtime and uses this skill as a project-generation/control-plane workflow.

## Truthfulness
- Do not count placeholders as approved mockups.
- Do not turn generated-image text into exact requirements.
- Do not claim live integrations without evidence.
- Missing evidence remains missing/blocked.
- Do not bypass security/compliance gates for convenience.

## Traceability
Maintain:
Mock ID -> Feature ID -> Route -> Surface -> Backend Module -> Entity/State -> API/Event -> Test IDs -> DoD -> PR/Release.

## Completion
A project can set implementation_gate=allowed only when required visual coverage, deterministic specs, backend completeness, tests and Definition of Done are complete or explicitly waived through an auditable decision.
