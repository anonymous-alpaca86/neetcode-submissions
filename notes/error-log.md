# Error Log

## Product of Array Except Self (LeetCode 238)
**Takeaway:** To cut runtime, avoid repeating work. My brute force recomputed
the product of all other elements for every index (nested loop, O(n²)).
Instead, keep a running prefix product (everything left of i) and a running
suffix product (everything right of i), updating each with one multiplication
per step. Two passes through the list, so O(n).
**General pattern:** If a nested loop recomputes something similar each
iteration, ask "can I carry the result forward instead of rebuilding it?"
(prefix sums, running totals, sliding window, hash maps).
