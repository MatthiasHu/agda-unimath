# The difference between integers

```agda
module elementary-number-theory.difference-integers where
```

<details><summary>Imports</summary>

```agda
open import elementary-number-theory.addition-integers
open import elementary-number-theory.integers

open import foundation.action-on-identifications-binary-functions
open import foundation.action-on-identifications-functions
open import foundation.identity-types
open import foundation.interchange-law
```

</details>

## Idea

Since integers of the form `x - y` occur often, we introduce them here and
derive their basic properties relative to `succ-ℤ`, `neg-ℤ`, and `add-ℤ`. The
file `multiplication-integers` imports `difference-integers` and more properties
are derived there.

## Definition

```agda
diff-ℤ : ℤ → ℤ → ℤ
diff-ℤ x y = x +ℤ (neg-ℤ y)

_-ℤ_ = diff-ℤ
infix 30 _-ℤ_
```

## Properties

```agda
ap-diff-ℤ : {x x' y y' : ℤ} → x ＝ x' → y ＝ y' → x -ℤ y ＝ x' -ℤ y'
ap-diff-ℤ p q = ap-binary diff-ℤ p q

eq-diff-ℤ : {x y : ℤ} → is-zero-ℤ (x -ℤ y) → x ＝ y
eq-diff-ℤ {x} {y} H =
  ( inv (right-unit-law-add-ℤ x)) ∙
  ( ( ap (x +ℤ_) (inv (left-inverse-law-add-ℤ y))) ∙
    ( ( inv (associative-add-ℤ x (neg-ℤ y) y)) ∙
      ( ( ap (_+ℤ y) H) ∙
        ( left-unit-law-add-ℤ y))))

is-zero-diff-ℤ' : (x : ℤ) → is-zero-ℤ (x -ℤ x)
is-zero-diff-ℤ' = right-inverse-law-add-ℤ

is-zero-diff-ℤ :
  {x y : ℤ} → x ＝ y → is-zero-ℤ (x -ℤ y)
is-zero-diff-ℤ {x} {.x} refl = is-zero-diff-ℤ' x

left-zero-law-diff-ℤ : (x : ℤ) → zero-ℤ -ℤ x ＝ neg-ℤ x
left-zero-law-diff-ℤ x = left-unit-law-add-ℤ (neg-ℤ x)

right-zero-law-diff-ℤ : (x : ℤ) → x -ℤ zero-ℤ ＝ x
right-zero-law-diff-ℤ x = right-unit-law-add-ℤ x

left-successor-law-diff-ℤ :
  (x y : ℤ) → (succ-ℤ x) -ℤ y ＝ succ-ℤ (x -ℤ y)
left-successor-law-diff-ℤ x y = left-successor-law-add-ℤ x (neg-ℤ y)

right-successor-law-diff-ℤ :
  (x y : ℤ) → x -ℤ (succ-ℤ y) ＝ pred-ℤ (x -ℤ y)
right-successor-law-diff-ℤ x y =
  ap (x +ℤ_) (neg-succ-ℤ y) ∙ right-predecessor-law-add-ℤ x (neg-ℤ y)

left-predecessor-law-diff-ℤ :
  (x y : ℤ) → (pred-ℤ x) -ℤ y ＝ pred-ℤ (x -ℤ y)
left-predecessor-law-diff-ℤ x y = left-predecessor-law-add-ℤ x (neg-ℤ y)

right-predecessor-law-diff-ℤ :
  (x y : ℤ) → x -ℤ (pred-ℤ y) ＝ succ-ℤ (x -ℤ y)
right-predecessor-law-diff-ℤ x y =
  ap (x +ℤ_) (neg-pred-ℤ y) ∙ right-successor-law-add-ℤ x (neg-ℤ y)

triangle-diff-ℤ :
  (x y z : ℤ) → (x -ℤ y) +ℤ (y -ℤ z) ＝ x -ℤ z
triangle-diff-ℤ x y z =
  ( associative-add-ℤ x (neg-ℤ y) (y -ℤ z)) ∙
  ( ap
    ( x +ℤ_)
    ( ( inv (associative-add-ℤ (neg-ℤ y) y (neg-ℤ z))) ∙
      ( ( ap (_+ℤ (neg-ℤ z)) (left-inverse-law-add-ℤ y)) ∙
        ( left-unit-law-add-ℤ (neg-ℤ z)))))

distributive-neg-diff-ℤ :
  (x y : ℤ) → neg-ℤ (x -ℤ y) ＝ y -ℤ x
distributive-neg-diff-ℤ x y =
  ( distributive-neg-add-ℤ x (neg-ℤ y)) ∙
  ( ( ap ((neg-ℤ x) +ℤ_) (neg-neg-ℤ y)) ∙
    ( commutative-add-ℤ (neg-ℤ x) y))

interchange-law-add-diff-ℤ : interchange-law add-ℤ diff-ℤ
interchange-law-add-diff-ℤ x y u v =
  ( interchange-law-add-add-ℤ x (neg-ℤ y) u (neg-ℤ v)) ∙
  ( ap ((x +ℤ u) +ℤ_) (inv (distributive-neg-add-ℤ y v)))

interchange-law-diff-add-ℤ : interchange-law diff-ℤ add-ℤ
interchange-law-diff-add-ℤ x y u v = inv (interchange-law-add-diff-ℤ x u y v)

left-translation-diff-ℤ :
  (x y z : ℤ) → (z +ℤ x) -ℤ (z +ℤ y) ＝ x -ℤ y
left-translation-diff-ℤ x y z =
  ( interchange-law-diff-add-ℤ z x z y) ∙
  ( ( ap (_+ℤ (x -ℤ y)) (right-inverse-law-add-ℤ z)) ∙
    ( left-unit-law-add-ℤ (x -ℤ y)))

right-translation-diff-ℤ :
  (x y z : ℤ) → (x +ℤ z) -ℤ (y +ℤ z) ＝ x -ℤ y
right-translation-diff-ℤ x y z =
  ( ap-diff-ℤ (commutative-add-ℤ x z) (commutative-add-ℤ y z)) ∙
  ( left-translation-diff-ℤ x y z)
```

```agda
diff-succ-ℤ : (x y : ℤ) → (succ-ℤ x) -ℤ (succ-ℤ y) ＝ x -ℤ y
diff-succ-ℤ x y =
  ( ap ((succ-ℤ x) +ℤ_) (neg-succ-ℤ y)) ∙
  ( ( left-successor-law-add-ℤ x (pred-ℤ (neg-ℤ y))) ∙
    ( ( ap succ-ℤ (right-predecessor-law-add-ℤ x (neg-ℤ y))) ∙
      ( issec-pred-ℤ (x -ℤ y))))
```
