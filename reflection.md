# Step 4: Authentic Engineering Reflection
Author: Ojeshwini K. | Date: November 24, 2026

### What I Got Wrong at the Start
I initially wanted to build a "Smart Hostel Laundry Portal" where students book slots via QR code and UPI. Ten minutes inside Ramu Anna's 8x8 tin shed made that idea look ridiculous. Ramu's phone is a cracked Redmi 6A kept in a plastic pouch to keep off soot; his hands are covered in ash; and students never plan laundry - they rush in when they notice a crumpled collar 30 minutes before a viva. The problem was never customer communication; it was fuel combustion physics and the irreversible cost of lighting an unmetered solid-fuel heat source.

### What I Would Cut
I would cut the token number and customer type tracking from the CSV. In real life, Ramu uses colored safety pins (red for 3rd-year hostelers, yellow for day scholars). Digital token tracking was an unnecessary academic addition that didn't help Ramu make the core decision: Do I light the stove right now or wait?

### Where AI Helped
AI was great at calculating the non-linear relationship between ambient heat dissipation and pressing absorption to estimate the 180-minute burn curve. It also generated clean, defensive CSV parsing so malformed lines don't crash the script.

### Where AI Wasted Time
AI repeatedly suggested generic SaaS features: SQLite databases, Twilio SMS alerts, and dynamic surge pricing (charging students Rs. 15 for urgent shirts). Charging dynamic surge prices to 3rd-year seniors who eat at the same hostel mess would start a fight at the counter. I had to strip out that bloat and keep the tool focused on a single Python CLI script.
