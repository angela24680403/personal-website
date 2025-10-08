
# Geometric Foundations of Deep Learning 
## Lecture 0: Introduction

Fundamental principles underlying deep learning architectures:
- Symmetry
- Euclidean Geometry
- Projective Geometry
- Non-Euclidean Geometry
- The Erlangen Programme
- Group Theory
- Hyperbolic Geometry
- Category Theory
- Noether's Theorem
- Gauge Invariance
- Unification of forces

Early Neural Networks and the AI Winter:
- Perceptron
- The XOR Affair
- AI Winter
- Group Invariance Theorem
- Deep Learning
- Universal Approximation
- The Curse of Dimensionality
- The Lighthill Report

The Emergence of Geometric Architectures
- Secrets of Visual Cortex
- Neocognitron
- Convolutional Neural Networks
- Recurrent Neural Networks
- Long Short Term Memory
- Time Warping
- Computer Vision
- ImageNet
- AlexNet

Graph Neural Networks and their Chemical Precursors
- Structural Similarity of Molecules
- Graph Theory and Chemistry
- Weisfeiler-Lehman Test
- First Graph NN

## Lecture 1: Introduction to Groups and Representations

Learning in high dimensions
- In general, learning functions in high dimensions is intractable. Number of samples required grows exponentially with dimensions
- We can inject assumptions about geometry through inductive biases. Restrict the functions to ones that respect the geometry.
- This can make the high-dimensional problem more tractable.

Some popular examples:
- Image data should be processed independently of shifts.
- Spherical data should be processed independently of rotations.
- Graph data should be processed independently of isomorphism.

A roadmap for our formalisation:
1. Data domains: define where the data lives.
2. Signals: define how data is represented or featurised.
3. Formalize symmetries: Identify the transformations that preserve the structure of the domain. These form groups.
4. Define group actions: describe how these groups act on the data domain i.e. how symmetries transform data.

The Space of Sygnals on a Geometric Domain
Vextor Space Structure of Signals

Symmetries
- A symmetry of an object is a transformation of that object that leaves it unchanged.

Symmetry Group
- A symmetry of an object is a transformation of that object that leaves it unchanged.
- The idensity transformation is always symmetry.
- Given two symmetry transformations, their composition is also a symmetry.
- Given any symmetry, it must be invertible.
- Moreover, its inverse is also a symmetry.
- Collecting all these axioms together, we recover a standard mathematical object: the group.

Abstract Groups
- A group is a set $G$  with a binary operation $gh$.
- Associativity: $(gh)t = g(ht)$ for all $g,h,t \in G$
- Identity
- Inverse

Symmetry Groups, Abstract Groups and Group Actions
- Symmetry group: A group of tranforations. The group operations is comparison.
- Abstract group: A set of elements together with composition rule satisfying the group axioms e.g. closure and associativity. This is the "idea" of a group without caring what the elements actually are. 
- Group action: When a group "does something" to another set. It is basically a way to connect a group to a set of points so that the group “moves” the points in a structured way.

Linearity of a Group Action
- a group acting on a vector space by linear transformations.

Group Representation
- A way to make the abstract group concrete, expressing them as matrices that move vectors around.
- Eg the group is a set of rotations, and the representation is the matrices that carry our those rotations on points or vectors.

Group Invariant
- Something that doesnt change when a group acts.
- Eg the group does some "moves", and the group invariants are the properties that stay the same no matter which move you do.

Problems with invariance
- Invariance is suitable when we need a single output over the entire domain. What if we need an output in each domain element?
- If you need to understand structure, relationships, or positions, full invariance destroys useful information.

Group Equivariance
- Invariant → “The output doesn’t change” (e.g., classification label).
- Equivariant → “The output changes in the same way” (e.g., rotated feature maps).

The building blocks of Geometric Deep Learning (GDL)
Let $\Omega$ and $\Omega'$ be domains, G is a symmetry group over $\Omega$. Write $\Omega' \subseteq \Omega$ if $\Omega'$ can be considered a compact version of $\Omega$.
1. Linear G-equivariant layer: It is like a "convolution" that respects the symmetry group G.
2. Nonlinearity: Applying nonlinear fnction like ReLU elementwise to the output of the linear layer. Non-linearity must also preserve equivariance.
3. Local pooling (Coarsening): Reduces resolution or aggregates nearby features.
4. G-Invariant Layer (Global pooling): Where you make the network's final output independent of the symmetry.

| Step                     | What it does                                | Symmetry property   | Analogy              |
| ------------------------ | ------------------------------------------- | ------------------- | -------------------- |
| (1) Linear G-equivariant | Extracts features while preserving symmetry | Equivariant         | Convolution layer    |
| (2) Nonlinearity         | Adds flexibility (nonlinear features)       | Equivariant         | ReLU                 |
| (3) Local pooling        | Coarsens local structure                    | Approx. equivariant | Downsampling         |
| (4) Global pooling       | Aggregates into symmetry-independent output | Invariant           | Classification layer |

Geometric Deep Learning: deep learning built from symmetry-respecting blocks. Each block either preserves (equivariant) or eliminates (invariant) the effects of the symmetry group G.



Reading List:
- [Geometric Foundations of DL](https://medium.com/data-science/geometric-foundations-of-deep-learning-94cdd45b451d)
- [Geometric Deep Learning Grids, Groups, Graphs,Geodesics, and Gauges](https://geometricdeeplearning.com/book/)
- [Hyperbolic Deep Reinforcement Learning](https://medium.com/data-science/hyperbolic-deep-reinforcement-learning-b2de787cf2f7)
