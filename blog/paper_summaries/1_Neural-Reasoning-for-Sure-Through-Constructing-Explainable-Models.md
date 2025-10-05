## 💡 Paper Summary

**Review Date:** 05/10/25  
**Paper Link:** [Neural Reasoning For Sure Through Constructing Explainable Models]("https://ojs.aaai.org/index.php/AAAI/article/view/33262")  
**Paper Authors:** Tiansi Dong, Mateja Jamnik and Pietro Liò, University of Cambridge.

The current flaw with neural network reasoning is that it is seen as a “black box” system, where the process by which outputs are generated from inputs is hidden. As a result, the reasoning reflected in the outputs is often classified as “unsure”, which is undesirable in many situations that require complete certainty when models respond to real-life applications.

This paper explores approaches to make neural network reasoning more reliable by introducing the reasoning-for-sure system. This system focuses on Aristotelian syllogism: a deductive reasoning structure in which a conclusion is derived from two or more propositions that are asserted or assumed to be true, ensuring the reliability of the “for-sure” property persists. Logical statements are encoded geometrically using spheres so that the model can inspect set-theoretic relations between them.

### What different neural and symbolic views in reasoning does reasoning-for-sure systems demonstrate?

- Standard neural network systems provide a non-symbolic view: Input information is represented as continuous vector embeddings rather than discrete symbols. Therefore, reasoning is depicted implicitly by recognising the patterns in continuous data through weighted activations and matrix operations.
- Explainable neural reasoning provides a symbolic or hybrid view: The system explicitly constructs reasoning steps by constructing an intermediate representation that combines logical statements with operators and analysing the set-theoretic relations between them. For example:
    1. All men are mortal.
    2. All Greeks are men.
    3. All Greeks are mortal.

The model would be able to explicitly reach to conclusion C from the premises, A and B. The reasoning system has more meaning internal states to assert a more reliable and logically-consistent thinking process.

### How does the reasoning-for-sure system understand set-theoretic relations between statements?

1. **Input**: symbolical premises expressed as set relations.
2. **Representation**: each predicate/class is converted to a sphere in a hyperbolic vector space.
3. **Set-theoretic Constraints**: Geometric encoding of basic set relations.
    - Containment (All A are B).
    - Disjointness (No A are B).
    - Overlap / existential (Some A are B).
    - Equality / mutual containment (A = B).
4. **Planning the geometric semantic model from the premises**: The constraints show how each sphere representing a premise sit relatively to other spheres in the given hyperbolic space. The idea is to observe geometrically e.g. how much a sphere is contained or disjointed from another. Think of it as planning the model: “I need A inside B, C disjoint from D, E overlapping F, etc.”.
5. **Building the semantic model by explicitly constructing sphere configuration**:
    Figuring out how to adjust the spheres to actually satisfy geometric constraints from 4 and finding specific positions and radii for the spheres that satisfy them.
6. **Inference by inspection of the geometric model**:
    Once a satisfying configuration is produced, verifying whether a candidate conclusion follows can be done by checking the corresponding geometric inequality(s).

### My initial thoughts on what can be done to extend this work?

1. Could this system handle statements that are only partially true? What if we tried a different geometric space could that make reasoning even more accurate?
2. The paper focuses and assumes premises to be strictly true or false, but could it handle scenarios where some statements are uncertain or only partially true? Perhaps it would still be possible to use this logical reasoning framework to propagate assumptions and approximations, while maintaining a structured and reliable inference process. If this is the case, reasoning-for-sure could be extended to handle a wider range of real-world scenarios, including situations with more nuanced or partially true statements.
