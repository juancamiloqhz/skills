# Type rule reference for this fixture

The `operator` diagnostic checks whether operand types support an operation. In this fixture, an integer plus a string is invalid and raises `TypeError` in Python. The `type: ignore[operator]` comment suppresses that correctness diagnostic; it is not a style exception. A runtime example can establish the concrete failure independently of a static checker. No type-checker installation is supplied or required for this fixture.
