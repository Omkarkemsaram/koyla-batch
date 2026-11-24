import sys, os, csv, argparse
from datetime import datetime, timedelta

CHARCOAL_COST_PER_KG_DEFAULT = 50.0
CHARCOAL_KG_PER_FIRING = 1.3
IGNITION_OVERHEAD_MIN = 30.0
USEFUL_BURN_DURATION_MIN = 180.0
BREAKEVEN_MARGIN_THRESHOLD_DEFAULT = 110.0

THERMAL_HIERARCHY = {
    "Heavy_Drill_Cotton": 1, "Cotton_Canvas": 1, "Cotton": 2,
    "Linen_Cotton": 2, "Denim_Cotton": 2, "Woolen_Blend": 3,
    "Poly_Viscose": 3, "Silk_Blend": 4, "Poly_Cotton": 4, "Synthetic_Blend": 5,
}

FABRIC_TEMP_LABELS = {
    1: "WHITE-HOT (200C - 220C): Heavy Starched / Drill Cotton",
    2: "HIGH HEAT (180C - 200C): Pure Cottons / Linens / Denim",
    3: "MEDIUM-HIGH (160C - 180C): Blended Woolens / Suiting",
    4: "MEDIUM HEAT (140C - 160C): Silk Blends / Poly-Cottons",
    5: "MILD RESIDUAL (120C - 140C): Delicate Synthetics / Polyesters",
}

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("csv_path", nargs="?", default="data.csv")
    parser.add_argument("--current-time", default="14:45")
    parser.add_argument("--test-bad-row", action="store_true")
    args = parser.parse_args()

    if not os.path.exists(args.csv_path):
        print(f"Error: {args.csv_path} not found.")
        return

    records = []
    # utf-8-sig handles Windows PowerShell BOM automatically
    with open(args.csv_path, mode="r", encoding="utf-8-sig") as f:
        reader = list(csv.DictReader(f))
        if args.test_bad_row:
            reader.append({"arrival_time": "99:99", "quantity": "-1", "unit_press_time_min": "0", "unit_price_inr": "-5"})
        for line, raw_row in enumerate(reader, start=2):
            try:
                row = {k.strip().lstrip('\ufeff'): v.strip() for k, v in raw_row.items() if k}
                dt = datetime.strptime(row["arrival_time"], "%H:%M")
                qty = int(row["quantity"])
                p_time = float(row["unit_press_time_min"])
                price = float(row["unit_price_inr"])
                if qty <= 0 or p_time <= 0 or price < 0: raise ValueError()
                records.append({
                    "dt": dt, "token": row.get("token_no", "?"), "garment": row.get("garment_type", "?"),
                    "fabric": row.get("fabric_category", "Cotton"), "qty": qty,
                    "time": qty * p_time, "rev": qty * price, "pickup": row.get("promised_pickup", "?"),
                    "urgency": row.get("urgency", "Normal"),
                    "thermal": THERMAL_HIERARCHY.get(row.get("fabric_category", ""), 3)
                })
            except Exception as e:
                sys.stderr.write(f"[WARN] Skipped invalid row at line {line}: {e}\n")

    eval_dt = datetime.strptime(args.current_time, "%H:%M")
    queue = [r for r in records if r["dt"] <= eval_dt]
    total_qty = sum(r["qty"] for r in queue)
    total_rev = sum(r["rev"] for r in queue)
    fuel_cost = CHARCOAL_KG_PER_FIRING * CHARCOAL_COST_PER_KG_DEFAULT
    net_margin = total_rev - fuel_cost
    urgent_items = [r for r in queue if "urgent" in r["urgency"].lower()]

    print("\n" + "=" * 74)
    print(" KOYLA-BATCH: CAMPUS PRESSING KIOSK OPERATIONAL ADVISORY")
    print(f" Evaluation Time: {args.current_time} IST | Kiosk: Om Sai Ram (Ramu Anna)")
    print("=" * 74)

    if urgent_items or total_rev >= BREAKEVEN_MARGIN_THRESHOLD_DEFAULT:
        print("\n############### >>> DECISION: [ FIRE THE COAL FURNACE NOW ] <<< ###############\n")
        print(f" Reason: {len(urgent_items)} urgent garments queued. Revenue (Rs.{total_rev:.1f}) covers fuel cost.")
    else:
        print("\n############### >>> DECISION: [ HOLD COAL - WAIT FOR EVENING BATCH ] <<< ###############\n")
        print(f" Reason: Low batch volume ({total_qty} pcs). Hold for 16:30 hostel rush.")

    print(f" * Queued Garments  : {total_qty} pieces (Urgent: {len(urgent_items)} pcs)")
    print(f" * Queued Revenue   : Rs. {total_rev:.1f}")
    print(f" * Fixed Fuel Cost  : Rs. {fuel_cost:.1f} (1.3 kg Babool Coal)")
    print(f" * Projected Margin : +Rs. {net_margin:.1f}\n")

    print("-" * 74)
    print(" OPERATIONAL THERMAL RUN-SHEET (Heavy Cotton First -> Synthetics Last)")
    print("-" * 74)
    print(f" {'Seq':<4} {'Token':<7} {'Garment Type':<16} {'Fabric Type':<20} {'Qty':<4} {'Price':<8} {'Pickup'}")
    print("-" * 74)
    sorted_q = sorted(queue, key=lambda x: x["thermal"])
    for idx, item in enumerate(sorted_q, 1):
        urg = "(!)" if "urgent" in item["urgency"].lower() else "   "
        print(f"{urg}{idx:<2} #{item['token']:<6} {item['garment']:<16} {item['fabric']:<20} {item['qty']:<4} Rs.{item['rev']:<6.1f} {item['pickup']}")
    print("=" * 74 + "\n")

if __name__ == "__main__":
    main()
