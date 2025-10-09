Review Date: 09/10/25
Paper Link: [Anchors: High Precision Model-Agnostic Explanations](https://www.cl.cam.ac.uk/teaching/2425/L193/files/pres1-sonia.pdf)

Anchors are if-then rules that give a reliable prediction locally around a specific data point. This is such that no matter what the other features are, the model will still make the same prediction. 

How do anchors work in simple terms?
1. Pick a specific data point.
2. Find a short rule as the anchor. For example, a few feature conditions that make the model's prediction very reliable locally.
3. Test it by generating similar examples that match those conditions and see if the prediction stays the same.
4. Keep expanding until the rule is small, precise and reliable.

Anchors as high-precision explanations
- The goal of local model-agnostic interpretebility is to explain the behaviours of an individual prediction corresponding to an intance.
- It assumes when the model is globally to complex, we can explain it more rigidly by zooming in on an individual prediction to make the explanation more feasible.

1. Precision 
- "If an anchor rule A holds, how often does the model give the same prediction?"
- E.g. We want this to be over a given threshold such as 0.95.
- These formally ensure with high confidence that
  $P(precision(A) \geq t) \geq 1 - \delta $

2. Coverage
- How often does rule A hold over all data?
  $coverage(A) = P(A(x') = 1)$
- We want high coverage, meaning the anchor applies to many instances but still keeps precision >= threshold.

Efficient Search via Beam Search and Multi-armed Bandits
- Anchors search space is huge (all combinations of feature conditions).
- They build anchors step-by-step, adding one condition at a time.
- They use beam search to keep only the most promising candidate anchors per iteration.

Note: Beam Search is a middle ground method for navigating through a large search spaces that tries to opimize the solution whilst also taking account of memory needed. (Beam width tells you how many most-likely entities in the search space to consider at the same time.)





