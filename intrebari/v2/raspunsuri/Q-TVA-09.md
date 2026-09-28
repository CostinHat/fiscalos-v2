# Q-TVA-09 — CALCUL

**Întrebarea:** Un restaurant emite în 2026 o notă cu mâncare 800 lei bază și vin 200 lei bază. Cât TVA colectează în total?

## Stratul semantic (motorul nou) — NU POT RĂSPUNDE

*La data de referință 28.09.2026, presupun un restaurant persoană impozabilă înregistrată în scopuri de TVA în România, care prestează servicii de restaurant consumate la locație (mâncare 800 lei bază) și servește vin (200 lei bază), fără alte elemente accesorii.*

Motiv: modelul s-a abţinut: Atomii primiți arată doar că băuturilor alcoolice servite în restaurant se aplică cota standard, iar mâncării o cotă redusă, dar nu conțin nivelul cotei standard și al cotei reduse aplicabile în anul 2026 (singura cifră de cotă redusă din atomi este 9%, într-un exemplu din norme, iar cotele standard apar doar în exemple istorice de 20% și 24%). În plus, determinarea TVA-ului total ar presupune un calcul (aplicarea cotelor pe cele două baze și însumarea), rezultat care nu apare literal în niciun atom.

- **Normele metodologice ale Codului fiscal (HG 1/2016) art. V alin. (8)** — `hg_1_2016_norme_cod_fiscal#artV~19/alin8~19` · valabil din nedovedit
  > Pentru băuturile alcoolice servite la restaurant sau oferite în cazul serviciilor de catering se aplică cota standard de TVA, dar nu se consideră că are loc o livrare separată de bunuri, oferirea de băuturi alcoolice făcând parte din serviciile de restaurant sau de catering.

Apel: `claude-opus-5`, {'intrare': 5480, 'iesire': 829, 'cache_scriere': 0, 'cache_citire': 1531} tokeni, $0.0489, 14.8 s

Pe fond: **NU POT** — modelul s-a abţinut: Atomii primiți arată doar că băuturilor alcoolice servite în restaurant se aplică cota standard, iar mâncării o cotă redusă, dar nu conțin nivelul cotei standard și al cotei redus

## Motorul lexical — NU POT RĂSPUNDE

*Data de referinta: 2026-09-28 (an, din "2026"). Perimetru presupus: persoana juridica romana in regim general, fara situatii speciale nementionate in intrebare - implicit, motorul lexical nu citeste perimetrul din intrebare.*

Motiv: R-CALC: intrebarea are 2 baze monetare; calculul cere compunerea mai multor reguli, pe care motorul nu o face


Pe fond: **NU POT** — R-CALC: intrebarea are 2 baze monetare; calculul cere compunerea mai multor reguli, pe care motorul nu o face

## Cheia

- răspuns așteptat: 130 lei (800 × 11% = 88 lei; 200 × 21% = 42 lei — băuturile alcoolice sunt excluse de la cota redusă)
- temei așteptat: Cod fiscal art. 291 alin. (2) lit. n) și alin. (1), forma modificată de Legea 141/2025 art. II pct. 42

