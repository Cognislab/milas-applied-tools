# Human-L3-in-control: A Checklist for Preventing Policy-Layer Delegation in Human-AI Interaction

Version: v0.1  
Status: Draft / Spec Note  
Author: Mameta Edanari / Cognis-Lab  

## 1. Problem

Human-in-the-loop does not necessarily mean human control.

In human-AI interaction, a human may remain formally present in the loop while gradually delegating goal-setting, prioritization, refusal, and stopping authority to the AI system.

This note proposes “Human-L3-in-control” as a lightweight checklist for detecting and preventing this form of policy-layer delegation.

## 2. Definition

In MiLAS, L3 refers to the policy layer: the layer responsible for goals, priorities, refusal, and stopping authority.

Human-L3-in-control means that the human retains:

- the goal of the task
- the priority order
- the right to reject AI proposals
- the authority to stop or defer the task
- the final commitment to action

## 3. Failure Modes

### 3.1 Rubber-stamping

The human approves AI outputs without meaningful evaluation.

### 3.2 Goal drift

The AI gradually shifts the task goal, and the human follows the shifted goal without noticing.

### 3.3 Refusal loss

The human feels unable to reject an AI proposal once it appears coherent or confident.

### 3.4 Stop-condition erosion

The original stopping condition disappears, and the interaction continues without a clear endpoint.

## 4. Checklist

Before or during AI use, ask:

1. Can I state the goal without AI assistance?
2. Can I reject the AI’s proposal?
3. Did I define stopping conditions before continuing?
4. Has the AI shifted the task goal?
5. Am I choosing, or merely approving?

If two or more answers indicate loss of human control, pause the interaction and restate the goal, priority, and stopping condition.

## 5. Relation to Existing Concepts

Human-L3-in-control is related to, but distinct from:

- Human-in-the-loop
- Meaningful Human Control
- Automation Bias
- Overreliance
- AI Governance

Human-in-the-loop focuses on whether a human is present in the process.  
Human-L3-in-control focuses on whether the human still retains policy-layer authority.

## 6. Limitations

This note uses MiLAS as a descriptive design lens, not as a validated cognitive theory.

The checklist is not a clinical tool, a safety certification method, or a substitute for formal AI governance frameworks.

It is a lightweight practical aid for identifying possible delegation of human goals, priorities, refusal, and stopping authority during human-AI interaction.

## 7. Suggested Use

Use this checklist when:

- asking AI to evaluate your work
- deciding whether to publish, submit, or revise something
- using AI for planning or prioritization
- comparing multiple AI responses
- noticing that the interaction continues without a clear stopping point
