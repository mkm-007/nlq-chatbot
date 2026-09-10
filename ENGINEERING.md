# Implementation notes

A small intent vocabulary keeps the query path inspectable. Unknown requests fail explicitly rather than silently returning unrelated records. Department values use bound parameters. A separate read-only connection and SQLite authorizer limit query execution to the employee table; a progress handler and result limit bound work.

Tests use temporary databases so they do not depend on, or change, the visitor's demo records. Coverage includes all three query types, invalid questions, attempted writes, metadata access, and repeatable initialization.
