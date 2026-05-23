# Cysca QA Notes

## Working assumptions

This skill is designed for QA work on complex systems where:

- multiple subsystems or services interact
- software, electronics, and integration concerns may coexist
- integration boundaries matter
- defects may appear only under timing, state, or recovery conditions
- traceability and evidence are important
- automation must be selected carefully, not forced everywhere

## Default QA priorities

1. Requirements clarity
2. Risk coverage
3. Interface and integration behavior
4. Safety and reliability
5. Failure handling and recovery
6. Regression safety
7. Observability and evidence

## Domain-specific concerns from Cysca's portfolio

- public transit and mobility systems
- building management and monitoring
- defense-oriented reliability and security
- industrial automation and control
- hardware/software systems with certification or compliance constraints

## Questions to ask early

- What is the system boundary?
- What are the critical workflows?
- Which integrations are in scope?
- Is hardware involved, and if so, what environmental or endurance conditions matter?
- What failure modes matter most?
- What environments are available?
- What evidence is required for sign-off?
- What should be automated first?

## Reporting format

- Observation
- Risk or impact
- Reproduction steps
- Expected result
- Actual result
- Environment
- Evidence
- Severity / priority

## Automation guidance

- Automate stable, repeatable checks first.
- Do not automate around unstable requirements.
- Favor integration and end-to-end coverage for critical paths.
- Keep test data and environment dependencies explicit.
- Add checks for protocol compatibility, device interoperability, and recovery behavior where applicable.
