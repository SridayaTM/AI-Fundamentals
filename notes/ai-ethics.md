# AI Ethics

This part made me step back from the technical side of AI and think about its impact.

Until this point, most of the focus was on how to build models and improve accuracy. But this section made it clear that even a well-performing system can be problematic if it is not designed and used responsibly.

---

## Core Principles

From what I understood, ethical AI is built around a few key ideas:

- fairness  
- transparency  
- accountability  
- privacy  
- robustness  

These are not strict rules, but they guide how systems should be developed and evaluated.

---

## Fairness

Fairness in AI means that a system should not consistently disadvantage certain groups of people.

In practice, this is difficult to achieve because models learn from existing data, and that data may already reflect real-world inequalities.

So fairness is not just a model issue — it starts from the data itself.

---

## Protected Attributes and Groups

Certain attributes like gender, race, or age should not influence outcomes in an unfair way.

This leads to the idea of:
- **privileged groups** → groups that tend to receive better outcomes  
- **unprivileged groups** → groups that may be disadvantaged  

Recognizing this difference is important when evaluating model behavior.

---

## Bias in AI

Bias does not usually come from the algorithm alone.

It can enter through:
- the data collected  
- how the problem is framed  
- decisions made during model design  

What stood out to me is that removing bias is not straightforward — it requires awareness at every stage.

---

## Robustness

A model should perform reliably even when inputs are slightly different from what it was trained on.

Real-world data is often messy, so systems need to handle variation without failing.

---

## Adversarial Robustness

This goes a step further — considering inputs that are intentionally designed to mislead the model.

Even small, almost invisible changes can sometimes lead to incorrect predictions.

This shows that model accuracy alone does not guarantee reliability.

---

## Adversarial Attacks

An adversary can influence a system by:
- modifying input data  
- exploiting weaknesses in the model  

This is especially concerning in sensitive applications.

---

## Explainability and Interpretability

As models become more complex, understanding their decisions becomes harder.

- **Interpretability** refers to how directly we can understand a model  
- **Explainability** refers to how we can justify or describe its decisions  

This becomes important when decisions affect people.

---

## Transparency

Transparency is about being clear on:
- how the system works  
- what data is used  
- what limitations exist  

Without this, it becomes difficult to trust or question the system.

---

## Governance

Governance involves setting processes around how AI systems are developed and used.

This includes:
- monitoring performance  
- auditing decisions  
- defining accountability  

It ensures that responsibility is not ignored after deployment.

---

## Roles and Responsibility

Different roles contribute to ethical AI:

- Developers and data scientists → design and train models  
- Organizations → decide how systems are applied  

Responsibility is shared, not limited to one role.

---

## Data and Privacy

AI systems often depend on large amounts of data.

- **Personal data** identifies an individual  
- **Sensitive data** (health, financial, etc.) requires stronger protection  

Handling this data carefully is essential.

---

## Anonymization and Privacy Techniques

- **Anonymization** removes identifying details from data  
- **Differential privacy** adds controlled noise to protect individuals  

These methods aim to balance usefulness and privacy.

---

## Data Minimization

Only collecting and using the data that is necessary.

This reduces risk and limits unnecessary exposure of personal information.

---

## My Take

This section changed how I look at AI systems.

It’s easy to focus on performance metrics, but that is only one part of the picture.

Decisions made during data collection, model design, and deployment all have consequences.

What stood out to me is that responsibility in AI is not something added at the end — it needs to be considered throughout the entire process.
