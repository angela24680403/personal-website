## Cambridge XAI Lecture Notes

### Lecture 1: Introduction & Global Perturbation Methods
Types of XAI questions:
- What does the prediction mean?
- How did the model make a prediction?
- Which features contributed to a certain prediction and how?
- How can a model learn or select features that are the model interpretable or informative?
- How much does each sample contribute to model training?

What does Explainability do?
- Debug and debias predictions.
- Verify systems.
- Improve models.
- Knowledge discovery.

Explainability gives a foundation for responsible AI
- **Competence:** improving/debugging models.
- **Fairness:** removing unwanted bias.
- **Safety:** making safer decisions.
- **Usability:** actionable decision making.
- **Human-AI collaboration:** better control and user interaction.
- **Accountability** enabling documentation and governance.
- **Privacy:** preserve privacy.

Example Models:
1. Decision trees: Interpretable because prediction can be explained with a rule.
2. Deep neural networks: black-box models. Predictions can be made mathematically but the evaluation is highly non-linear. 

Key Definitions:
- **Interpretability**: the ability to explain or provide the meaning in understandable terms to humans.
- **Explainability**: a notion of explanation as an interface between humans and a decision make that is both an accurate proxy of the decision maker and comprehensibly to humans.
- **Transparency**: a model is transparent if by itself it is understandable.

![Types of Explainable Models](https://github.com/angela24680403/personal-website/blob/main/blog\study_notes\imgs\explainable_ai\types_explainability.png)

A Taxonomy for XAI Methods for Black-box Models
- When is explanation extracted? In-model (inherently interpretable) or post-hoc (black box)?
- Does it explain a particular sample or the whole model? Local, global, or both?
- Does it depend on a particular model? Model-specific or model-agnostic?
- Does it explain the model or an approximation of the model? Visualisation or surrogate?

Explainable modes:
1. **Analytic statement**: natural language descriptions of elements and context that support the decision.
2. **Visualisations**: highlight parts of data that support the decisions and allow user to make their own understanding.
3. **Cases**: give typical/illustrative examples that support the decision.
4. **Rejections or alternate choice**: counterfactual or common misconceptions that argue against the alternative decisions.


#### Knowledge Distillation
Intuition: an interpretable model is trained to approximate the predictions of a black model and then used to explain its predictions.  
![Steps in knowledge distillation.](https://github.com/angela24680403/personal-website/blob/main/blog\study_notes\imgs\explainable_ai\knowledge-distillation.png)


#### Surrogate Alignment
Using surrogate models to achieve alignment. This means creating interpretable models that mimic behaviour of complex systems to ensure the output aligns with human values. 

$  R^2 = 1 - \frac{SSE}{SST} = 1 - \frac{\sum^n_{i=1}(y^*_i - \hat{y}_i)^2}{\sum^n_{i=1} (\hat{y}_i - \bar{\hat{y}})^2} $
- SSE: Sum of squares error
- SST: Sum of squares total
- $y^*_i$: surrogate model predict instance i.
- $\hat{y}_i$: black box model predict instance i.
- $\bar{\hat{y}}_i$: mean of black box model predictions.


### Global Perturbation Methods
This is an XAI technique that helps us understand how a model behaves across the entire input space. In other words, it tries to answer the following: "If I change this feature across many inputs, how does it affect the model's output overall?"

Partial Dependence Plot (PDP):
Measures the marginal effect of a feature on the prediction of the model while holding the other features constant.

PDP-based feature importance:
- Intuition: the more the PDP varies the more important the feature is.
- Formulation: How to measure flatness/variability. 

PDP Shortcomings:
- Interactable for high dimensional data.
- Does not factor in feature interactions.
- It is defined over unique values of features, regardless of their frequency. 



Reading List:

- [Cambridge Explainable Artificial Intelligence Module Material](https://www.cl.cam.ac.uk/teaching/2425/L193/materials.html)
- [Interpretable Machine Learning](https://christophm.github.io/interpretable-ml-book/)
