# Similarity of elements in large preorders

```agda
module order-theory.similarity-of-elements-large-preorders where
```

<details><summary>Imports</summary>

```agda
open import foundation.dependent-pair-types
open import foundation.propositions
open import foundation.universe-levels

open import order-theory.large-preorders
```

</details>

## Idea

Two elements `x` and `y` of a [large preorder](order-theory.large-preorders.md)
`P` are said to be **similar** if both `x ≤ y` and `y ≤ x` hold.

## Definition

```agda
module _
  {α : Level → Level} {β : Level → Level → Level} (P : Large-Preorder α β)
  where

  sim-prop-Large-Preorder :
    {l1 l2 : Level}
    (x : type-Large-Preorder P l1) (y : type-Large-Preorder P l2) →
    Prop (β l1 l2 ⊔ β l2 l1)
  sim-prop-Large-Preorder x y =
    prod-Prop
      ( leq-Large-Preorder-Prop P x y)
      ( leq-Large-Preorder-Prop P y x)

  sim-Large-Preorder :
    {l1 l2 : Level}
    (x : type-Large-Preorder P l1) (y : type-Large-Preorder P l2) →
    UU (β l1 l2 ⊔ β l2 l1)
  sim-Large-Preorder x y = type-Prop (sim-prop-Large-Preorder x y)

  is-prop-sim-Large-Preorder :
    {l1 l2 : Level}
    (x : type-Large-Preorder P l1) (y : type-Large-Preorder P l2) →
    is-prop (sim-Large-Preorder x y)
  is-prop-sim-Large-Preorder x y =
    is-prop-type-Prop (sim-prop-Large-Preorder x y)
```

## Properties

### The similarity relation is reflexive

```agda
module _
  {α : Level → Level} {β : Level → Level → Level} (P : Large-Preorder α β)
  where

  refl-sim-Large-Preorder :
    {l1 : Level} (x : type-Large-Preorder P l1) → sim-Large-Preorder P x x
  pr1 (refl-sim-Large-Preorder x) = refl-leq-Large-Preorder P x
  pr2 (refl-sim-Large-Preorder x) = refl-leq-Large-Preorder P x
```

### The similarity relation is transitive

```agda
module _
  {α : Level → Level} {β : Level → Level → Level} (P : Large-Preorder α β)
  where

  transitive-sim-Large-Preorder :
    {l1 l2 l3 : Level}
    {x : type-Large-Preorder P l1}
    {y : type-Large-Preorder P l2}
    {z : type-Large-Preorder P l3} →
    sim-Large-Preorder P y z → sim-Large-Preorder P x y →
    sim-Large-Preorder P x z
  pr1 (transitive-sim-Large-Preorder H K) =
    transitive-leq-Large-Preorder P _ _ _ (pr1 H) (pr1 K)
  pr2 (transitive-sim-Large-Preorder H K) =
    transitive-leq-Large-Preorder P _ _ _ (pr2 K) (pr2 H)
```

### The similarity relation is symmetric

```agda
module _
  {α : Level → Level} {β : Level → Level → Level} (P : Large-Preorder α β)
  where

  symmetric-sim-Large-Preorder :
    {l1 l2 : Level}
    {x : type-Large-Preorder P l1}
    {y : type-Large-Preorder P l2} →
    sim-Large-Preorder P x y → sim-Large-Preorder P y x
  pr1 (symmetric-sim-Large-Preorder H) = pr2 H
  pr2 (symmetric-sim-Large-Preorder H) = pr1 H
```
