# Appendix L — State Transition Model

Specified
    │
    ▼
Governed
    │
    ▼
Executing
    │
    ├────────► Drift Detected
    │               │
    ▼               ▼
Verified ◄──── Corrected
    │
    ▼
Archived

State transitions describe governance behavior conceptually and are independent
of any implementation.
