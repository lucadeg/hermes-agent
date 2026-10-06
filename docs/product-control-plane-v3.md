# MVX Hermes Agent — Brand Kit v3 / Product Control Plane

This fork treats Brand Kit v3 as a reusable project-generation skill and as its own pending brand/control-plane specification.

## Agent behavior
When a user asks Hermes to build a substantial product, Hermes should first determine whether a v3 control plane exists. If it does not:
1. create/discover the Brand Kit v3 workspace;
2. define premium mock coverage;
3. define deterministic product/backend/test contracts;
4. keep implementation blocked until the required evidence is approved.

For small, clearly bounded changes, this gate can be proportionate rather than forcing a 30-board kit.

## Project-specific state
The MVX Hermes Agent brand-kit workspace is under:
`brand-kits/mvx-hermes-agent/v3/`

Its current state is intentionally blocked because the premium visual identity and complete frontend/control surfaces still need to be designed.

## Integration with Hermes skills
The bundled skill lives at:
`skills/product-control-plane-brand-kit-v3/SKILL.md`

It relies on existing Hermes tools for filesystem inspection, image/design workflows, coding, tests and repository operations. No special vendor integration is required.
