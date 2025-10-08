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

![Types of Explainable Models](https://github.com/angela24680403/personal-website/blob/main/blog/study_notes/imgs/explainable_ai/types_explainability.png?raw=true)

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
![Steps in knowledge distillation.](https://github.com/angela24680403/personal-website/blob/main/blog/study_notes/imgs/explainable_ai/knowledge-distillation.png?raw=true)

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

### Lecture 2: Local Perturbation Methods

What does it mean to be local?
- Key assumption in local explainability: Even though globally the model may be complex, it may be less complex locally.
- Locality refers to the vacinity of a particular sample for which we seek an explanation.
- Local explanations vary for each sample despite being based on the same complex model.

Explaining a sample one feature at a time:
- Common for humans to explain things based on features.
- Feature attribution/importance: we want a sense of which features were most relevant for the prediction of the model.

Shapley Scores
- A score that fairly assigns credit across all players/features by averaging marginal contribution of a feature across all possible coalitions.
- All this equation says is that we compute a feature's importance by marginalising over its contributions across all possible subsets of features.
- However it is too expensive to look at every subset of features.

SHAP
- Shapley Additive exPlanation (SHAP) efficiently estimates Shapley scores by looking at how a model's output deviates from its mean one feature at a time.
- It is used to explain how much each feature contributes to a particular prediction.
- For each feature, SHAP asks: If I add this feature to the model (in every possible order), how much does it change the prediction on average?
- E.g.: Model prediction = 0.5 (base) + 0.2 (age helped) - 0.1 (income lowered) + 0.3 (education helped)
- Drawback: SHAP can be computationally expensive due to local model creation.

$\phi_i = \sum_{S \subseteq F \setminus \{i\}} \frac{|S|! \, (|F| - |S| - 1)!}{|F|!} \Big[ f_{S \cup \{i\}}(x_{S \cup \{i\}}) - f_S(x_S) \Big] $

Saliency Maps: Vanilla Gradient
- partial derivatives represent sensitivity of otput to input change.
- Vanilla gradient: For an input x and label y, we calculate the gradient for the prediction wrt input features.
- Problem with this: ReLU saturation problem. Inputs that contributed to the output negatively may be disregarded and their attribution may be concealed. 

Saliency Maps: SmoothGrad
- Remove noise by adding noise!
- For an image of interest, we create multiple versions by adding nosie.
- For each version, we get the saliency map.
- We average over all of them.
Reading List:

- [Cambridge Explainable Artificial Intelligence Module Material](https://www.cl.cam.ac.uk/teaching/2425/L193/materials.html)
- [Interpretable Machine Learning](https://christophm.github.io/interpretable-ml-book/)
