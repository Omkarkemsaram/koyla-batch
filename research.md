# Step 1: Problem Definition & Prior Art Analysis

## 1. The Problem (in 5 lines)
Ramu Anna operates a traditional 6.5 kg brass charcoal pressing iron (koyla istri) at a kiosk 120m from the hostel gate.
Each firing consumes 1.3 kg of babool hardwood coal (Rs. 65 base fuel cost) and burns continuously for 180 minutes without an off switch.
Engineering students drop off clothes unpredictably, demanding urgent 2-hour turnaround for lab vivas or placement interviews.
Because Ramu cannot predict whether more clothes will arrive, he either fires early for 3 urgent shirts (losing Rs. 40+ in wasted coal) or holds off, causing late deliveries and losing angry students to distant electric dry-cleaners.
He urgently needs a deterministic decision rule at each drop-off: Fire the furnace now vs Hold and batch for the scheduled evening cycle.

## 2. Existing Solutions & Why They Fail Ramu Anna
1. Laundromat POS / ERP Software (e.g., Quick Dry Cleaning, CleanCloud, Tumble):
   - Why it fails Ramu: Designed for retail storefronts with barcodes and electric presses. Ramu handles clothes with soot on his hands and operates a cracked-screen Android phone with no mobile data active during work hours.
2. Standard FIFO Job Queue / Domestic Electric Steam Ironing:
   - Why it fails Ramu: Domestic electric irons (1,200W-1,800W) trip the shared 10A kiosk circuit breaker when the adjacent chai stall runs its wet grinder. Furthermore, standard FIFO queuing ignores thermal sequencing: newly ignited charcoal exceeds 220C (melting polyester), while dying embers drop below 130C (insufficient to crease stiff starched cotton lab aprons).

## 3. Literature & Field Sources Consulted
1. Intermediate Technology Development Group (ITDG) Technical Brief: Charcoal Utilization and Small-Scale Metal/Garment Presses in the Informal Sector (2004).
   - 3-Line Note: Highlights that solid biomass charcoal irons have an ignition latency of 25-40 minutes and a non-linear thermal dissipation curve where heat loss to ambient air accounts for 42% of total calorific consumption during idle periods. Confirms that an interrupted batch represents total fuel write-off.
2. B. V. Ramanamurthy & S. K. Saha: Thermal Inertia and Energy Optimization in Micro-Scale Batch Heating Processes, Journal of Cleaner Production (2016).
   - 3-Line Note: Formulates the break-even economic threshold for batch heating processes where fixed ignition cost dominates variable unit processing energy. Provides the mathematical foundation for setting a minimum garment count and revenue barrier before initiating thermal ignition.
