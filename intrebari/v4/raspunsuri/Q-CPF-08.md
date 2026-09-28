# Q-CPF-08 — CAPCANA

**Întrebarea:** ANAF constată în 2026 că o SRL a depus cu întârziere D100 în martie 2024 și vrea să aplice amendă. Nu s-a prescris aplicarea amenzii, având în vedere termenul de 6 luni din OG 2/2001?

## Stratul de navigare (v4) — NU POT RĂSPUNDE

*La data de referință (martie 2024), presupun o SRL, contribuabil/plătitor administrat de organul fiscal central, care a depus cu întârziere declarația fiscală D100 (obligație de declarare la termen), faptă contravențională din Titlul XI al Codului de procedură fiscală, constatată de ANAF în 2026; presupun că nu există împrejurări care să transforme fapta în infracțiune.*

Motiv: VERIFICAREA MECANICA a respins propunerea modelului: valoarea legala '2024' nu apare in niciun citat (C13: o valoare legala se dovedeste din atom, chiar daca e si in intrebare)

- **Codul de procedură fiscală (Legea 207/2015) art. 339 alin. (1)** — `legea_207_2015_consolidat#art339/alin1` · valabil din nedovedit
  > Prin derogare de la prevederile art. 13 alin. (1) din Ordonanța Guvernului nr. 2/2001 privind regimul juridic al contravențiilor, aprobată cu modificări și completări prin Legea nr. 180/2002 , cu modificările și completările ulterioare, aplicarea sancțiunii amenzii pentru contravențiile prevăzute în prezentul titlu se prescrie în termen de 5 ani de la data săvârșirii faptei.
- **Codul de procedură fiscală (Legea 207/2015) art. 336 alin. (1) lit. b)** — `legea_207_2015_consolidat#art336/alin1/litb` · valabil din nedovedit
  > neîndeplinirea de către contribuabil/plătitor la termen a obligațiilor de declarare prevăzute de lege, a bunurilor și veniturilor impozabile sau, după caz, a impozitelor, taxelor, contribuțiilor și a altor sume
- **Codul de procedură fiscală (Legea 207/2015) art. 336 alin. (1)** — `legea_207_2015_consolidat#art336/alin1` · valabil din nedovedit
  > Constituie contravenții următoarele fapte, dacă nu au fost săvârșite în astfel de condiții încât să fie considerate, potrivit legii, infracțiuni:
- derogare tratată: `legea_207_2015_consolidat#art339/alin1` — Atomul citat este chiar norma derogatorie: înlătură, pentru contravențiile din Titlul XI al Codului de procedură fiscală, termenul de prescripție din art. 13 alin. (1) din OG 2/2001 invocat în întrebare și îl înlocuiește cu 5 ani de la data săvârșirii faptei.

### Navigarea (12 pași, 8 ture)

1. `cauta` {"interogare": "prescripția aplicării sancțiunii contravenționale 6 luni de la data săvârșirii faptei"}
2. `cauta` {"interogare": "contravenții Codul de procedură fiscală prescripție depunere cu întârziere declarație"}
3. `deschide` {"id": "legea_207_2015_consolidat#art339/alin1"}
4. `deschide` {"id": "og_2_2001#art13/alin1"}
5. `cuprins` {"act": "legea_207_2015_consolidat", "filtru": "contravenții"}
6. `cauta` {"interogare": "Aplicarea sancțiunii amenzii contravenționale se prescrie în termen de 6 luni de la data săvârșirii faptei"}
7. `deschide` {"id": "legea_207_2015_consolidat#art336"}
8. `deschide` {"id": "legea_207_2015_consolidat#art336/alin1"}
9. `cuprins` {"act": "og_2_2001", "filtru": "prescripție"}
10. `deschide` {"id": "legea_207_2015_consolidat#art336/alin1/lita"}
11. `cauta` {"interogare": "OG 2/2001 aplicarea sancțiunii amenzii se prescrie 6 luni data săvârșirii faptei contravenții"}
12. `deschide` {"id": "legea_207_2015_consolidat#art336/alin1/litb"}

Apel: `claude-opus-5`, {'intrare': 16, 'iesire': 3281, 'cache_scriere': 11391, 'cache_citire': 87727} tokeni, $0.1972, 57 s

Pe fond: **NU POT** — VERIFICAREA MECANICA a respins propunerea modelului: valoarea legala '2024' nu apare in niciun citat (C13: o valoare legala se dovedeste din atom, chiar daca e si in intrebare)

## Stratul semantic v3 (context dat de căutare) — NU POT, pe fond NU POT

> modelul s-a abţinut: Atomii primiți conțin exclusiv dispoziții din Codul de procedură fiscală (eșalonări la plată, certificarea declarațiilor, schimb de informații) și din Codul fiscal, niciunul nu redă termenul de prescripție a aplicării sancțiunii contravenționale din OG 2/2001 și nici regimul contravențional al nedepunerii în termen a declarațiilor fiscale. În plus, verificarea prescripției ar presupune și un calcul al intervalului dintre martie 2024 și 2026, care nu apare literal în niciun a…

## Cheia

- Nu s-a prescris: pentru contravențiile din Codul de procedură fiscală, aplicarea amenzii se prescrie în 5 ani de la săvârșirea faptei (derogare de la termenul de 6 luni din OG 2/2001 art. 13 alin. (1)).
- temei: Legea 207/2015 art. 339 alin. (1); OG 2/2001 art. 13 alin. (1)
