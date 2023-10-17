## Pytest and Test Driven Development

## TDD
    # Red
    # Green
    # Refactor

"The tests you write for your program will never catch the errors you don't write tests for"

Write tests before you write the code

*Context --write program bit by bit. One feature, one chunk at a time.

**Red**
1. Write one failing test for functionality you want to implement
2. Run the test.
3. Test will fail because code doesn't exist yet

**Green** 
1. Write minimum code you need to get test to pass.
    a.  YAGNI = "you ain't gonna need it."
        **if you don't need it, don't write it**

**Refactor**
1. Once test passes, refactor code to improve maintainability, readability, and structure while still passing tests.
    a. *Refactoring* means re-writing code without changing its behavior.
    b. "First make it work, then make it right, then make it fast."
    c. "Plan to throw the first one away."

## Why TDD?
    -Reliability
    -Documentation. Tests srve as great living documentation
    -aintainability.
    -Collaboration. TDD and pair programming often go together.
    -Workflow.
    -Regression testing. A **regression** is when a bug is fixed, but then happens again.
        -When we fix a bug we write a "regression test".
        

OODA LOOP

Observe 
Orient
Decide 
Act

This is how to debug

