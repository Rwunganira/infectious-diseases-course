# Infectious Diseases: A Concise Course for Public Health Practice

A short, practical course on what a public health professional needs to know about infectious diseases: how they work, how they spread, how we measure them, and how we stop them. Eight modules, about 2–3 hours each, with an exercise at the end of every module.

**Audience:** epidemiologists, FETP trainees, surveillance officers, programme managers.
**Prerequisites:** basic epidemiology (rates, proportions) and some comfort with Python or R for the exercises.

---

## Course map

| # | Module | Core question |
|---|--------|---------------|
| 1 | [Foundations: agents, hosts, environment](#module-1--foundations-agents-hosts-environment) | What causes infection, and why do only some people get sick? |
| 2 | [Transmission](#module-2--transmission) | How does a pathogen get from one host to the next? |
| 3 | [Natural history and key time periods](#module-3--natural-history-and-key-time-periods) | When is someone infectious, and when do they show symptoms? |
| 4 | [Measuring spread](#module-4--measuring-spread) | How fast is it spreading, and how big will it get? |
| 5 | [Surveillance and diagnostics](#module-5--surveillance-and-diagnostics) | How do we know what is happening? |
| 6 | [Outbreak investigation](#module-6--outbreak-investigation) | What do we do when cases appear? |
| 7 | [Prevention and control](#module-7--prevention-and-control) | Which levers break transmission? |
| 8 | [Priority diseases and One Health](#module-8--priority-diseases-and-one-health) | Which diseases matter most, and where do new ones come from? |

---

## Module 1 — Foundations: agents, hosts, environment

**You will learn to:** name the main pathogen types and explain infection outcomes using the epidemiological triad.

**Key concepts**
- **Pathogen types:** viruses (measles, influenza, HIV, Ebola), bacteria (TB, cholera, *Salmonella*), parasites — protozoa (malaria) and helminths (schistosomiasis), fungi (*Candida auris*), prions.
- **Epidemiological triad:** *agent* (infectivity, virulence, drug resistance), *host* (age, immunity, nutrition, comorbidity, vaccination), *environment* (water, sanitation, crowding, climate, vectors).
- **Infection vs. disease:** colonisation → infection → disease. Many infections are asymptomatic (most polio, much TB infection).
- **Infectivity / pathogenicity / virulence:** ability to infect; ability to cause disease once infected; severity of that disease (e.g. case fatality ratio).
- **Immunity:** innate vs. adaptive; natural vs. vaccine-derived; waning immunity.
- **Antimicrobial resistance (AMR):** selection pressure from misuse of antibiotics; a cross-cutting threat to every module that follows.

**Exercise:** For cholera, measles and malaria, fill in one triad each (agent / host / environment factors). Which factor is most modifiable by public health action?

---

## Module 2 — Transmission

**You will learn to:** classify transmission routes and link each to the control measure that interrupts it.

**Chain of infection:** agent → reservoir → portal of exit → mode of transmission → portal of entry → susceptible host. Break any link and transmission stops.

| Route | Examples | Typical control |
|-------|----------|-----------------|
| Contact (direct/indirect) | Ebola, scabies, MRSA | Hand hygiene, PPE, isolation |
| Droplet | Influenza, pertussis, meningococcus | Masks, distancing |
| Airborne | Measles, TB, varicella | Ventilation, N95, airborne isolation |
| Faecal–oral (water/food) | Cholera, typhoid, hepatitis A, rotavirus | WASH, food safety, vaccination |
| Vector-borne | Malaria, dengue, Rift Valley fever | Bednets, IRS, larval control |
| Blood / sexual | HIV, hepatitis B/C, syphilis | Screening, condoms, safe injection, PrEP |
| Vertical (mother-to-child) | HIV, syphilis, hepatitis B | Antenatal testing, treatment, birth-dose vaccine |
| Zoonotic spillover | Rabies, Marburg, anthrax, mpox | One Health surveillance, animal vaccination |

**Reservoirs:** humans (measles), animals (rabies in dogs, Marburg in fruit bats), environment (cholera in water, anthrax spores in soil). A disease can be eradicated only if its reservoir is human-only and a good tool exists (smallpox; polio and Guinea worm are close).

**Exercise:** Pick one disease from the table and draw its chain of infection. Mark which link your country's programme targets today.

---

## Module 3 — Natural history and key time periods

**You will learn to:** define the time periods that drive surveillance and control decisions.

```
Exposure ──► Infection ──────────────────────────────────────► Recovery / death
              │◄──── latent period ────►│◄─── infectious period ───►│
              │◄──────── incubation period ───────►│ symptoms ...
```

- **Incubation period:** infection → symptom onset. Sets quarantine length and the "two maximum incubation periods" rule for declaring an outbreak over (e.g. 42 days for Ebola and Marburg).
- **Latent period:** infection → becoming infectious.
- **Pre-symptomatic transmission:** happens when the latent period is shorter than the incubation period (COVID-19, influenza). It makes symptom-based control much harder. SARS-1 and Ebola transmit mainly after symptoms, which is why isolation worked well for them.
- **Serial interval:** symptom onset in a case → onset in the person they infected. **Generation time:** the same, measured infection-to-infection. Needed to estimate R.
- **Outcomes:** recovery with immunity, chronic infection/carriage (hepatitis B, typhoid carriers), latency and reactivation (TB, herpes zoster), death.

**Exercise:** Look up incubation periods for cholera, measles, Ebola and rabies. For each, state what quarantine or monitoring period you would recommend for contacts and why.

---

## Module 4 — Measuring spread

**You will learn to:** calculate and interpret the core outbreak measures and read a simple SIR model.

**Frequency and severity**
- **Incidence** (new cases / population at risk / time) vs. **prevalence** (existing cases at a point).
- **Attack rate** = cases ÷ population at risk during an outbreak. **Secondary attack rate** = cases among contacts ÷ contacts.
- **Case fatality ratio (CFR)** = deaths ÷ confirmed cases. It is biased early in an outbreak (deaths lag; mild cases are missed).

**Transmissibility**
- **R₀ (basic reproduction number):** average secondary cases from one case in a fully susceptible population. Approximate values: measles 12–18, pertussis 5–17, smallpox 5–7, COVID-19 (ancestral) 2–3, seasonal flu ~1.3.
- **Rₜ (effective reproduction number):** the same, at time *t*, given immunity and control. Rₜ > 1 means growth, < 1 means decline.
- **Herd immunity threshold:** 1 − 1/R₀. For measles that is ~92–95%, which is why measles needs two doses at very high coverage.
- **Doubling time** and **growth rate** come straight from the epidemic curve.
- **Overdispersion:** a minority of cases cause most transmission (superspreading). It is why cluster-focused response works.

**Models**
- **SIR model:** Susceptible → Infected → Recovered, with transmission rate β and recovery rate γ; R₀ = β/γ. Add an *E* (exposed) compartment for SEIR.
- Models are for exploring scenarios ("what if vaccination reached 80%?"), not for precise prediction.

**Exercise:** Run [`exercises/sir_model.py`](exercises/sir_model.py). Change R₀ and the vaccination coverage, and find the coverage at which the epidemic no longer takes off. Compare it with 1 − 1/R₀.

---

## Module 5 — Surveillance and diagnostics

**You will learn to:** describe how surveillance systems detect infectious disease and judge test results in context.

**Surveillance**
- **Purpose:** detect outbreaks early, monitor trends, guide and evaluate programmes.
- **Types:** passive (routine facility reports), active (staff seek cases), sentinel (selected sites, e.g. influenza ILI/SARI), syndromic, event-based (media, community rumours), laboratory-based, genomic, wastewater/environmental.
- **Frameworks:** WHO **IDSR** (Integrated Disease Surveillance and Response) in African countries; **IHR (2005)**, which requires notification of events that may be a public health emergency of international concern; **DHIS2** as the common reporting platform.
- **Case definitions:** suspected → probable → confirmed. Wide definitions catch more cases (sensitive); narrow ones are more accurate (specific).
- **Thresholds:** alert vs. epidemic thresholds. Some diseases trigger action on a single case (cholera, measles, polio/AFP, VHF, anthrax).
- **Evaluating a system (CDC guidelines):** simplicity, flexibility, data quality, acceptability, sensitivity, PPV, representativeness, timeliness, stability.

**Diagnostics**
- Microscopy, culture, rapid diagnostic tests (RDTs), PCR, serology (IgM = recent, IgG = past/immunity), sequencing.
- **Sensitivity / specificity** are properties of the test. **PPV / NPV** depend on prevalence: the same RDT gives many false positives when prevalence is low.
- **Specimens:** right sample, right time, cold chain, triple packaging, chain of custody.

**Exercise:** A malaria RDT has sensitivity 95% and specificity 95%. Calculate the PPV at 30% prevalence and at 1% prevalence. What does this mean for testing in a low-transmission district?

---

## Module 6 — Outbreak investigation

**You will learn to:** carry out the standard steps of a field outbreak investigation.

**The steps** (they overlap in practice; control measures start as early as possible):
1. Prepare for fieldwork (team, logistics, lab, coordination).
2. Confirm the outbreak exists (compare with baseline; rule out artefacts).
3. Verify the diagnosis (clinical review, lab).
4. Build a working case definition (person, place, time + clinical/lab criteria).
5. Find cases systematically and build a **line list**.
6. Do descriptive epidemiology: **epi curve** (point source vs. continuous vs. propagated), map, person characteristics.
7. Develop hypotheses.
8. Test them analytically: **cohort** (risk ratio) or **case-control** (odds ratio).
9. Refine hypotheses; do environmental and lab studies.
10. Implement control and prevention measures.
11. Keep up surveillance to confirm the measures work.
12. Communicate findings: situation reports, briefings, the final report.

**Supporting skills:** contact tracing and follow-up, risk communication and community engagement (RCCE), Incident Management System (IMS) and Public Health Emergency Operations Centres (PHEOC), after-action reviews.

**Exercise:** Sketch the epi curve you would expect from (a) a contaminated wedding meal and (b) a measles outbreak in a school. Explain the difference in shape.

---

## Module 7 — Prevention and control

**You will learn to:** choose interventions matched to the transmission route and setting.

- **Vaccination:** routine immunisation (EPI), campaigns (SIAs), outbreak response and ring vaccination (Ebola rVSV-ZEBOV), cold chain, coverage vs. effectiveness.
- **Case management:** early diagnosis and treatment shortens the infectious period (TB DOTS, malaria ACTs, cholera ORS and IV fluids).
- **Isolation** (sick people) and **quarantine** (exposed people who are well).
- **Infection prevention and control (IPC):** standard precautions, transmission-based precautions, screening/triage, health worker protection.
- **WASH:** safe water, sanitation, hygiene. The backbone of controlling diarrhoeal disease.
- **Vector control:** insecticide-treated nets, indoor residual spraying, larval source management.
- **Chemoprophylaxis and mass drug administration:** PrEP/PEP, seasonal malaria chemoprevention, deworming, NTD MDA.
- **Antimicrobial stewardship** to slow AMR.
- **Non-pharmaceutical interventions:** masks, distancing, gathering limits, travel measures. Weigh them against social and economic costs.
- **Behaviour change and community engagement:** interventions work only if people accept and use them.

**Exercise:** For a cholera outbreak in a peri-urban area, list five interventions, rank them by expected impact, and say how you would measure each one.

---

## Module 8 — Priority diseases and One Health

**You will learn to:** recognise the key infectious disease priorities and explain the One Health approach to emerging threats.

**Major endemic burdens:** HIV, tuberculosis, malaria, pneumonia, diarrhoeal disease, viral hepatitis, neglected tropical diseases.

**Epidemic-prone diseases to know (IDSR immediately notifiable examples):** cholera, measles, meningitis, yellow fever, viral haemorrhagic fevers (Ebola, Marburg, Lassa, CCHF), mpox, novel influenza, polio (AFP), anthrax, plague, rabies, COVID-19.

**One Health**
- Around 60% of known human pathogens, and about 75% of emerging ones, are zoonotic.
- Drivers: land-use change, wildlife contact, intensive livestock farming, climate change, travel and trade.
- Joint human–animal–environment work: shared surveillance, joint outbreak investigation (e.g. rabies, anthrax, Rift Valley fever, avian influenza), AMR across sectors.

**Global health security**
- IHR (2005), the Joint External Evaluation (JEE), National Action Plans for Health Security (NAPHS), the **7-1-7 target** (detect within 7 days, notify within 1, respond within 7), the Pandemic Fund, and the WHO Pandemic Agreement (adopted 2025).
- **Regional context:** Rwanda's Marburg response (2024) shows the whole cycle. Rapid detection, contact tracing, IPC, trial vaccine use and the 42-day countdown to declaring the outbreak over.

**Exercise:** Choose one priority zoonosis in your country. Map which sectors (human, animal, environment) hold relevant data today and propose one joint surveillance action.

---

## Capstone (optional)

Use a public line list or a simulated dataset (for example from the [`outbreaks` R package](https://www.reconverse.org/outbreaks/) or your own `python-epidemics` work) to:
1. build an epi curve and describe person/place/time,
2. estimate the growth rate or Rₜ,
3. write a one-page situation report with three recommended control measures.

---

## Key references

- Heymann DL (ed.). *Control of Communicable Diseases Manual*, 21st ed. APHA.
- Giesecke J. *Modern Infectious Disease Epidemiology*, 3rd ed. CRC Press.
- CDC. *Principles of Epidemiology in Public Health Practice* (free online, Lessons 1, 5 and 6).
- WHO AFRO. *Technical Guidelines for Integrated Disease Surveillance and Response*, 3rd ed.
- WHO. *International Health Regulations (2005)*, 3rd ed.
- Vynnycky E, White R. *An Introduction to Infectious Disease Modelling*. OUP.
- The Applied Epi *Epidemiologist R Handbook* — <https://epirhandbook.com>.

---

*Repository:* `infectious-diseases-course` · *Author:* Samuel Rwunganira
