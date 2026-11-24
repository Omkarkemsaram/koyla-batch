# koyla-batch - Operational Charcoal Firing Optimizer

> Candidate: Ojeshwini K.  
> Target User: Mr. Ramachandrappa M. ("Ramu Anna"), Om Sai Ram Pressing Kiosk, Mathikere, Bengaluru  
> Date: November 24, 2026  
> Video Demo: https://youtu.be/koyla-batch-demo  

## 1. What This Tool Does
Simulates the burn break-even economics and thermodynamic decay of a 6.5 kg solid-brass charcoal iron (1.3 kg Babool coal, Rs. 65 cost, 180 min burn).
- Recommends: FIRE THE COAL FURNACE NOW vs HOLD COAL.
- Thermally sorts clothes: Heavy starched cotton lab aprons first (220C) -> Synthetics last (130C).

## 2. Quickstart
Command to run:
py koyla_batch.py data.csv
py koyla_batch.py data.csv --current-time 13:50
py koyla_batch.py data.csv --test-bad-row

## 3. What It Gets Wrong
1. Cross-Breeze Variations: Street winds act as a forced draft, burning coal in 140 min instead of 180.
2. Charcoal Moisture: Damp monsoon coal takes longer to ignite and smokes.
3. Fabric Mislabeling: Tactile fingertip testing must override the script if a student mislabels polyester as cotton.
