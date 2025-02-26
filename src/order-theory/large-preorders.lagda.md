# Large preorders

```agda
module order-theory.large-preorders where
```

<details><summary>Imports</summary>

```agda
open import foundation.dependent-pair-types
open import foundation.identity-types
open import foundation.propositions
open import foundation.universe-levels

open import order-theory.preorders
```

</details>

## Idea

A **large preorder** consists of types indexed by a universe levels, and an
ordering relation comparing objects of arbitrary universe levels. This level of
generality therefore accommodates the inclusion relation on subtypes of
different universe levels. Many preorders in agda-unimath naturally arise as
large preorders.

## Definition

```agda
record
  Large-Preorder (α : Level → Level) (β : Level → Level → Level) : UUω where
  constructor
    make-Large-Preorder
  field
    type-Large-Preorder : (l : Level) → UU (α l)
    leq-Large-Preorder-Prop :
      {l1 l2 : Level} →
      type-Large-Preorder l1 → type-Large-Preorder l2 → Prop (β l1 l2)
    refl-leq-Large-Preorder :
      {l1 : Level} (x : type-Large-Preorder l1) →
      type-Prop (leq-Large-Preorder-Prop x x)
    transitive-leq-Large-Preorder :
      {l1 l2 l3 : Level} (x : type-Large-Preorder l1)
      (y : type-Large-Preorder l2) (z : type-Large-Preorder l3) →
      type-Prop (leq-Large-Preorder-Prop y z) →
      type-Prop (leq-Large-Preorder-Prop x y) →
      type-Prop (leq-Large-Preorder-Prop x z)

open Large-Preorder public

module _
  {α : Level → Level} {β : Level → Level → Level} (X : Large-Preorder α β)
  where

  leq-Large-Preorder :
    {l1 l2 : Level} →
    type-Large-Preorder X l1 → type-Large-Preorder X l2 → UU (β l1 l2)
  leq-Large-Preorder x y = type-Prop (leq-Large-Preorder-Prop X x y)

  is-prop-leq-Large-Preorder :
    {l1 l2 : Level} →
    (x : type-Large-Preorder X l1) (y : type-Large-Preorder X l2) →
    is-prop (leq-Large-Preorder x y)
  is-prop-leq-Large-Preorder x y =
    is-prop-type-Prop (leq-Large-Preorder-Prop X x y)

  leq-eq-Large-Preorder :
    {l1 : Level}
    {x y : type-Large-Preorder X l1} →
    (x ＝ y) → leq-Large-Preorder x y
  leq-eq-Large-Preorder refl = refl-leq-Large-Preorder X _

  preorder-Large-Preorder : (l : Level) → Preorder (α l) (β l l)
  pr1 (preorder-Large-Preorder l) = type-Large-Preorder X l
  pr1 (pr2 (preorder-Large-Preorder l)) = leq-Large-Preorder-Prop X
  pr1 (pr2 (pr2 (preorder-Large-Preorder l))) = refl-leq-Large-Preorder X
  pr2 (pr2 (pr2 (preorder-Large-Preorder l))) = transitive-leq-Large-Preorder X
```
